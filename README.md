[![Build Status](https://travis-ci.com/botnetdobbs/StackOverflowLiteApi.svg?branch=master)](https://travis-ci.com/botnetdobbs/StackOverflowLiteApi)
# StackOverflowLiteApi
StackOverflowLiteApi is a question and answer platform API

#Usage
- [Heroku-Link](https://zstackoverflowliteapi.herokuapp.com/api/v1/questions)

## Endpoints to the API
1. Posting a question
- POST _http://127.0.0.1:500/api/v1/questions_

2. Fetch all questions
- GET _http://127.0.0.1:500/api/v1/questions_

3. Fetch a specific question
- GET _http://127.0.0.1:500/api/v1/questions/<<int:questionID>>_

4. Edit a specific question
- PUT _http://127.0.0.1:500/api/v1/questions/<<int:questionID>>_

5. Delete a specific question
- DELETE _http://127.0.0.1:500/api/v1/questions/<<int:questionID>>_

6. Posting an answer to the specific question
- POST _http://127.0.0.1:500/api/v1/questions/<<int:questionID>>/answers_

7. Fetch an answer(s) to the specific question
- GET _http://127.0.0.1:500/api/v1/questions/<<int:questionID>>/answers_

8. Fetch a specific answer from a specific question
- GET _http://127.0.0.1:500/api/v1/questions/<<int:questionID>>/answers<<int:answerID>>_

9. Edit a specific answer from a specific question
- PUT _http://127.0.0.1:500/api/v1/questions/<<int:questionID>>/answers<<int:answerID>>_

10. Delete a specific answer from a specific question
- DELETE _http://127.0.0.1:500/api/v1/questions/<<int:questionID>>/answers<<int:answerID>>_

NB:-Unique Identifiers
> <<int:questionID>>
> <<int:answerID>>
