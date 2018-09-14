" Inspired by: https://realpython.com/vim-and-python-a-match-made-in-heaven/

" -[ Plugins ]-

call plug#begin()

Plug 'tmhedberg/SimpylFold'		" folding

Plug 'ncm2/ncm2'			" Completion
Plug 'roxma/nvim-yarp'			" remote plugin framework

Plug 'ncm2/ncm2-path'			" System path completion
Plug 'ncm2/ncm2-jedi'			" Python completion

Plug 'davidhalter/jedi-vim'		" Python code navigation
Plug 'jeetsukumaran/vim-pythonsense'	" Python class and function navigation

Plug 'nvie/vim-flake8'			" Synthax checker for Python

Plug 'scrooloose/nerdtree'		" File viewer
Plug 'ctrlpvim/ctrlp.vim'		" Filename searcher
Plug 'mileszs/ack.vim'			" Files content searcher

Plug 'Raimondi/delimitMate'		" Auto completion for delimiter

Plug 'vim-airline/vim-airline'		" Enhanced status bar
Plug 'godlygeek/tabular'		" Easy tabular indentation

call plug#end()

" -[ Plugins specific configuration ]-

" { SimpylFold }
let g:SimpylFold_docstring_preview	= 1

" { ncm2 }
" enable ncm2 for all buffers
autocmd BufEnter * call ncm2#enable_for_buffer()

" IMPORTANTE: :help Ncm2PopupOpen for more information
set completeopt=noinsert,menuone,noselect

let g:ncm2#auto_popup			= 0

" { jedi-vim }
let g:jedi#completions_enabled 		= 0
let g:jedi#show_call_signatures 	= 2

" { vim-flake8 }
let g:flake8_show_in_gutter		= 1
let g:flake8_show_in_file		= 1

" -[ Neovim configuration ]-

" UTF-8 support
set encoding=utf-8

" No mode show ( because of the status bar, this information is redondant )
set noshowmode

" Colors
set hlsearch
hi Search ctermbg=LightYellow
hi Search ctermfg=Red

hi MatchParen cterm=bold ctermbg=DarkRed ctermfg=magenta
hi Visual ctermfg=LightRed ctermbg=DarkRed

" Python colors highlight
" let python_highlight_all=1
" syntax on

" Enable folding
set foldmethod=indent
set foldlevel=99

" PEP 8 indentation
au BufNewFile,BufRead *.py 
			\ set tabstop=4 	| 
			\ set softtabstop=4 	| 
			\ set shiftwidth=4 	|  
			\ set expandtab 	| 
			\ set autoindent 	|
			\ set nonumber		|
			\ set fileformat=unix

au BufNewFile,BufRead *.js, *.html, *.css 
			\ set tabstop=2 	| 
			\ set softtabstop=2 	| 
			\ set shiftwidth=2

" -[ Key biding ]-

" Go to previous TAB
nmap <C-up> gT
imap <C-up> <Esc>gTi

" Go to next TAB
nmap <C-down> gt
imap <C-down> <Esc>gti

" Use <TAB> to select the popup menu:
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

" Activate ncm2 completion
imap <C-Space> <Plug>(ncm2_manual_trigger)

" Enable folding with the spacebar
nnoremap <space> za

" Enable NERDTree with alt+e
map <M-e> :NERDTreeToggle<CR>

" Exit of terminal insert mode
tnoremap <Esc> <C-\><C-n>

" -[ Final ]-
