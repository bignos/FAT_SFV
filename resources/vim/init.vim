" Inspired by: https://realpython.com/vim-and-python-a-match-made-in-heaven/

" -[ Plugins ]-

call plug#begin()

" Plug 'python-mode/python-mode'		" Python IDE mode for Vim
					" Use 'git clone --recursive https://github.com/python-mode/python-mode'
					" for the first installation

Plug 'tmhedberg/SimpylFold'		" folding

Plug 'ncm2/ncm2'			" Completion
Plug 'roxma/nvim-yarp'		" remote plugin framework

" Plug 'ncm2/ncm2-bufword'		" Word completion
" Plug 'ncm2/ncm2-tmux'			" Tmux completion
Plug 'ncm2/ncm2-path'			" System path completion
Plug 'ncm2/ncm2-jedi'			" Python completion

Plug 'davidhalter/jedi-vim'		" Python code navigation
Plug 'jeetsukumaran/vim-pythonsense'	" Python class and function navigation

" Plug 'SirVer/ultisnips'		" Snippets engine
" Plug 'honza/vim-snippets'		" Snippets
" Plug 'vim-syntastic/syntastic'		" Visual synthax checker
" Plug 'neomake/neomake'			" Visual synthax checker
" Plug 'nvie/vim-flake8'			" Synthax checker for Python
" Plug 'tell-k/vim-autopep8'		" Autofix Style for Python

Plug 'scrooloose/nerdtree'		" File viewer
Plug 'ctrlpvim/ctrlp.vim'		" Filename searcher
Plug 'mileszs/ack.vim'			" Files content searcher

Plug 'Raimondi/delimitMate'		" Auto completion for delimiter

" Plug 'lepture/vim-jinja'		" Jinja syntax support ( HTML templating )
Plug 'vim-airline/vim-airline'		" Enhanced status bar
Plug 'godlygeek/tabular'		" Easy tabular indentation

call plug#end()

" -[ Plugins specific configuration ]-

" { Python-mode }
" let g:pymode_folding 			= 0
" let g:pymode_options_max_line_length 	= 119	" Because 80 is too small
" let g:pymode_options_colorcolumn 	= 1	" No display of line size limit


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
			\ set expandtab 	| 
			\ set autoindent 	|
			\ set nonumber		|
			\ set fileformat=unix

au BufNewFile,BufRead *.js, *.html, *.css 
			\ set tabstop=2 	| 
			\ set softtabstop=2 	| 
			\ set shiftwidth=2

" -[ Key biding ]-

" Use <TAB> to select the popup menu:
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

" Activate ncm2 completion
imap <C-Space> <Plug>(ncm2_manual_trigger)

" Enable folding with the spacebar
nnoremap <space> za

" Enable NERDTree with alt+e
map <M-e> :NERDTreeToggle<CR>

" Enable Autopep
" autocmd FileType python noremap <buffer> <F8> :call Autopep8()<CR>

" Enable PymodeLint
" map <F7> :PymodeLint<CR>

" Enable PymodeLintAuto ( Auto-Fix )
" map <F8> :PymodeLintAuto<CR>

" -[ Final ]-
