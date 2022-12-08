Test Runner is a utility client that allows you to run multiple tests against a fully loaded grammar without having to get into a complex Q&A session

There is one additional command line parameter

    --testdir <location of test files>

The directory specified along with all subdirectories are searched for files ended in ".tests"

## Tests
The format of each test file is as follows

    "QUESTION", "ANSWER1" [,"ANSWER2", .. "ANSWERN"]

An example being

    "LAST NAME", "MY LAST NAME IS BOT."
    "MIDDLE NAME", "MY MIDDLE NAME IS AIML."
    "FIRST NAME", "MY FIRST NAME IS Y."
    "FULL NAME",  "MY FULL NAME IS Y-BOT"

Each value to be tested can be any complete regular expression e.g

    "LAST NAME", "MY LAST NAME IS .*"      <--- When you don't care what the name is

This is useful when you return a huge amount of text, and are confident that if the first sentence is unique enough to pass your test

    "WHAT IS A CHAT ROBOT", "A chat robot is a program that attempts to simulate the conversation or "chat" of a human being. The.*"

## Running the Tests
To execute the test runner, an example script exists within Y-Bot folder

    #! /bin/sh
    clear
    export PYTHONPATH=../../src:../../libs/MetOffer-1.3.2:.
    python3 ../../src/programy/clients/test_runner.py --test_dir ./tests --config ./config.yaml --cformat yaml --logging ./logging.yaml

### Test Output
When you run the tests you'll see something like the following

    Loading, please wait...
    No bot root argument set, defaulting to [/Projects/AIML/program-y/bots/y-bot]
    Loading Tests from directory [/Projects/AIML/program-y/bots/y-bot/tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/aimlstandardlibrary.tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/bot_profile.tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/client_profile.tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/config.tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/datetime_convo.tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/datetime_core.tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/pand_system.tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/system.tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/utilities.tests]
    Loading tests from file [/Projects/AIML/program-y/bots/y-bot/tests/core/xfind.tests]
    Successes: 172
    Failures:  3
	    UTILITIES: [SUBSTRING 1 3] expected [TESTSTRING], got [Sorry, I don't have an answer for that!]
	    UTILITIES: [SUBSTRINGEXPLODE 1 3] expected [TESTSTRING], got [Sorry, I don't have an answer for that!]
	    UTILITIES: [NORMALIZE TEST.ORG] expected [test.org], got [. Sorry, I don't have an answer for that!]
    Total processing time 13.836841.2 secs
    That's approx 13.008750 tests per sec

As you can see the test runner searched for tests in all fodlers below /tests folder, and rand a total of 172 of which 3 failed, for which it displays what it expected and what it got