#Declare the data structure to store our questions and answers (List)
questions = [
    {
        "id": 1,
        "title": "The default sample title",
        "description": "The default sample QUESTION",
        "answers": [
            {
                "id": 1,
                "answer": "The default sample ANSWER"
            }
        ]
    }
]

class QuestionModel:

    """Initialise the Model class with the _id being
                an optional parameter            
        used _id since id is a Python keyword    
    """
    def __init__(self, title, description, _id=None):
        self.title = title
        self.description = description
        self.id = _id

    """Check if a question with the exact description 
                exists in the list
    """
    @classmethod
    def find_by_description(cls, description):
        for question in questions:
            if question['description'] == description:
                return True
        return False

    @classmethod
    def all(cls):
        if questions:
            return {"questions": questions}
        return None
            

    """Save the question to the questions list
    """
    def save(self):
        #Create a new question dictionary
        new_question = {
            "id": questions[-1]['id'] + 1,
            "title": self.title,
            "description": self.description,
            "answers": []
        }
        #append the dictionsry to the questions list
        questions.append(new_question)
        return new_question
