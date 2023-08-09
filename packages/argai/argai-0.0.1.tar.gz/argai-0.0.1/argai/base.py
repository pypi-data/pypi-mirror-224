import json
import openai
from pydantic import BaseModel
from abc import ABC, abstractmethod
from typing import Optional, Type


class FunctionNotFound(Exception):
    pass


class ArgDefinition(BaseModel):
    name: str
    description: str
    jsonschema: str
    name_for_human: Optional[str]
    description_for_human: Optional[str]


class ArgRun:
    """
    Class to store the results of the run
    """
    def __init__(self, gpt_model: str = "gpt-3.5-turbo-0613", verbose: bool = False, **kwargs):
        self.gpt_model = gpt_model
        self.verbose = verbose
        self.output = None
        self.status = None
        self.messages = []  # Conversation
        self.results = []  # Cleaned results
        self.logs = []  # Log of prints
        self.attempt_logs = {}
        self.tokens_used = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        }

    def __iter__(self):
        for k, v in self.to_dict().items():
            yield k, v

    def __str__(self):
        return self.output

    def __getitem__(self, index):
        return self.to_dict()[index]

    def __repr__(self):
        return f".output: {self.__str__()}\n.status: {self.status}\nalso available: .results .messages, .logs, .attempt_logs, .tokens_used" 

    def to_dict(self):
        return {
            "output" : self.output,
            "status" : self.status,
            "messages": self.messages,
            "results": self.results,
            "logs": self.logs,
            "attempt_logs": self.attempt_logs,
            "tokens_used": self.tokens_used,
        }
    
    def log(self, message):
        if self.verbose:
            print(message)
        self.logs.append(message)

    def _count_token(self, response):
        self.tokens_used["prompt_tokens"] += response["usage"]["prompt_tokens"]
        self.tokens_used["completion_tokens"] += response["usage"]["completion_tokens"]
        self.tokens_used["total_tokens"] += response["usage"]["total_tokens"]

    def _completion(self, messages, prefix="", *args, **kwargs):
        response = openai.ChatCompletion.create(
            model=self.gpt_model, messages=messages, *args, **kwargs
        )
        self._count_token(response)
        return response

    def _print_func(self, function_name, function_arguments):
        arg_str = ", ".join(
            [f"{key}={repr(value)}" for key, value in function_arguments.items()]
        )
        return f"{function_name}({arg_str})"

    def format_llm_messages(self, message, *args, **kwargs):
        if message["role"] == "user":
            return f'💬: {message["content"]}'
        elif message["role"] == "assistant":
            return f'🤖: {message["content"]}'
        elif message["role"] == "function":
            if "args" in kwargs:
                return f'🌟: Ran {self._print_func(message["name"], message["args"])}, result: {message["content"]}'
            else:
                return f'🌟: Ran {message["name"]}, result: {message["content"]}'
        elif message["role"] == "system":
            return f'🖥️: {message["content"]}'
        else:
            return f'❓: {message["content"]}'


class ArgBase(ABC):
    def __init__(self, gpt_model: str = "gpt-3.5-turbo-0613", verbose: bool = False):
        self.gpt_model = gpt_model
        self.verbose = verbose

    def _check_schema_for_function(self, function_name: str, jsonschemas: list):
        for f in jsonschemas:
            if f["name"] == function_name:
                return f
        raise FunctionNotFound(f"Failed to find function with name {function_name}")

    @abstractmethod
    def _call_func(self, function_name, function_arguments, run: ArgRun = None):
        pass

    def _llm_func_call(
        self,
        messages: list,
        jsonschemas: list,
        max_attempts: int = 1,
        current_attempt: int = 1,
        run: ArgRun = None,
    ):
        # check
        if current_attempt > 1:
            run.log(f"    ️‍🩹 Self-heal attempt {current_attempt} | 📝 Calling LLM:")
        else:
            run.log(f"    📝 Calling LLM")

        response = run._completion(messages, functions=jsonschemas)
        response_message = response["choices"][0]["message"]
        run.messages = messages + [dict(response_message)]

        if "function_call" in response_message:
            response_func_call = response_message["function_call"]
            func_args = None
            func_name = response_func_call["name"]
            try:
                func_args = json.loads(response_func_call["arguments"])
                func_output = self._call_func(func_name, func_args, run=run)
            except FunctionNotFound:
                func_output = {
                    "status": "error",
                    "result": f"Error, the function name {func_name} is not a provided function name.",
                }
            except:
                import traceback

                traceback.print_exc()
                func_output = {
                    "status": "error",
                    "result": f"Error, the arguments provided to the {func_name} function is not a valid json. The arguments provided were: {response_func_call['arguments']}.",
                }
            run.output = func_output["result"]
            run.status = func_output["status"]

            if func_output["status"] == "success":
                result = {
                    "name": func_name,
                    "status": "function_called",
                    "arguments": response_func_call["arguments"],
                    "result": func_output["result"],
                }
            else:  # errored and now attempting to self-heal and rerun
                run.log(f"    ❌ {func_output['result']}")
                if max_attempts == current_attempt:
                    # if max attempts reached, return error
                    if func_args:
                        result = {
                            "name": func_name,
                            "status": "failed_function_called",
                            "arguments": func_args,
                            "result": func_output["result"],
                        }
                    else:
                        result = {
                            "name": func_name,
                            "status": "failed_function_called",
                            "arguments": response_func_call["arguments"],
                            "result": func_output["result"],
                        }
                else:
                    # if max attempts not reached, rerun with the function's error message
                    result = self._llm_func_call(
                        messages=messages
                        + [
                            response_message,
                            {
                                "role": "function",
                                "name": func_name,
                                "content": func_output["result"],
                            },
                        ],
                        jsonschemas=jsonschemas,
                        max_attempts=max_attempts,
                        current_attempt=current_attempt + 1,
                        run=run,
                    )
        else:
            # no function called
            result = {
                "status": "no_function_called",
                "result": response_message["content"],
            }
        return result

    def _single_func_call(
        self,
        messages: list,
        jsonschemas: list,
        max_attempts: int = 1,
        run: ArgRun = None,
    ):
        return self._llm_func_call(
            messages=messages,
            jsonschemas=jsonschemas,
            max_attempts=max_attempts,
            run=run,
        )

    def _func_call(
        self,
        messages: list,
        jsonschemas: list,
        max_calls: int = 5,
        current_call: int = 1,
        max_attempts: int = 5,
        run: ArgRun = None,
    ):
        # if messages is a string, convert it to a list
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]

        if run is None:
            run = ArgRun(gpt_model=self.gpt_model, verbose=self.verbose)

        run.log(f"{current_call}: {run.format_llm_messages(messages[-1])}")

        result = self._single_func_call(
            messages, jsonschemas=jsonschemas, max_attempts=max_attempts, run=run
        )

        if max_calls != 1 and max_calls == current_call:
            # stop if max calls reached
            run.log(f"Max calls of {max_calls} reached.")
            run.results.append(result)
            return run
        else:
            # continue if max calls not reached
            if result["status"] == "function_called":
                run.results.append(result)
                self._func_call(
                    messages
                    + [
                        {
                            "role": "assistant",
                            "content": None,
                            "function_call": {
                                "name": result["name"],
                                "arguments": str(result["arguments"]),
                            },
                        },
                        {
                            "role": "function",
                            "name": result["name"],
                            "content": str(result["result"]),
                        },
                    ],
                    jsonschemas=jsonschemas,
                    max_calls=max_calls,
                    current_call=current_call + 1,
                    run=run,
                )
                return run
            else:
                run.results.append(result)
                run.log(f"{current_call+1}: {run.format_llm_messages(run.messages[-1])}")
                return run
