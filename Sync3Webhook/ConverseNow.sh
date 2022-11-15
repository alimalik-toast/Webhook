#!/bin/bash

export DISPLAY=":0"
export XAUTHORITY=/home/username/.Xauthority

sleep 300

firefox --new-window "https://ocb.staging.v2.conversenow.ai/pandalabint/pd-119476" & 
