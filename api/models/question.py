from api.db import connect

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
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM questions WHERE id = %s", (questionID,))
                question = cursor.fetchone()
                if question:
                        return cls(question[2], question[3], questionID)
                else:
                    return None

    """Check if a question with the exact description 
                exists in the questions table
    """
    @classmethod
    def find_by_description(cls, description):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM questions 
                                WHERE description = %s""", (description,))
                question = cursor.fetchone()
                if question:
                    return True
                else:
                    return None

    @classmethod
    def find_by_user_id(self, userID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT questions.id, users.username, 
                                questions.title, questions.description 
                                FROM questions 
                                INNER JOIN users ON users.id = questions.user_id
                                WHERE user_id=%s""", (userID,))
                questions = cursor.fetchall()
                #If questions is not None, loop through the questions
                #append them in the quest list as dictionaries
                if questions:
                    #Create an empty list for storing the questions
                    quest = []
                    for q in questions:
                        quest.append({"id": q[0], 
                                        "author":q[1], 
                                        "title": q[2], 
                                        "description": q[3]})
                    return quest
                else:
                    return None

    """Get a specific question and also the parent user
    """    
    @classmethod
    def find_descriptive_single_question(cls, questionID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT questions.id, questions.title, 
                                questions.description, users.username FROM questions
                                INNER JOIN users ON users.id  = questions.user_id
                                WHERE questions.id = %s""", (questionID,))
                question = cursor.fetchone()
                if question:
                    data = {"id": question[0], 
                            "title": question[1], 
                            "description": question[2], 
                            "author": question[3]}
                    return data

    """Get all questions from the questions table
    """
    @classmethod
    def all(cls):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT questions.id, questions.title, 
                                questions.description, users.username FROM questions
                                INNER JOIN users ON users.id  = questions.user_id""")
                questions = cursor.fetchall()
                #If questions is not None, loop through the questions
                #append them in the quest list as dictionaries
                if questions:
                    #Create an empty list for storing the questions
                    quest = []
                    for q in questions:
                        quest.append({"id": q[0], 
                                        "title":q[1], 
                                        "description": q[2], 
                                        "author": q[3]})
                    return quest
                else:
                    return None
            

    """Save the question to the questions table
    """
    def save(self, user_id):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO questions
                                (user_id, title, description) 
                                VALUES(%s, %s, %s)""", 
                                (user_id, self.title, self.description))
                return {"message": "Question created successfully."}  

    """Update the question in the questions table
    """
    def update(self):
        #update the object and return True
        #else, return False
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE questions 
                                SET title=%s, description=%s WHERE id=%s""", 
                                (self.title, self.description, self.id))
                return True

    """Delete the question in the questions table
    """
    def delete(self):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM questions WHERE id=%s", (self.id,))
                return True