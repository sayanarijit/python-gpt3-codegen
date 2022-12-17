__version__ = "0.1.0"

import inspect
import os

import openai
from diskcache import Cache

openai.api_key = os.getenv("OPENAI_API_KEY")
cache = Cache("__python_gpt3_codegen_cache__")


def codegen(obj):
    name = obj.__name__
    doc = obj.__doc__
    sig = inspect.signature(obj)

    def_ = "def"
    if type(obj) == type:
        def_ = "class"

    repr_ = f"""{def_} {name}{sig}:
    '''{doc}'''
    """

    if repr_ in cache:
        completed = cache[repr_]
    else:
        resp = openai.Edit.create(
            model="text-davinci-edit-001",
            input=repr_,
            instruction="Complete the definition",
        )

        completed = resp.choices[0].text
        cache[repr_] = completed

    exec(completed)
    return eval(name)
