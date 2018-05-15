#!/bin/bash
xrdb ~/.Xresources
export LC_ALL="en_US.UTF-8"

compton -b &
dunst &
feh --bg-fill ${HOME}/.startup/rose-erkul.jpg &
polybar can &
redshift &
xsetroot -cursor_name left_ptr &
exec bspwm
