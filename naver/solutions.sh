#!/usr/bin/env bash

DB_FILE_PATH="./users.txt"
COMMAND="$1"
PARAMETER1="$2"
PARAMETER2="$3"
PARAMETER3="$4"


if [ $COMMAND = "help" ];
then
    echo "(c) Your Name";

elif [ $COMMAND = "list" ];
then
    cat "$DB_FILE_PATH";

elif [ $COMMAND = "add" ] && [ -n $PARAMETER1 ] && [ -n $PARAMETER2 ];
then
    echo -e  "$PARAMETER1\t$PARAMETER2">> "$DB_FILE_PATH";

elif [ $COMMAND = "remove" ] && [ -n $PARAMETER1 ];
then
    sed -i "/$PARAMETER1/d" $DB_FILE_PATH;

elif [ $COMMAND = "search" ] && [ -n $PARAMETER1 ];
then
    grep "$PARAMETER1" "$DB_FILE_PATH";

else
    echo "Usage: solution.sh [add|help|list|search|remove]";
  exit 1;
fi