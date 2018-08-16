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

    """Return the answer in json(dict) format
    """
    def json(self):
        return {"answer": self.answer}

    """Add answer to the question in the questions list
    """
    @classmethod
    def add_answer(cls, questionID, answer):
        for question in questions:
            if question['id'] == questionID:
                #Add id(auto increment to the answer)
                answer.update({"id": question["answers"][-1]["id"] + 1 if question["answers"][-1] else 1 })
                question["answers"].append(answer)
                return question
        return {"message": "Error adding answer."}

    """Find an answer uniquely identified by its ID
    """
    @classmethod
    def find_by_id(cls, questionID, answerID):
        for question in questions:
            if question["id"] == questionID:
                for answer in question["answers"]:
                    if answer["id"] == answerID:
                        #return an object
                        return cls(answer["answer"], answer["id"])
        return None

    """Update the answer object
    """
    def update(self, questionID):
        updated_answer = {"answer": self.answer}
        for question in questions:
            if question["id"] == questionID:
                for answer in question["answers"]:
                    if answer["id"] == self.id:
                        answer.update(updated_answer)
                        return updated_answer
        return None

    """Delete the answer object
    """
    def delete(self, questionID):
        for question in questions:
            if question['id'] == questionID:
                for answer in question['answers']:
                    if answer['id'] == self.id:
                        if question['answers'].remove(answer):
                            return {"message": "Answer deleted successfully"}
        
    

