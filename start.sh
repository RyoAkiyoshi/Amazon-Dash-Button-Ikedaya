#!/bin/bash
if pgrep -f twitter-dash.py > /dev/null
then
    echo "twitter-dash.py is already running!"
else
    echo "start twitter-dash.py"
    ./twitter-dash.py
fi
