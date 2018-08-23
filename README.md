[![Build Status](https://travis-ci.com/botnetdobbs/StackOverflowLiteApi.svg?branch=master)](https://travis-ci.com/botnetdobbs/StackOverflowLiteApi)    [![Coverage Status](https://coveralls.io/repos/github/botnetdobbs/StackOverflowLiteApi/badge.svg?branch=master)](https://coveralls.io/github/botnetdobbs/StackOverflowLiteApi?branch=master)    [![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
# StackOverflowLiteApi
StackOverflowLiteApi is a question and answer platform API

NB: Challenge 2 is in the challenge2 branch

# Usage
- [Get started here](https://zstackoverflowliteapi.herokuapp.com)

- clone the Repo `git clone https://github.com/botnetdobbs/StackOverflowLiteApi.git`
- Install Virtualenv `pip install virtualenv`
- navigate to project folder `cd StackOverflowLiteApi`
- Create the virtual environment `virtualenv venv`
## Activate the virtualenv 
- Windows: `.\venv\Scripts\activate`
- Linux. `source venv/bin/activate`
# Testing
Use [Postman](https://www.getpostman.com)

- Create [Variables](http://blog.getpostman.com/2014/02/20/using-variables-inside-postman-and-collection-runner/) for your requests to avoid typing the long urls
-On the POST endpoint for login, go to the "tests" tab and add thie following
```javascript
const jsonData = JSON.parse(responseBody);
postman.setEnvironmentVariable("jwt_token", jsonData.access_token);
```
-That {{jwt_token}} variable created is being populated with the access token. Now go to the necessary endpoints endpoints and set up the headers
```
Key: Authorization
Value: JWT {{jwt_token}}
```
-Register, login and enjoy...

## Endpoints to the API
1. Posting a question
- POST _http://127.0.0.1:5000/api/v1/questions_

2. Fetch all questions
- GET _http://127.0.0.1:5000/api/v1/questions_

3. Fetch a specific question
- GET _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>_

4. Edit a specific question
- PUT _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>_

5. Delete a specific question
- DELETE _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>_

6. Posting an answer to the specific question
- POST _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>/answers_

7. Fetch an answer(s) to the specific question
- GET _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>/answers_

8. Fetch a specific answer from a specific question
- GET _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>/answers<<int:answerID>>_

9. Edit a specific answer from a specific question
- PUT _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>/answers<<int:answerID>>_

10. Delete a specific answer from a specific question
- DELETE _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>/answers<<int:answerID>>_

11. Upvote a question
- PUT _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>/answers/<<int:answerID>>/upvote

12. Downvote a question
- PUT _http://127.0.0.1:5000/api/v1/questions/<<int:questionID>>/answers/<<int:answerID>>/downvote

11. Register as a user
- PUT _http://127.0.0.1:5000/api/v1/auth/register_

11. Login as a user
- PUT _http://127.0.0.1:5000/api/v1/auth/login_

NB:-Unique Identifiers
> <<int:questionID>>
> <<int:answerID>>


