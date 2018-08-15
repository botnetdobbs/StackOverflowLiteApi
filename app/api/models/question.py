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

    """Return the object in json(dict) format
    """
    def json(self):
        return {"title": self.title, "description": self.description}

    """Find the question by id & return an object
    """
    @classmethod
    def find_by_id(cls, questionID):
        for question in questions:
            if question['id'] == questionID:
                return cls(question['title'], question['description'], questionID)
        return None

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

    """Update the question in the questions list
    """
    def update(self):
        #Create a new dictionsry
        updated_question = {
            "title": self.title,
            "description": self.description
        }
        #Check if the question dictionary exists in the questions list
        #if it matches the object id, update and return True
        #else, return False
        for question in questions:
            if question['id'] == self.id:
                question.update(updated_question)
                return True
        return False

    """Delete the question in the questions list
    """
    def delete(self):
        #Called global variable question
        global questions
        for question in questions:
            if question['id'] == self.id:
                #Filter through the list only retaining non natching questions
                questions = list(filter(lambda x: x['id'] != self.id, questions))
                return True
        return False