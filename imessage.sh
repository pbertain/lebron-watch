#!/bin/bash

ARGS=$#
TYPE=`echo ${2} | tr '[:upper:]' '[:lower:]'`

usage()
{
  printf "\nUsage: $0 [ -t (GROUP | DIRECT) ] [ -m 'Message to send' ] [ -r (Direct: phone or iCloud account\nGroup: chat name) ]\n\n"
  exit 2
}

type_usage()
{
  printf "\n\nOnly 'DIRECT' or 'GROUP' are allowed keywords.\n\n\n"
  exit 3
}

group_send()
{
  RECIPIENT=${1}
  MESSAGE=${2}
  cat<<EOF | osascript - "${RECIPIENT}" "${MESSAGE}"
  on run {targetBuddyAcct, targetMessage}
      tell application "Messages"
          send targetMessage to chat targetBuddyAcct
      end tell
  end run
EOF
}

direct_send()
{
  RECIPIENT=${1}
  MESSAGE=${2}
  cat<<EOF | osascript - "${RECIPIENT}" "${MESSAGE}"
  on run {targetBuddyAcct, targetMessage}
      tell application "Messages"
          set targetBuddy to buddy targetBuddyAcct
          send targetMessage to targetBuddy
      end tell
  end run
EOF
}

if [ ${ARGS} -ne 6 ]
then
    printf "\nYou provided ${ARGS} arguments. Please provide exactly 6.\n"
    usage
fi

if [ ${1} != "-t" ]
then
    printf "\n-t: \"${1}\" - broken syntax\n\n"
    usage
fi

if [ "${TYPE}" != "direct" ] && [ "${TYPE}" != "group" ]
then
    printf "\nType of message: \"${TYPE}\" - broken syntax\n\n"
    usage
fi

if [ ${3} != "-r" ]
then
    printf "\n-r: \"${3}\" - broken syntax\n\n"
    usage
fi

#if [ -n $4 ]
#then
#    printf "\nRecipient: \"${4}\" - broken syntax\n\n"
#    usage
#fi

if [ ${5} != "-m" ]
then
    printf "\n-m: \"${5}\" - broken syntax\n\n"
    usage
fi

#if [ -n $6 ]
#then
#    printf "\nMessage contents: \"${6}\" - broken syntax\n\n"
#    usage
#fi

case ${TYPE} in
    "direct")
        direct_send "${4}" "${6}" ;;
    "group")
        group_send "${4}" "${6}" ;;
    *)
        type_usage ;;
esac

#echo "you have successfully completed this program"
