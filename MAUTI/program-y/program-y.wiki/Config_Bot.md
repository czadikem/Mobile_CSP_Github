# Bot Configuration Overrides

Bot configuration consists of a number of options which control the overall behaviour of the chat bot, it is made up of core settings and also the following sub sections

* **[Brains](./Config_Bot_Brains)**
* **[Default Responses](./Config_Bot_Defaults)**
* **[Initial Questions](./Config_Bot_Questions)**
* **[Initial Max Search](./Config_Bot_MaxSearch)**
* **[Initial Overrides](./Config_Bot_Overrrides)**
* **[Initial Exit](./Config_Bot_Exit)**
* **[Spelling](./Config_Bot_Spelling)**
* **[Translations](./Config_Bot_Translation)**
* **[Sentiment Analysis](./Config_Bot_Sentiment)**
* **[Conversations](./Config_Bot_Conversation)**
* **[Sentence Splitting/Joining](./Config_Bot_Sentence)**

## Example

```yaml
        bot:
            brain_selector: programy.bot.DefaultBrainSelector

            initial_question: Hi, how can I help you today?
            initial_question_srai: YINITIALQUESTION

            default_response: Sorry, I don't have an answer for that!
            default_response_srai: YDEFAULTRESPONSE
            empty_string: YEMPTY
            
            exit_response: So long, and thanks for the fish!
            exit_response_srai: YEXITRESPONSE
            
            override_properties: true
            
            max_question_recursion: 1000
            max_question_timeout: 60
            max_search_depth: 100
            max_search_timeout: 60
            
            spelling:
              load: true
              classname: programy.spelling.norvig.NorvigSpellingChecker
              alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
              check_before: true
              check_and_retry: true
              
            splitter:
                classname: programy.dialog.splitter.regex.RegexSentenceSplitter

            joiner:
                classname: programy.dialog.joiner.SentenceJoiner

            conversations:
              save: true
              load: false
              max_histories: 100
              restore_last_topic: false
              initial_topic: TOPIC1
              empty_on_start: false
        
            from_translator:
                classname: programy.translate.textblob_translator.TextBlobTranslator
                from: fr
                to: en 

            to_translator:
                classname: programy.translate.textblob_translator.TextBlobTranslator
                from: en
                to: fr

            sentiment:
                classname: programy.sentiment.textblob_sentiment.TextBlobSentimentAnalyser
                scores: programy.sentiment.scores.SentimentScores
```