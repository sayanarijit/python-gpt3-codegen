from python_gpt3_codegen import codegen


@codegen
def is_even(n: int) -> bool:
    """Check if a number is even."""


def test_codegen():
    assert is_even(2)
    assert not is_even(3)
