set nocompatible
filetype off

set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" general
Plugin 'gmarik/vundle'
Plugin 'kien/ctrlp.vim'
Plugin 'bitc/vim-bad-whitespace'
Plugin 'ciaranm/detectindent'
Plugin 'editorconfig/editorconfig-vim'
Plugin 'scrooloose/nerdcommenter'
Plugin 'scrooloose/nerdtree'
Plugin 'scrooloose/syntastic'
Plugin 'majutsushi/tagbar'
Plugin 'troydm/easybuffer.vim'
Plugin 'jnurmine/Zenburn'
Plugin 'mileszs/ack.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'mattn/emmet-vim'
Plugin 'Gundo'
Plugin 'tpope/vim-fugitive'
Plugin 'tpope/vim-abolish'
Plugin 'tpope/vim-surround'

" lang specific
Plugin 'pangloss/vim-javascript'
Plugin 'Valloric/YouCompleteMe'
" snippets for YouCompleteMe
" Plugin "SirVer/ultisnips"
" Plugin 'marijnh/tern_for_vim'

Plugin 'tpope/vim-markdown'
" Plugin 'psykidellic/vim-jekyll'
" Plugin 'tpope/vim-liquid'

" Plugin 'digitaltoad/vim-jade'

" Plugin 'guns/vim-clojure-static'

Plugin 'jhradilek/vim-rng'

filetype plugin indent on
