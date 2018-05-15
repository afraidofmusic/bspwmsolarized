## Zsh Completions
source ${HOME}/.zsh.d/zsh-completions/zsh-completions.plugin.zsh
## Aliases
alias ls='ls --color'
#alias neofetch='neofetch --ascii_colors 2 7 --colors 2 7 7 2'
alias scale1366='xrandr --output eDP1 --scale-from 1366x768 --panning 1366x768'
alias scale1080='xrandr --output eDP1 --scale-from 1920x1080 --panning 1920x1080'
## Prompt
PROMPT='%B%F{red} %~%f λ %b'
## Command Completion
autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
## History
autoload -Uz up-line-or-beginning-search down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

[[ -n "$key[Up]"   ]] && bindkey -- "$key[Up]"   up-line-or-beginning-search
[[ -n "$key[Down]" ]] && bindkey -- "$key[Down]" down-line-or-beginning-search
# TMUX
if which tmux >/dev/null 2>&1; then
    test -z "$TMUX" && (tmux attach || tmux new)
fi
