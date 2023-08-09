import json
import openai
import inspect
from argai.utils import extract_json
from argai.base import ArgBase, ArgRun, ArgDefinition, FunctionNotFound


class ArgFunction(ArgBase):
    def __init__(
        self, func, gpt_model: str = "gpt-3.5-turbo-0613", verbose: bool = True
    ):
        self.func = func
        self.name = func.__name__
        self.code = inspect.getsource(func)
        self._jsonschema = {}
        self._func_doc = func.__doc__ if func.__doc__ else ""
        super().__init__(gpt_model=gpt_model, verbose=verbose)

    @property
    def jsonschema(self):
        if self._jsonschema:
            return self._jsonschema
        else:
            self._jsonschema = self.generate_jsonschema()
            return self._jsonschema

    @property
    def description(self):
        if self._func_doc:
            return self._func_doc
        else:
            self._func_doc = self.generate_description()
            return self._func_doc

    def _completion(self, messages, *args, **kwargs):
        response = openai.ChatCompletion.create(
            model=self.gpt_model, messages=messages, *args, **kwargs
        )
        return response

    def _call_func(
        self, function_name: str, function_arguments: dict, run: ArgRun = None
    ):
        if function_name != self.name:
            raise FunctionNotFound(f"Failed to find function with name {function_name}")
        run.log(
            f"    🏃 Running function: {run._print_func(function_name, function_arguments)}"
        )
        try:
            result = self.func(**function_arguments)
            run.log(f"    ✔️ Sucessfull, result: {str(result)}")
            return {"status": "success", "result": result}
        except Exception as e:
            error = f"{type(e).__name__}: {e}"
            run.log(f"    ❌ Errored: {error}")
            return {
                "status": "error",
                "result": f"Got the error of {error} with these arguments: {str(function_arguments)}",
            }

    def func_call(
        self,
        messages: list,
        max_calls: int = 1,
        current_call: int = 1,
        max_attempts: int = 5,
        run: ArgRun = None,
    ):
        return self._func_call(
            messages=messages,
            jsonschemas=[self.jsonschema],
            max_attempts=max_attempts,
            max_calls=max_calls,
            current_call=current_call,
            run=run,
        )

    def prompt_on_code(self, prompt: str, system_prompt: str = ""):
        final_prompt = f"```{self.code}```\n{prompt}"
        if system_prompt:
            response = self._completion(
                [
                    {"role": "user", "content": final_prompt},
                    {"role": "system", "content": system_prompt},
                ]
            )
        else:
            response = self._completion(
                [
                    {"role": "user", "content": final_prompt},
                ]
            )
        return response

    def critique(
        self,
        prompt: str = "Critique the above code, pointing out the good and bad and rate it out of 10.",
    ):
        response = self.prompt_on_code(prompt)
        response_message = response["choices"][0]["message"]["content"]
        return response_message

    def generate_description(
        self,
        prompt: str = "Write a simple description of what this function does and when to use it.",
    ):
        response = self.prompt_on_code(prompt)
        generated_description = response["choices"][0]["message"]["content"]
        return generated_description

    def generate_jsonschema(
        self,
        prompt: str = "Based on the function's code, write the JSON Schema for its parameters."
    ):
        # Generate JSON Schema
        response = self.prompt_on_code(
            prompt,
            "You are an expert at turning python functions into JSON Schema."
            "Reply only with the JSON and make sure each parameter is given a description of what it expects in plain english.",
        )
        response_message = response["choices"][0]["message"]["content"]
        generated_schema = json.loads(extract_json(response_message))

        # Convert properties to parameters
        if "properties" in generated_schema:
            generated_schema["parameters"] = {
                "type": "object",
                "properties": generated_schema["properties"],
            }
            del generated_schema["properties"]
        elif (
            "properties" not in generated_schema
            and "parameters" not in generated_schema
        ):
            generated_schema = {
                "parameters": {"type": "object", "properties": generated_schema}
            }

        # Add name and description
        generated_schema["name"] = self.name
        generated_schema["description"] = self.description

        # Remove any extra keys
        for k in list(generated_schema.keys()):
            if k not in ["name", "description", "parameters"]:
                del generated_schema[k]
        return generated_schema

    def chat(self, max_attempts: int = 5, max_calls: int = 1, exit_word:str = "exit"):
        print("===== Interactive Chat =====")
        print(f'Type {exit_word} to exit.\n')
        results = []
        message = input("Say something")
        messages = [{"role": "user", "content": message}]
        while message != exit_word:
            result = self.func_call(messages, max_attempts=max_attempts, max_calls=max_calls)
            messages = result.messages
            message = input("Say something")
            messages.append({"role": "user", "content": message})
            results.append(result)
        return results