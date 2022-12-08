# Post Processors
Post processors converts the raw answer after it has been returned from the brain.

Post processors are chained together, and are called in the sequence order in which they are defined in their 
configuration file `postprocessors.conf`. Each post processor is listed as the full Python class path.

As an example the current Y-Bot post processor configuration looks like this. A line starting with a `#` shows that 
post processor is commented out

```ini
programy.processors.post.denormalize.DenormalizePostProcessor
programy.processors.post.formatpunctuation.FormatPunctuationProcessor
programy.processors.post.formatnumbers.FormatNumbersPostProcessor
programy.processors.post.multispaces.RemoveMultiSpacePostProcessor
programy.processors.post.removehtml.RemoveHTMLPostProcessor
programy.processors.post.consoleformat.ConsoleFormatPostProcessor
#programy.processors.post.translate.TranslatorPostProcessor
#programy.processors.post.emojize.EmojizePostProcessor
```

## Available Post Processors

The available post processors are currently

* **DenormalizePostProcessor**. Denormalises the output into more human readable english.
* **FormatPunctuationProcessor**. Formats punctuation by removing/adding spaces etc.
* **FormatNumbersPostProcessor**. Formats numbers by converting to numeric values and removing spaces.
* **RemoveMultiSpacePostProcessor**. Removes multipl spaces added by the parser.
* **RemoveHTMLPostProcessor**. Removes HTML.
* **ConsoleFormatPostProcessor**. Formats the output for 80 character width consoles
* **TranslatorPostProcessor**. Translates the text using Google Translate.
* **EmojizePostProcessor**. Replaces emoji character strings with the pictorial equivalent.

## Building Your Own Post Processor

Post Processors inherit from the abstract base class

```python
programy.processors.processing.PostProcessor
```

The class has a single method, process, which takes bot, client and the string to post-process and should return the processed string

```python
    class PostProcessor(Processor):
        def __init__(self):
            Processor.__init__(self)

        @abstractmethod
        def process(self, bot, clientid, string):
            pass
```

Once built and tested the path to the class needs to be appened to PYTHONPATH system variable