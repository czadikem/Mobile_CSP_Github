# Pattern Matching

The AIML 1.0 wildcards * and _ are defined so that they match one or more words.   AIML 2.0 introductes two new wildcards, ^ and #, defined to match zero or more words.  As a shorthand description, we refer to these as “zero+ wildcards”.

Both ^ and # are defined to match 0 or more words.   The difference between them is the same as the difference between * and _.   The # matching operator has highest priority in matching, followed by _, followed by an exact word match, followed by ^, and finally * has the lowest matching priority.
When defining a zero+ wildcard it is necessary to consider what the value of <star/> (as well as <thatstar/> and <topicstar/>) should be when the wildcard match has zero length.   In AIML 2.0 we leave this up to the botmaster.  Each bot can have a global property named nullstar which the botmaster can set to “”, “unknown”, or any other value.

## Matching Order
* `Priority Word`
* `#`   ( Zero or more )
* `_`   ( One or more )
* `word`
* `^`   ( Zero or more )
* `*`   ( One or more )
 