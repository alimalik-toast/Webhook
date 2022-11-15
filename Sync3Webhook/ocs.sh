#!/bin/bash

export DISPLAY=":0"
export XAUTHORITY=/home/delphidisplay/.Xauthority

currentwindow=`xdotool getwindowfocus`

id=`xdotool search --name "Menu Board"`
# windowactivate %1
xdotool windowmap $id
xdotool windowactivate $id

