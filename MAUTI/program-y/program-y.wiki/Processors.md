# Processors
Processors allow you to change the content of the question or answer, or to modify the question 
in flight and retry if the question does not illicit a valid response.

At this time there are 3 types of processors

* [Pre Processors](./Pre_Processors). Which converts the raw text of the question entered into the bot before it is passed to the brain to answer.

* [Post Processors](./Post_Processors). Which converts the raw answer after it has been returned from the brain.

* [Post Question Processors](./Post_Question_Processors). Can be used to manipulate the question after an initial 
response was blank and then retry the question.
