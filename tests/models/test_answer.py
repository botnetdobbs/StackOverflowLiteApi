import pytest

from api.models.answer import AnswerModel
from api.models.question import QuestionModel

def test_new_answer_item():
    """
    GIVEN the Answer model
    WHEN a new Answer is created
    THEN check the answer field if defined
    """
    answer = AnswerModel("This is my answer")
    assert answer.id == None
    assert answer.answer != 'This is a wrong answer'
    assert answer.answer == 'This is my answer'

def test_answer_json():
    answer = AnswerModel("Return my answer in Json")
    assert answer.json() == {"answer": "Return my answer in Json"}

def test_save_answer():
    new_question = QuestionModel('My simple title', 'My simple question')
    new_question.save(1)
    samp_answer = AnswerModel("This is my sample answer")
    samp_answer.add_answer(1)

def test_answer_find_by_id():
    new_question = QuestionModel('My simple title', 'My simple question')
    new_question.save(1)
    samp_answer = AnswerModel("My sample answer")
    samp_answer.add_answer(1)

    answer = AnswerModel.find_by_id(1, 1)
    assert answer.answer == "My simple answer"

def test_for_non_existing_question():
    assert AnswerModel.get_answers(1) == {"message": "Question does not exist."}

def test_update():
    new_question = QuestionModel('My simple title', 'My simple question')
    new_question.save(1)
    samp_answer = AnswerModel("This is my sample answer")
    samp_answer.add_answer(1)
    new_answer = AnswerModel.find_by_id(1, 1)
    new_answer.answer = 'This is my new answer'
    assert new_answer.update(1) == True

def test_delete():
    new_question = QuestionModel('My simple title', 'My simple question')
    new_question.save(1)
    samp_answer = AnswerModel("This is my sample answer")
    samp_answer.add_answer(1)
    answer = AnswerModel.find_by_id(1, 1)
    assert answer.delete(1) == True