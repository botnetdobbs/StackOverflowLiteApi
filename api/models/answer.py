from api.db import connect

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
        return {"id": self.id, "answer": self.answer}

    """Add answer to the question in the questions list
    """
    def add_answer(self, questionID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO answers 
                                (question_id, answer) VALUES(%s, %s)""", 
                                (questionID, self.answer))
                return True

    """Find an answer uniquely identified by its ID
    """
    @classmethod
    def find_by_id(cls, questionID, answerID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM answers 
                                WHERE id = %s AND question_id = %s""", 
                                (answerID, questionID))
                answer = cursor.fetchone()
                if answer:
                    return cls(answer[3], answer[0])
                else:
                    return None
    
    """Find if an answer already generated
    """
    @classmethod
    def find_by_answer(cls, questionID, answer):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM answers 
                WHERE answer = %s AND question_id = %s""", 
                (answer, questionID))
                answer = cursor.fetchone()
                if answer:
                    return True
                else:
                    return None
    
    """Get a specific answer and also the parent question
    """
    @classmethod
    def find_descriptive_single_answer(cls, answerID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT answers.id, questions.id,
                                answers.answer, answers.upvote, answers.downvote, answers.solved FROM answers
                                INNER JOIN questions ON questions.id  = answers.question_id
                                WHERE answers.id = %s""", (answerID,))
                question = cursor.fetchone()
                if question:
                    data = {"id": question[0], 
                            "question_id": question[1], 
                            "answer": question[2], 
                            "upvotes": question[3],
                            "downvotes": question[4],
                            "solved": question[5]}
                    return data

    """Get answer/s to the question in the questions list
    """
    @classmethod
    def get_answers(cls, questionID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM answers 
                                WHERE question_id = %s""", (questionID,))
                answers = cursor.fetchall()
                #Create an empty list to store the answres
                answ = []
                #Check if answer is not None
                if answers:
                    for answer in answers:
                        answ.append({"id": answer[0], 
                                    "question_id":answer[1], 
                                    "answer": answer[3], 
                                    "upvotes": answer[4],
                                    "downvotes": answer[5],
                                    "solved": answer[6]})
                    return answ
                return None


    """Update the answer object
    """
    def update(self, questionID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE answers SET 
                                answer=%s WHERE id = %s AND question_id = %s""", 
                                (self.answer, self.id, questionID))
                return True

    """Delete the answer object
    """
    def delete(self, questionID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM answers 
                                WHERE id = %s AND question_id = %s""", 
                                (self.id, questionID))
                return True
    """Upvote the answer object
    """
    def upvote(self, questionID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE answers 
                                SET upvote = upvote + %s WHERE id=%s AND question_id=%s""", 
                                (1, self.id, questionID))
                return True

    """Downvote the answer object
    """
    def downvote(self, questionID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE answers 
                                SET downvote = downvote + %s 
                                WHERE id=%s AND question_id=%s""", 
                                (1, self.id, questionID))
                return True
    
    """Mark the answer as solved
    """
    def solve(self, questionID):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE answers 
                                SET solved = %s 
                                WHERE id=%s AND question_id=%s""", 
                                (1, self.id, questionID))
                return True
        
    

