# Normalization

An AIML chat bot works best when it is presented with a pure strong of words, with no punctuation, abbreviations and symbols. However good English language processing rarely fits this pattern, and so we need to be able to remove these difficult to process items, replacing them with textual representations. This is the role of the normalization and denormalization processes.

* Normalization removes a wide range of difficult to parse textual elements and replaces them text strings that represent their value

* Denormalisation is the reverse process, taking the very pure text output from the bot and replaces, where it can, text with their representative symbols and abbreivations. 

This whole process is best explained using some examples. 

1. Consider you want to parse an email address such as keiffster@gmail.com. During the normalization process this would be converted to keiffster at gmail dot com, which is the easily converted into an AIML pattern `<pattern>* at * dot com</pattern`

2. There are many ways the user could say `aren't`, such as `are not`, `arent', `aren't` etc. The normaliser will convert all of these into `are not`, making pattern matching much simpler

## Preprocessing
The normalization process is carried out by the `NormalizePreProcessor`, which is normally included in the preprocessors.conf file found in storage folder and referenced in your yaml configuration file. This class is usually the first or only entry so that the normalized text can be passed to all other processors.

```bash
programy.processors.pre.normalize.NormalizePreProcessor
```

This normalizer uses the contents of the file `storage/lookups/normal.txt` to decide which to symbols, words and abbreviations to normalize. Examples of which are

### HTML Conversions
```bash
"%20"," "
"%26","&"
"%2C",","
"%2c",","
"%28","("
"%29",")"
"%21","!"
```
### URL Conversions
```bash
".com"," dot com "
".org"," dot org "
".edu"," dot edu "	
".gov"," dot gov "
".uk"," dot uk " 	
".net"," dot net " 	
```

### Text Conversions
```bash
" aren t "," are not "
" aren.t "," are not "
" arent "," are not "
" aren't "," are not "
" are'nt "," are not "
" arn t "," are not "
```

### Basic Spelling
```bash 
" becasue "," because "
" becouse "," because "
" becuase "," because "
```

### Symbols
```bash
"-"," dash "
"#"," sharp "
"$"," dollarsign "
```

If you decide not to use the normalize preprocessing function, you can also use the `<normalize>` tag to normalize individual words. For more information on how to use this tag see [Normalize Tag](https://github.com/keiffster/program-y/wiki/Template-Tags#normalize)

## Postprocessing

Denormalisation is the reverse process

The denormalization process is carried out by the `DenormalizePreProcessor`, which is normally included in the postprocessors.conf file found in the storage folder and referenced in your yaml configuration file. This class is usually the last or only entry so that the denormalized text can be processed after all other post processing has taken place

```bash
programy.processors.post.denormalize.DenormalizePostProcessor
```

This denormalizer uses the contents of the file `storage/lookups/denormal.txt` to decide which to symbols, words and abbreviations to normalize. 

If you decide not to use the denormalize preprocessing function, you can also use the `<denormalize>` tag to denormalize individual words. For more information on how to use this tag see [Dernomalize Tag](https://github.com/keiffster/program-y/wiki/Template-Tags#denormalize)

## More Information
For more information about the above and how to create your own processors, see [Pre & Post Processing](https://github.com/keiffster/program-y/wiki/Processors)

