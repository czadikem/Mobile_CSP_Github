## Sentiment Analysis Configuration

These configuration items allow you to control how the Sentiment Analysis is processed. It is an optional set of settings, and leaving them blank means no sentiment analysis is carred

```yaml
        bot:
            sentiment:
                classname: programy.sentiment.textblob_sentiment.TextBlobSentimentAnalyser
                scores: programy.sentiment.scores.SentimentScores
```

* **classname** - The Python class that will carry out Sentiment Analysis
* **scores** - A Python class that is used to convert Sentiment Analysis scores to text values

For more information see [Sentiment Analysis](./Sentiment-Analysis)
