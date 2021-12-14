from models.poll import Poll
from models.answer import Answer


class TestPoll:

    def test_answer_has_two_answers(self):
        test_answers = []

        test_answer_one = Answer(answer_text="one")
        test_answer_two = Answer(answer_text="two")
        test_answers.append(test_answer_one)
        test_answers.append(test_answer_two)
        test_poll = Poll(test_answers)

        assert len(test_poll.answers) > 1



