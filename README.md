[![Build Status](https://travis-ci.com/botnetdobbs/StackOverflowLiteApi.svg?branch=master)](https://travis-ci.com/botnetdobbs/StackOverflowLiteApi)    [![Coverage Status](https://coveralls.io/repos/github/botnetdobbs/StackOverflowLiteApi/badge.svg?branch=master)](https://coveralls.io/github/botnetdobbs/StackOverflowLiteApi?branch=master)    [![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
# StackOverflowLiteApi
StackOverflowLiteApi is a question and answer platform API

# Usage
- [Get started here](https://zstackoverflowliteapi.herokuapp.com)

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
