import json
from textwrap import dedent

from bq_tabulate import tool


def test_arithmetic():
    with open("tests/example.json") as infile:
        example_json = json.load(infile)
    actual = tool.bq_tabulate(example_json)
    expected = dedent(
        """\
        category         f0_
        -----------  -------
        documentary     1568
        action       1758089
        drama          93642
        comedy        700800"""
    )
    assert actual == expected
