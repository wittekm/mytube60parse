from unittest import TestCase

from mt60parse import parse_from_file


class ParseTests(TestCase):
    def test_ragefest(self) -> None:
        filepath = "input/ragefest.html"
        parsed = parse_from_file(filepath)

        assert parsed[0]["title"] == "Ludacris - Get Back"
        assert parsed[-1]["title"] == "Queen - 'We Are The Champions'"

