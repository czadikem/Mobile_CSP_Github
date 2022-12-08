#Pre Processor

Pre Processors converts the raw text of the question entered into the bot before it is passed to the brain to answer.

Pre processors are chained together, and are called in the sequence order in which they are defined in their 
configuration file `preprocessors.conf`. Each pre processor is listed as the full Python class path.

As an example the current Y-Bot pre processor configuration looks like this. A line starting with a `#` shows that 
pre processor is commented out

```ini
programy.processors.pre.normalize.NormalizePreProcessor
programy.processors.pre.removepunctuation.RemovePunctuationPreProcessor
#programy.processors.pre.demojize.DemojizePreProcessor
#programy.processors.pre.splitchinese.SplitChinesePreProcessor
#programy.processors.pre.toupper.ToUpperPreProcessor
#programy.processors.pre.translate.TranslatorPreProcessor
#programy.processors.pre.wordtagger.WordTaggerPreProcessor
#programy.processors.pre.lemmatize.LemmatizePreProcessor
#programy.processors.pre.stemming.StemmingPreProcessor
#programy.processors.pre.stopwords.StopWordsPreProcessor
```

## Available Pre Processors

The available pre processors are currently

* **NormalizePreProcessor**. Normalises the input replacing abbreviations and punctuation and replacing numbers with word.
* **RemovePunctuationPreProcessor**. Remove all punctuation from the sentence.
* **DemojizePreProcessor**. Replaces emoji character strings with word equivalents.
* **SplitChinesePreProcessor**. Splits the sentence based on chinese language grammar rules. 
* **ToUpperPreProcessor**. Converts all text to upper case.
* **TranslatorPreProcessor**. Translate the language using Google translate.
* **WordTaggerPreProcessor**. Using NLP to tag each word with its grammar definition. See [NLP](./Natural_Language_Processing) for more details.
* **LemmatizePreProcessor**. Lemmatizes the string, replace any plural words with singular, e.g mice to mouse. See [NLP](./Natural_Language_Processing) for more details.
* **StemmingPreProcessor**. Applies Stemming to the string, reducing each word to its base stemm, e.g troubled, troubles and troubling to troubl. See [NLP](./Natural_Language_Processing) for more details.
* **StopWordsPreProcessor**. Removes all stop words from the string, e.g as, is, the etc. See [NLP](./Natural_Language_Processing) for more details

## Building Your Own Pre Processor

Pre Processors inherit from the abstract base class

```python
programy.processors.processing.PreProcessor
```

The class has a single method, process, which takes bot, client and the string to pre-process and should return the processed string

```python
    class PreProcessor(Processor):

        def __init__(self):
            Processor.__init__(self)

        @abstractmethod
        def process(self, bot, clientid, string):
            pass
```

Once built and tested the path to the class needs to be appened to PYTHONPATH system variable