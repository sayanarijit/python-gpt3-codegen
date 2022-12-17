# python-gpt3-codegen

[Experimental] Auto generate code using openapi.

## Usage

With `export OPENAI_API_KEY="enter your api key here"`

```python
from python_gpt3_codegen import codegen


@codegen
def is_even(n: int) -> bool:
    """Check if a number is even."""


assert is_even(2)
assert not is_even(3)
```
