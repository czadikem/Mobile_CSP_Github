# Chinese Support

Program-y now supports Chinese characters, format and layout as to the best of my knowledge of the language. As anyone will be aware, Chinese is the makeup of a sequence of pictorial words, from what I understand this has limited spacing apart from when it includes anglicized words and punctuation.

To handle this different view of the words, the input text ( that entered by a user ), then pattern text ( that between the `<pattern>` tags ) and the template text ( that between then `<template>` tags ) needed to be split and merged differently

* Input text needs to be split at each Chinese symbol word boundary so that 你也好 becomes 你 也 好
* Pattern text, again needs to be split along the same lines to be matched with input text
* Template text needs to be merged so that 你 也 好 becomes 你也好

With all of the above, the combination of English and Chinese needs to be handled correctly.

As such new features have been added to the platform which will be released in 1.9. Watch this space for more details

# WARNING
Unfortunately, I do not speak any dialect of Chinese and therefore this work is based on the awesome feedback and input from Program-Y users. Please feel free to continue to feedback and help improve multi-language support. If I have missed anything or got anything majorly wrong, firstly I apologise if it offends your native tongue, and secondly please let me know what rule has been broken and I'll fix as soon as I can 



