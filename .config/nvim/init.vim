filetype plugin on
filetype indent on

set number
set expandtab
set autoindent
set shiftwidth=4
set tabstop=4

call plug#begin()
    " Plugins here
call plug#end()

set guicursor=i:block-Cursor

" Indent/dedent
nnoremap <A-j> :m .+1<CR>
nnoremap <A-k> :m .-2<CR>
nnoremap <A-h> <<
nnoremap <A-l> >>

inoremap <A-j> <Esc>:m .+1<CR>gi
inoremap <A-k> <Esc>:m .-2<CR>gi
inoremap <A-h> <C-d>
inoremap <A-l> <C-t>

vnoremap <A-j> :m '>+1<CR>gv
vnoremap <A-k> :m '<-2<CR>gv
vnoremap <A-h> <gv
vnoremap <A-l> >gv
