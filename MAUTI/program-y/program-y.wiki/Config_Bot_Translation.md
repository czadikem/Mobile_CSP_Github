# Translation Configuration

```yaml
bot:
  translator:
    classname: programy.translate.textblob_translator.TextBlobTranslator
    from: fr
    to: en 
```

* **classname** - The Python class to use for translating to and from text
* **from** - The language to convert from to internal English representation of the grammar
* **to** - The language to convert to before displaying.

If you leave any of them  blank it will attempt to determine the language and translate it into English

For more information see [Translation](./Translation)
