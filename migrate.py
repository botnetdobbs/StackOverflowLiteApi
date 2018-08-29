import psycopg2
from api.db import connect
 
 
def migrate():
    """ create tables in the PostgreSQL database"""
    commands = (
        "GRANT ALL ON SCHEMA public TO public",
        """CREATE TABLE users (
                            id serial PRIMARY KEY,
                            username character varying(60) NOT NULL,
                            email character varying(60) NOT NULL,
                            password character varying(255) NOT NULL
                            )
                            """,
        """CREATE TABLE questions (
                            id serial PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            title TEXT NOT NULL,
                            description TEXT NOT NULL,
                            FOREIGN KEY (user_id) 
                            REFERENCES users (id)
                            ON DELETE CASCADE ON UPDATE CASCADE
                            )
                            """,
        """CREATE TABLE answers (
                            id serial PRIMARY KEY,
                            question_id INTEGER NOT NULL,
                            answer TEXT NOT NULL,
                            upvote INT DEFAULT 0,
                            downvote INT DEFAULT 0,
                            solved INT DEFAULT 0,
                            FOREIGN KEY (question_id) 
                            REFERENCES questions (id)
                            ON DELETE CASCADE ON UPDATE CASCADE)
                            """)
    with connect() as connection:
        with connection.cursor() as cursor:
            for command in commands:
                cursor.execute(command)
 
 
if __name__ == '__main__':
    migrate()