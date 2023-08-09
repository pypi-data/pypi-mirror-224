# Storing of the function's definitions and their arguments
from typing import List
from argai.func import ArgFunction
from argai.base import ArgBase, ArgRun, FunctionNotFound


class ArgFunctionStorage(ArgBase):
    def __init__(self, gpt_model: str = "gpt-3.5-turbo-0613", verbose: bool = False):
        self.functions: List[ArgFunction] = []
        super().__init__(gpt_model=gpt_model, verbose=verbose)

    def list_all(self):
        return {f.name: f for f in self.functions}

    def register(self, func):
        self.functions.append(
            ArgFunction(func, gpt_model=self.gpt_model, verbose=self.verbose)
        )

    def get_jsonschemas(self, function_names: list = []):
        schemas = []
        if function_names:
            for f in self.functions:
                if f.name in function_names:
                    schemas.append(f.jsonschema)
        else:
            for f in self.functions:
                schemas.append(f.jsonschema)
        return schemas

    def _call_func(self, function_name, function_arguments: dict, run: ArgRun = None):
        for f in self.functions:
            if f.name == function_name:
                return f._call_func(function_name, function_arguments, run=run)
        raise FunctionNotFound(f"Failed to find function with name {function_name}")

    def func_call(
        self,
        messages: list,
        function_names: list = [],
        max_calls: int = 1,
        current_call: int = 1,
        max_attempts: int = 5,
        run: ArgRun = None,
    ):
        jsonschemas = self.get_jsonschemas(function_names)
        return self._func_call(
            messages=messages,
            jsonschemas=jsonschemas,
            max_attempts=max_attempts,
            max_calls=max_calls,
            current_call=current_call,
            run=run,
        )
