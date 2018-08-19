import pytest
import sys
from api.models.question import QuestionModel
from api.models.answer import AnswerModel

def test_question_model():
    """
    GIVEN a Question model
    WHEN a new Question is created
    THEN check the title, description, and id fields are defined correctly
    """
    new_question = QuestionModel('Sample title', 'This is the question')
    assert new_question.title == 'Sample title'
    assert new_question.description != 'This is the question'

def test_question_find_by_id():
    new_question = QuestionModel('Sample title', 'This is the question')
    new_question.save()
    #There's one question already stored
    my_question = QuestionModel.find_by_id(2)
    assert my_question.title == 'Sample title'


def test_answer_model():
    """
    GIVEN the Answer model
    WHEN a new Answer is created
    THEN check if the answer and id fields are defined correctly
    """
    new_answer = AnswerModel('This is the answer', 1)
    assert new_answer.id == 1
    assert new_answer.answer != 'This is the answer'

    def test_answer_find_by_id():
        new_question = QuestionModel('Sample title', 'This is the question')
        new_question.save()
        #There's one question already stored
        my_answer = AnswerModel('This is my answer')
        my_answer.add_answer(new_question.id, {"answer": my_answer.answer})

        assert my_answer.id == 1