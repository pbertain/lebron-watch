#!/bin/bash

NBA_DATE=`date '+%a %m-%d'`
NBA_TIME=`date '+%l:%M%p'`
NBA_PYTHON="/usr/bin/python3"
NBA_SCRIPT="/Users/paulb/Documents/version-control/git/lebron-watch/main.py"
DATE_CHECK="/Users/paulb/Documents/version-control/git/lebron-watch/date-check.py"
NBA_DATA=`${NBA_PYTHON} ${NBA_SCRIPT}`
LAKERS_GAME_CHECK=`${NBA_PYTHON} ${DATE_CHECK}`

/Users/paulb/bin/imessage.sh -t GROUP -r "NBA Stats" -m "It is ${NBA_DATE} @${NBA_TIME} and ${LAKERS_GAME_CHECK} The all-time scoring update is that ${NBA_DATA}"

