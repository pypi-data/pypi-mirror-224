import re

def extract_json(text):
    json_data = re.search(r"\{[^\{\}]*(?:\{[^\{\}]*\}[^\{\}]*)*\}", text).group(0)
    return json_data
