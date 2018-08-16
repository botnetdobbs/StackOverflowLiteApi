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
                ans_id = 1
                if len(question["answers"]) > 0:
                    #Add id(auto increment to the answer)
                    ans_id = question["answers"][-1]["id"] + 1
                answer.update({"id": ans_id})
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

    """Get answer/s to the question in the questions list
    """
    @classmethod
    def get_answers(cls, questionID):
        for question in questions:
            if question['id'] == questionID:
                return {"answers": question['answers']}
        return {"message": "Question does not exist."}

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
                        question['answers'].remove(answer)
                            
        return None
        
    

