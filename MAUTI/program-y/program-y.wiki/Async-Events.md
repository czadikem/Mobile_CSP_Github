# Scheduling Asynchronous Events

Program-Y now ships with an very powerful scheduler which allows you to scheduler events either as one time only or regularly repeating events, seconds, minutes, hours, days and even weeks in the future.

Y-Bot ships with a basic grammar to control the scheduler. This can be found in aiml/extensions/scheduler/scheduler.aiml

The core grammars contained in this file are

## Scheduler

SCHEDULE IN|EVERY X SECONDS|MINUTES|HOURS|DAYS|WEEKS TEXT|SRAI <some text>

This allows you to set up a single one time only event using 'IN' or an infinitely repeating event using 'EVERY'
You have the option to set the period to one of the following

* SECONDS
* MINUTES
* HOURS
* DAYS
* WEEKS

You can also control what text is returned, eith either
* TEXT - Returns exactly the text provided in the command
* SRAI - First passes the text provided through the bot, as if it was a question and returns the parsed result

Examples

* SCHEDULE IN 1 HOUR TEXT Check the oven
* SCHEDULE EVERY 30 MINUTES TEXT Stand up
* SCHEDULE EVERY 24 HOURS SRAI WAKE WAKEY

Note in the 3rd example, if the pattern WAKEY WAKEY does not exist then the question will be processed by the UDC handler

## Scheduler Job Control

There are a number of commands that allow the user to see their own jobs they have created, and to pause, resume and stop them. 

### List Jobs
The first command to use is SCHEDULER LIST, which provides an ordered list of the jobs

SCHEDULER LIST
1. 7296636ea2b16e5c10955675d43d496b
2. 87463636ea2b16e5c10955675d43d496b

The index, 1, 2, etc can then be used in the following commands

### Pausing Jobs
You can pause both a single specfic job or all jobs with the SCHEDULER PAUSE ALL or SCHEDULE PAUSE <JOB NUMBER> commands

### Pausing Jobs
You can resume both a single specfic job or all jobs with the SCHEDULER RESUME ALL or SCHEDULE RESUME <JOB NUMBER> commands

### Stopping Jobs
You can stop both a single specfic job or all jobs with the SCHEDULER STOP ALL or SCHEDULE STOP <JOB NUMBER> commands. After this command the job is permanently removed from the scheduler and is no longer available to the user

## Extending the Scheduler

You can extending the scheduler by either creating your own extension or modifying the existing extension. 

The scheduler control class can be found in src/scheduling/scheduler.py
The scehduler extension class can be found in src/extensions/scheduler/scheduler.py
The scheduler uses the amazing Python library APScheduler, which can be found at 


