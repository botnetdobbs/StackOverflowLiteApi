from api.db import connect

dbname = "stackoverflowliteapi"
def create_tables():
  with connect() as connection:
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with connection.cursor as cursor:
      cursor.execute("CREATE DATABASE "+ dbname)
      cursor.execute("CREATE TABLE users(id serial PRIMARY KEY,username character varying(60) NOT NULL,password character varying(255) NOT NUL)")
      cursor.execute("""CREATE TABLE questions (
                    id serial PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    FOREIGN KEY (user_id) 
                    REFERENCES users (id)
                    ON DELETE CASCADE ON UPDATE CASCADE)
                  """)
      cursor.execute("""CREATE TABLE answers (
                  id serial PRIMARY KEY,
                  question_id INTEGER NOT NULL,
                  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                  answer TEXT NOT NULL,
                  upvotes INT DEFAULT 0,
                  downvotes INT DEFAULT 0,
                  FOREIGN KEY (question_id) 
                  REFERENCES questions (id)
                  ON DELETE CASCADE ON UPDATE CASCADE)
                  """)

