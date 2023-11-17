#!/bin/bash

NBA_PATH="/Users/paulb/Dropbox/home/tech/nba/dame-watch"
NBA_DATE=`date '+%a %m-%d'`
NBA_TIME=`date '+%l:%M%p'`
#echo "${NBA_DATE} - ${NBA_TIME}"
NBA_PYTHON="/usr/bin/python3"
NBA_SCRIPT="${NBA_PATH}/main.py"
DATE_CHECK=`${NBA_PYTHON} ${NBA_PATH}/date_validate.py`
NBA_DATA=`${NBA_PYTHON} ${NBA_SCRIPT}`
BLAZERS_GAME_CHECK="${DATE_CHECK}"
TODAYS_PLAYER_PTS=`${NBA_PYTHON} ${NBA_PATH}/get_tonights_player_points.py`
TODAYS_GAME_RESULT=`${NBA_PYTHON} ${NBA_PATH}/gsw_todays_game_score.py`
iMESSAGE="${NBA_PATH}/imessage.sh"
MESSAGE="${NBA_DATE}@${NBA_TIME}: ${TODAYS_GAME_RESULT} and ${TODAYS_PLAYER_PTS}"

if [ "${BLAZERS_GAME_CHECK}" = "TRUE" ]
then
#    ${iMESSAGE} -t GROUP -r "NBA Stats" -m "${MESSAGE}"
#    ${iMESSAGE} -t GROUP -r "NBA Watch" -m "${MESSAGE}"
    ${iMESSAGE} -t DIRECT -r "pbertain@mac.com" -m "${MESSAGE}"
else
    echo "Rip City had the day off"
fi

