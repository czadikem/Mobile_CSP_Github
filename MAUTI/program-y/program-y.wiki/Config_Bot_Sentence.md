# Sentence Splitting & Joining

This features allows you to control how sentences are split when initially read by the bot and how they are combined to display the final output.

Both of these are optional settings, and if you don't use them, the system reverts to defaults of splitting on basic English punctuation .,;:?! etc and joins sentences with fullstop 

```yaml
bot:
  splitter:
    classname: programy.dialog.splitter.regex.RegexSentenceSplitter
```

* **classname** - Python class that handles the splitting of sentences

```yaml
bot:
  joiner:
    classname: programy.dialog.joiner.SentenceJoiner
```

* **classname** - Python class that handles the joining of senttences

For more information see [Sentence Splitting](./Sentence-Splitting)
