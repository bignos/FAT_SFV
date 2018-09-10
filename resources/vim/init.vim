" Inspired by: https://realpython.com/vim-and-python-a-match-made-in-heaven/

set hlsearch
hi Search ctermbg=LightYellow
hi Search ctermfg=Red

hi MatchParen cterm=bold ctermbg=DarkRed ctermfg=magenta
hi Visual ctermfg=LightRed ctermbg=DarkRed

" Enable folding
set foldmethod=indent
set foldlevel=99

" Enable folding with the spacebar
nnoremap <space> za

call plug#begin()
Plug 'tmhedberg/SimpylFold'
Plug 'roxma/nvim-completion-manager'
" Plug 'SirVer/ultisnips'
" Plug 'honza/vim-snippets'
Plug 'neomake/neomake'
call plug#end()

" Specific plug-in configuration

" -[ neomake ]-
" When writing a buffer (no delay).
call neomake#configure#automake('w')
" When writing a buffer (no delay), and on normal mode changes (after 750ms).
call neomake#configure#automake('nw', 750)
" When reading a buffer (after 1s), and when writing (no delay).
call neomake#configure#automake('rw', 1000)
" Full config: when writing or reading a buffer, and on changes in insert and
" normal mode (after 1s; no delay when writing).
call neomake#configure#automake('nrwi', 500)

" -[ SimpylFold ]-
let g:SimpylFold_docstring_preview=1
