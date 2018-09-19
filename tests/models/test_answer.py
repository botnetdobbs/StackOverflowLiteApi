import pytest

from api.models.answer import AnswerModel
from api.models.question import QuestionModel
from tests.modules_for_t import teardown, create_user
from api.create_tables import create_tables

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
    assert answer.json() == {"id": None, "answer": "Return my answer in Json"}

def test_save_answer():
    create_tables()
    create_user()
    new_question = QuestionModel('My simple title', 'My simple question')
    new_question.save(1)
    samp_answer = AnswerModel("This is my sample answer")
    samp_answer.add_answer(1, 'lazarus')
    teardown()

def test_answer_find_by_id():
    create_tables()
    create_user()
    new_question = QuestionModel('My simple title', 'My simple question')
    new_question.save(1)
    samp_answer = AnswerModel("My sample answer")
    samp_answer.add_answer(1, 'lazarus')

    answer = AnswerModel.find_by_id(1, 1)
    assert answer.answer != "My simple answer"
    teardown()

def test_update():
    create_tables()
    create_user()
    new_question = QuestionModel('My simple title', 'My simple question')
    new_question.save(1)
    samp_answer = AnswerModel("This is my sample answer")
    samp_answer.add_answer(1, 'lazarus')
    new_answer = AnswerModel.find_by_id(1, 1)
    new_answer.answer = 'This is my new answer'
    assert new_answer.update(1) == True
    teardown()

def test_delete():
    create_tables()
    create_user()
    new_question = QuestionModel('My simple title', 'My simple question')
    new_question.save(1)
    samp_answer = AnswerModel("This is my sample answer")
    samp_answer.add_answer(1, 'lazarus')
    answer = AnswerModel.find_by_id(1, 1)
    assert answer.delete(1) == True
    teardown()