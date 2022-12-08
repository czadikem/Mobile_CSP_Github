# Overview
By use News API to pull the latest headlines from a range of news sources, this extension can be used to implement functionality similar to Alexa Flash Breifings and provide a quick summary of the news of choice

# License Keys
For details of the News API see the API document [here](https://newsapi.org/docs/client-libraries/python)

Before you start you need to obtain a license key from the developer, [here](https://newsapi.org/register)

Once you have been provided with a license key, add it to the file license.keys in in the config folder of your bot. 
```ini
NEWSAPI_API_KEY = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Core Grammars
* `ABC NEWS`
* `AL JAZEERA NEWS`
* `ARS TECHNICA NEWS`
* `ASSOCIATED PRESS NEWS`
* `BBC NEWS`
* `BBC SPORT NEWS`
* `BLOOMBERG NEWS`
* `BUSINESS INSIDER NEWS`
* `BUSINESS INSIDER UK NEWS`
* `BUZZFEED NEWS`
* `CNBC NEWS`
* `CNN NEWS`
* `DAILY MAIL NEWS`
* `ENGADGET NEWS`
* `ENTERTAINMENT WEEKLY NEWS`
* `ESPN NEWS`
* `ESPN CRIC INFO NEWS`
* `FINANCIAL TIMES NEWS`
* `FOOTBALL ITALIA NEWS`
* `FORTUNE NEWS`
* `FOUR FOUR TWO NEWS`
* `FOX SPORTS NEWS`
* `GOOGLE NEWS`
* `HACKER NEWS`
* `IGN NEWS`
* `INDEPENDENT NEWS`
* `MASHABLE NEWS`
* `METRO NEWS`
* `MIRROR NEWS`
* `MTV NEWS`
* `MTV UK NEWS`
* `NATIONAL GEOGRAPHIC NEWS`
* `NEW SCIENTIST NEWS`
* `NEWSWEEK NEWS`
* `NEW YORK MAGAZINE NEWS`
* `NFL NEWS`
* `POLYGON NEWS`
* `RECODE NEWS`
* `REDDIT NEWS`
* `REUTERS NEWS`
* `TALKSPORT NEWS`
* `TECHCRUNCH NEWS`
* `TECHRADAR NEWS`
* `THE ECONOMIST NEWS`
* `THE GUARDIAN AU NEWS`
* `THE GUARDIAN UK NEWS`
* `THE HUFFINGTON POST NEWS`
* `THE NEW YORK TIMES NEWS`
* `THE NEXT WEB NEWS`
* `THE SPORT BIBLE NEWS`
* `THE TELEGRAPH NEWS`
* `THE VERGE NEWS`
* `THE WALL STREET JOURNAL NEWS`
* `THE WASHINGTON POST NEWS`
* `TIME NEWS`
* `USA TODAY NEWS`
* `BUSINESS NEWS` - Pulls together all business related news feeds
* `ENTERTAINMENT NEWS` - Collects all entertainment feeds from the sources above
* `GAMING NEWS` - All gaming news from the above feeds
* `MUSIC NEWS` - Use the above feeds to pull together single music related feeds
* `SCIENCE AND NATURE NEWS` - All since and nature feeds from above
* `SPORT NEWS` - Comprehensive news feeds from a variety of links above
* `TECHNOLOGY NEWS` - Full set of technology feeds from above
* `UK NEWS` - All UK news from sources available above
* `UK NEWSPAPERS NEWS` - All UK news from UK news papers with links above
