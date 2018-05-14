#!/bin/bash
xrdb ~/.Xresources

dunst &
feh --bg-fill ${HOME}/.startup/rose-erkul.jpg &
polybar can &
redshift &
xsetroot -cursor_name left_ptr &
exec bspwm
