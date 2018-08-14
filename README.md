# StackOverflowLiteApi
StackOverflowLiteApi is a question and answer platform API

## Endpoints to the API
1. Posting a question
- POST _http://127.0.0.1:500/api/v1/question_

2. Fetch all questions
- GET _http://127.0.0.1:500/api/v1/question_

2. Fetch a specific question
- GET _http://127.0.0.1:500/api/v1/question/<<int:questionID>>_

3. Posting an answer to the a question
- POST _http://127.0.0.1:500/api/v1/question/<<int:questionID>>/answers_

3. Posting an answer to the a question
- POST _http://127.0.0.1:500/api/v1/question/<<int:questionID>>/answers_

NB:-Unique Identifier
> <<int:questionID>>
