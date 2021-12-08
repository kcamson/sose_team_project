import pytest
from models.answer import Answer

class TestAnswer:
    def test_answerText(self):
        a = Answer("Test Answer")
        assert a.answer_text == "Test Answer"