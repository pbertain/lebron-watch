#!/bin/bash

PLAYER=$1

JUNK=`/opt/homebrew/bin/python3 ./player-watch.py "LeBron James" "today"`
iMESSAGE_SCRIPT="./imessage.sh"
iMESSAGE_TARGET="pbertain@mac.com"
MESSAGE="${JUNK}"
#NBA_DATA=`${NBA_PYTHON} ${NBA_SCRIPT} "LeBron James" ${NBA_DATE}`
NBA_DATE="today"
NBA_PATH="/Users/paulb/Dropbox/home/tech/nba/player-watch"
NBA_PYTHON="/opt/homebrew/bin/python3"
NBA_SCRIPT="${NBA_PATH}/player-stats.py"

if [ "${NBA_DATA}" = "false" ]
then
    logger "No games for LBJ today"
else
    ${iMESSAGE_SCRIPT} -t DIRECT -r ${iMESSAGE_TARGET} -m "${MESSAGE}"
fi

