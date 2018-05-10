#!/bin/bash
xrdb ~/.Xresources

feh --bg-tile ${HOME}/.startup/solarized.png &
mpv ${HOME}/.startup/xp.mp3 &
polybar can &
setxkbmap tr &
unclutter &
wmname LG3D &
xsetroot -cursor_name left_ptr &
sxhkd &
exec bspwm
