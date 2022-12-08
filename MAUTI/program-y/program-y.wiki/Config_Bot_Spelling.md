# Bot Spelling Configuration

The spelling configuration is used to define the class Program-Y why uses to spell check each sentence. The spelling checker relies on a corpus of words that you used to determine the correct spelling. The larger this file, the longer spelling takes to loader and the longer it takes to check spelling, but the more accurate the check will be.

```yaml
bot:
    spelling:
      classname: programy.utils.spelling.checker.SpellingChecker
      corpus: $BOT_ROOT/spelling/corpus.txt
      check_before: false
      check_and_retry: false
```
There are 2 options to control how spelling is performed, either check the spelling of every sentence or to only check if the sentence fails a response, then the sentence is corrected and the question asked again. The former is slightly slower but will give greater accuracy, while the latter will be faster, but may result in incorrect spellings create false responses

For more information see [Spelling](./Spelling)
