#!/bin/bash
xrdb ~/.Xresources
export LC_ALL="en_US.UTF-8"

dunst &
. ${HOME}/.fehbg &
polybar can &
redshift &
xcompmgr &
xsetroot -cursor_name left_ptr &
exec bspwm
