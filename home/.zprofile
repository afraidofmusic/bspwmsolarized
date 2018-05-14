## Path
export PATH=$PATH:${HOME}/.local/bin
## Environment Variables
export QT_QPA_PLATFORMTHEME=qt5ct
## Gtk3-NoCSD
export GTK_CSD=0
## Start X at login
if [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
    exec startx
fi
## Tmux
if [[ -z "$TMUX" ]] ;then
    ID="$( tmux ls | grep -vm1 attached | cut -d: -f1 )" # get the id of a deattached session
    if [[ -z "$ID" ]] ;then # if not available create a new one
        tmux new-session
    else
        tmux attach-session -t "$ID" # if available attach to it
    fi
fi
