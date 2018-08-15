#Import the data structure
from api.models.question import questions

class AnswerModel:

    """Initialise the Model class with the _id being
                an optional parameter            
        used _id since id is a Python keyword    
    """
    def __init__(self, answer, _id=None):
        self.id = _id
        self.answer = answer

    """Add answer to the question in the questions list
    """
    @classmethod
    def add_answer(cls, questionID, answer):
        for question in questions:
            if question['id'] == questionID:
                #Add id(auto increment to the answer)
                answer.update({"id": question["answers"][-1]["id"] + 1})
                question["answers"].append(answer)
                return question
        return {"message": "Error adding answer."}

