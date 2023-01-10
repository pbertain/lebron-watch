#!/bin/bash

NBA_PATH="/Users/paulb/Dropbox/home/tech/nba/lebron-watch"
NBA_DATE=`date '+%a %m-%d'`
NBA_TIME=`date '+%l:%M%p'`
NBA_PYTHON="/usr/bin/python3"
NBA_SCRIPT="${NBA_PATH}/main.py"
DATE_CHECK="${NBA_PATH}/date-validate.py"
NBA_DATA=`${NBA_PYTHON} ${NBA_SCRIPT}`
LAKERS_GAME_CHECK=`${NBA_PYTHON} ${DATE_CHECK}`

if [ "${DATE_CHECK}" = "TRUE" ]
then
    /Users/paulb/bin/imessage.sh -t GROUP -r "NBA Stats" -m "${NBA_DATE}@${NBA_TIME}: All-time scoring update is ${NBA_DATA}"
else
    echo "Lakers day off"
fi
