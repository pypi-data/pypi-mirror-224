import re
import json
import inspect

class EmptyAnnotation(Exception):
    pass

def extract_json(text:str):
    json_data = re.search(r"\{[^\{\}]*(?:\{[^\{\}]*\}[^\{\}]*)*\}", text).group(0)
    return json_data

def extract_function_jsonschema(function, include_return:bool=False, raise_error_on_empty:bool=False):
    annotations = inspect.signature(function).parameters
    schema = {
        "type": "object",
        "properties": {}
    }

    for param_name, param in annotations.items():
        param_type = param.annotation.__name__
        if param_type == "_empty":
            if raise_error_on_empty:
                raise EmptyAnnotation(f"Parameter '{param_name}' has no type annotation.")
        schema["properties"][param_name] = {"type": param_type}

    if include_return:
        return_type = function.__annotations__["return"].__name__
        schema["properties"]["return"] = {"type": return_type}

    schema_json = json.dumps(schema)
    return schema_json