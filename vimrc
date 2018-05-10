"" Vundle ""
set nocompatible              " be iMproved, required
filetype off                  " required
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'" required
Plugin 'altercation/vim-colors-solarized'
Plugin 'hsitz/VimOrganizer'
Plugin 'junegunn/goyo.vim'
Plugin 'junegunn/limelight.vim'
Plugin 'python-mode/python-mode'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
call vundle#end()            " required
filetype plugin indent on    " required
"" Vundle ""

"" Split Navigations ""
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
"" Split Navigations ""

"" Solarized ""
syntax on
set background=dark
colorscheme solarized
"" Solarized ""

"" Tweaks
set number
set laststatus=2
""
