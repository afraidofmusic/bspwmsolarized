""" Vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'altercation/vim-colors-solarized'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'python-mode/python-mode'
Plugin 'scrooloose/nerdtree'
call vundle#end()
filetype plugin indent on
""" Airline
let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
""" Nerdtree
map <C-n> :NERDTreeToggle<CR>
""" Solarized
syntax enable
set background=light
colorscheme solarized
""" Pymode
let g:pymode_python = 'python3'
""" Buffer Switching
nnoremap <C-b> <CR>:b<Space>
""" Tweaks
set number
