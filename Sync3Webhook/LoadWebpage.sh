#!/bin/bash

sleep 300

firefox --new-window "https://menu-board.novolabs.com/menu-board/ticket-items?lid=12976160&chid=16&lpn=19514099150" & 

sleep 60

id=`xdotool search --name "Insight Verify"`
xdotool windowmap $id
xdotool windowactivate $id key F11

sleep 60

id=`xdotool search --name "Menu Board"`
xdotool windowmap $id
xdotool windowactivate $id key F11
