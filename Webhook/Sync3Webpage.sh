#!/bin/bash

export DISPLAY=":0"
export XAUTHORITY=/home/username/.Xauthority

sleep 300

firefox --new-window "https://menu-board.novolabs.com/menu-board/ticket-items?&lid=12975818&chid=16" & 

sleep 60

#xdotool search --sync --name "Menu Board" key F11
id=`xdotool search --name "Menu Board"`
xdotool windowmap $id
xdotool windowactivate $id key F11

sleep 30

#xdotool search --sync --name "Insight Verify" key F11
id2=`xdotool search --name "Insight Verify"`
xdotool windowmap $id2
xdotool windowactivate $id2 key F11

