## Aliases
alias vi='nvim'
alias ls='ls --color'
alias emacs='emacs -nw'
alias neofetch='neofetch --ascii_colors 2 7 --colors 2 7 7 2'
## Prompt
PROMPT='%B%F{red}%~%F{white} λ %b%f'
RPROMPT='%B[%F{blue}%w%f]-[%F{yellow}%T%f]%b'
## Zsh Installer
zstyle ':completion:*' completer _expand _complete _ignored _correct _approximate
zstyle ':completion:*' max-errors 100 not-numeric
zstyle :compinstall filename '/home/can/.zshrc'
autoload -Uz compinit
compinit
HISTFILE=~/.zsh_history
HISTSIZE=1000
SAVEHIST=1000
## Zsh Syntax Highlighting
source ${HOME}/.zsh.d/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh
## Zsh Titleso
source ${HOME}/.zsh.d/zsh-titles/titles.plugin.zsh
