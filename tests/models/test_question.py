import pytest
from api.models.question import QuestionModel
from flask import jsonify
from tests.modules_for_t import teardown, create_user
from api.create_tables import create_tables


def test_new_question_item():
    """
    GIVEN a Question model
    WHEN a new Question is created
    THEN check the title, description, and id fields are defined correctly
    """
    new_question = QuestionModel('This is a sample title', 'This is a sample description')

    assert new_question.title == 'This is a sample title'
    assert new_question.description == 'This is a sample description'

def test_question_find_by_id():
    """
    Given a new question saved
    When a query is called by id
    Then a new object should be returned, check if the fields are correct
    """
    create_tables()
    create_user()
    new_question = QuestionModel('This is a sample 1 title', 'This is a sample 1 description')
    new_question.save(1)
    #It's the first to be stored hence id == 1
    question = QuestionModel.find_by_id(1)
    assert question.title == 'This is a sample 1 title'

    new_question1 = QuestionModel('This is a sample 2 title', 'This is a sample 2 description')
    new_question1.save(1)
    
    question1 = QuestionModel.find_by_id(2)
    assert question1.title == 'This is a sample 2 title'
    teardown()

def test_question_find_by_description():
    """
    Given a new question saved
    When a query is called by description
    Then a boolean is returned, check if the fields are correct
    """
    create_tables()
    create_user()
    new_question = QuestionModel('This is a sample 1 title', 'This is a sample 1 description')
    new_question.save(1)
    #It's the first to be stored hence id == 1
    question = QuestionModel.find_by_description('This is a sample 1 description')
    assert question == True
    teardown()


def test_json():
    create_tables()
    create_user()
    my_question = QuestionModel('Json title', 'Json description')
    my_question.save(1)

    question_query = QuestionModel.find_by_id(1)
    assert question_query.json() == {"title": 'Json title', "description": 'Json description'}
    teardown()

def test_delete():
    """
    GIVEN a new question saved
    WHEN a new query is passed for deletion
    THEN it should return True
    """
    create_tables()
    create_user()
    new_question = QuestionModel('This is a sample title', 'This is a sample description')
    new_question.save(1)

    question = QuestionModel.find_by_id(1)
    assert question.delete() == True
    teardown()