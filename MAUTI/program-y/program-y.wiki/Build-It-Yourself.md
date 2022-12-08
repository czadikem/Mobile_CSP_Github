So you want develop on Program-Y yourself, that's the beauty of Python, you can start right away. No complicated build scripts, not compile, wait, run, wait, test, wait, fix wait cycles. Get interactive with the go straight away.

The code is covered well with unit tests, approx 82% at the moment and growing. IN this page, I'll show you the pull, code, test, commit cycle that will get you up and running in no time

## Integration Tests
```
Alice2
	Linux
		alice2.sh

Professor
	Linux
		processfor.sh

Rosie
	Linux
		rosie.sh

Y-Bot
	Linux
		y-bot.sh
		y-bot_tests.sh	
		y-bot-rest.sh
			curl 'http://localhost:5000/api/rest/v1.0/ask?question=hello+world&userid=1234567890'
		y-bot-twitter.sh
		y-bot-webchat.sh
			http://localhost:5000
		y-bot-xmpp.sh
	Windows
		y-bot.cmd

	Services To Test
		Pandora
		Pannous
		Wikipedia

	Extensions To Test
		Weather
		NewsAPI
		Banking
		Energy
		Telecoms
		Survey
		Maps
		Geocode
```