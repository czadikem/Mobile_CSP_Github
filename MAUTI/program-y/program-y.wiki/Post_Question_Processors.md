#Post Question Processing
 
A new feature added since 3.10 is the ability to carry out additional processing on a question if the bot/brain 
combination returns empty string, essentially meaning no response was given for the input question.
 
Post question processing works almost identically to pre and post processing of question and answer. 
Post question processors are loaded and stored like pre and post processors and are actioned if ‘ask_question’ 
returns an empty response.
 
The post question processor manager loads all post processing processors on start up, and stores them in a 
chain in order in which they are specified in the configuration file postquestionprocessing.conf
 
Each post question processor then has a chance to carry out further processing on the question asked by either
 
* Carry out further processing on the question and ask it again
* Create a none AIML based response
* Create a more dynamic response than returning ‘default response’
 
If the chain of post question processors fail to return a response, then the brain reverts back to the pre v3.10 
functionality and returns the system defined default_response stored in configuration.
 
## Loading A Post Question Processor
 
All post question processors are stored in the configuration file ‘processors/postquestionprocessing.conf’ or 
the ‘postquestionprocessing’ table if using SQL storage. Each processor defined as the full python class path, e.g
 
```ini
programy.processors.postquestion.lemmatize.LemmatizePostQuestionProcessor
programy.processors.postquestion.stemming.StemmingPostQuestionProcessor
programy.processors.postquestion.stopwords.StopWordsPostQuestionProcessor
```
 
## Available Post Question Processors

The available post processors are currently

* **LemmatizePostQuestionProcessor**. Lemmatizes the string, replace any plural words with singular, e.g mice to mouse
* **StemmingPostQuestionProcessor**. Applies Stemming to the string, reducing each word to its base stemm, e.g troubled, troubles and troubling to troubl
* **StopWordsPostQuestionProcessor**. Removes all stop words from the string, e.g as, is, the etc
 
## Building Your Own Post Question Processors
 
Post Question Processors inherit from the abstract base class

```python
programy.processors.processing.PostQuestionProcessor
```

The class has a single method, process, which takes bot, client and the string to post-process and should return the processed string

```python
    class PostQuestionProcessor(Processor):
        def __init__(self):
            Processor.__init__(self)

        @abstractmethod
        def process(self, bot, clientid, string):
            pass
```

Once built and tested the path to the class needs to be appened to PYTHONPATH system variable

## Addendum
This functionality was added to the code base by developer `ksenia1997`

