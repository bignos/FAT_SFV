" Inspired by: https://realpython.com/vim-and-python-a-match-made-in-heaven/

" -[ Plugins ]-

call plug#begin()

Plug 'tmhedberg/SimpylFold'		" folding
Plug 'python-mode/python-mode'		" Python IDE mode for Vim
Plug 'ncm2/ncm2'			" Completion
Plug 'roxma/nvim-yarp'			" remote plugin framework

Plug 'ncm2/ncm2-bufword'		" Word completion
" Plug 'ncm2/ncm2-tmux'			" Tmux completion
Plug 'ncm2/ncm2-path'			" System path completion
" Plug 'ncm2/ncm2-jedi'			" Python completion
" Plug 'SirVer/ultisnips'		" Snippets engine
" Plug 'honza/vim-snippets'		" Snippets
" Plug 'vim-syntastic/syntastic'		" Visual synthax checker
" Plug 'neomake/neomake'			" Visual synthax checker
" Plug 'nvie/vim-flake8'			" Synthax checker for Python

Plug 'scrooloose/nerdtree'		" File viewer
Plug 'ctrlpvim/ctrlp.vim'		" Filename searcher
Plug 'mileszs/ack.vim'			" Files content searcher

Plug 'Raimondi/delimitMate'		" Auto completion for delimiter 

call plug#end()

" -[ Plugins specific configuration ]-

" { SimpylFold }
let g:SimpylFold_docstring_preview=1

" { ncm2 }
" enable ncm2 for all buffers
autocmd BufEnter * call ncm2#enable_for_buffer()

" IMPORTANTE: :help Ncm2PopupOpen for more information
set completeopt=noinsert,menuone,noselect

" { neomake }
" When writing a buffer (no delay).
" call neomake#configure#automake('w')
" When writing a buffer (no delay), and on normal mode changes (after 750ms).
" call neomake#configure#automake('nw', 750)
" When reading a buffer (after 1s), and when writing (no delay).
" call neomake#configure#automake('rw', 1000)
" Full config: when writing or reading a buffer, and on changes in insert and
" normal mode (after 1s; no delay when writing).
" call neomake#configure#automake('nrwi', 500)

" { NERDTree }
" autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" { python-mode }
let g:pymode_python = 'python3'

" -[ Neovim configuration ]-

" UTF-8 support
set encoding=utf-8

" Colors
set hlsearch
hi Search ctermbg=LightYellow
hi Search ctermfg=Red

hi MatchParen cterm=bold ctermbg=DarkRed ctermfg=magenta
hi Visual ctermfg=LightRed ctermbg=DarkRed

" Python colors highlight
let python_highlight_all=1
syntax on

" Enable folding
set foldmethod=indent
set foldlevel=99

" PEP 8 indentation
au BufNewFile,BufRead *.py 
			\ set tabstop=4 	| 
			\ set softtabstop=4 	| 
			\ set shiftwidth=4 	| 
			\ set textwidth=79 	| 
			\ set expandtab 	| 
			\ set autoindent 	| 
			\ set fileformat=unix

au BufNewFile,BufRead *.js, *.html, *.css 
			\ set tabstop=2 	| 
			\ set softtabstop=2 	| 
			\ set shiftwidth=2

" -[ Key biding ]-

" Use <TAB> to select the popup menu:
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

" Enable folding with the spacebar
nnoremap <space> za

" Enable NERDTree with alt+e
map <M-e> :NERDTreeToggle<CR>



