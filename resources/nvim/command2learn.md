Vim command to learn
====================

--------------------------------------------------------------------------------


### [Command-line]
~~~
vim -R {file}   Open {file} in read-only mode
vim -r {file}   Recorver {file} and recent edit after a crash
vim +{file}     Open {file} at last line
vim +{line} {file}
                Open {file} and place the cursor at {line}
vim +/{pattern} file
                Open {file} and place the cursor at first occurence of the search pattern
vim -c {command} {file}
                Open {file} and execute {command}
vim -d {file1} {file2}
                Diffting on file1 and file2
vim -D {file}   Start vim in debug mode
~~~

### [Vim standard command synthax]
~~~
[command][number]textobject
[number][command]textobject
~~~

### [Movement]
#### {character}
~~~
h, j, k, l      Left, Down, Up, Right
~~~

#### {text}
~~~
w, W, b, B      Forward, backward by word
e, E            End of word
(, )            Beginning of previous/next sentence
{, }            Beginning of previous/next paragraph
[[, ]]          Beginning of previous/next section
~~~

#### {Lines}
~~~
<Enter>         First nonblank character of next line
0,$,g_          First, end and end without '\n' of current line
^               First nonblank character of current line
+,-             First nonblank character of next/previous line
{n}|            Column {n} of current line
H,M,L           Top, Middle, Last line of screen
{n}H            {n} line after top line
{n}L            {n} line before last line
~~~

#### {Scrolling}
~~~
C-f,C-b         Scroll forward/backward one screen
C-d,C-u         Scroll down/up one half screen
C-e,C-y         Show one more line at bottom/top of window
z<CR>           Reposition line with cursor: to top of screen
z.              Reposition line with cursor: to middle of screen
z-              Reposition line with cursor: to bottom of screen
~~~

#### {Searches}
~~~
/{pattern}      Search forward for {pattern}
?{pattern}      Search backward for {pattern}
/{pattern}\c    Search forward for {pattern} case insensitive
?{pattern}\c    Search backward for {pattern} case insensitive
n,N             Repeat last search in same/opposite direction
/,?             Repeat previous search forward/backward
f{char}         Search forward for character {char} in current line
F{char}         Search backward for character {char} in current line
t{char}         Search forward to character before {char} in current line
T{char}         Search backward to character after {char} in current line
;               Repeat previous current-line search
,               Repeat previous current-line search in opposite direction
~~~

#### {Line number}
~~~
C-g             Display current line number
{n}G            Goto line {n}
G               Goto last line
:{n}            Goto line {n}
~~~

#### {Marking position}
~~~
m{char}         Mark current position as {char}
`{char}         Goto mark {char}
``              Return to previous mark or context
'{char}         Goto beginning of line containing mark {char}
''              Return to beginning of line containing previous mark
~~~


### [Editing]
#### {Insert}
~~~
i,a             Insert mode before/after cursor
I,A             Insert mode before beginning/after end of line
o,O             Insert new line below/above and active insert mode
~~~

#### {Change}
~~~
cw              Delete a word and active insert mode
cc              Delete current line and active insert mode
c{motion}       Delete character under motion and active insert mode
C               Delete to the end of the line and active insert mode
r               Change one character
R               Active Replace mode
s               Delete character and active insert mode
S               Delete current line and active insert mode
~~~

#### {Delete/Move}
~~~
x               Delete character under cursor
X               Delete character before cursor
dw              Delete a word
dd              Delete Current line
d{motion}       Delete text between the cursor and the target of {motion}
D               Delete to end of the line
p,P             Paste deleted text after/before cursor
"{register}p    Paste text from register {register}
~~~

#### {Copy}
~~~
yw              Copy word
yy              Copy current line
"{register}yy   Copy current line into register {register}
y{motion}       Copy text between the cursor and the target of {motion}
~~~

#### {Other commands}
~~~
.               Repeat last edit command
u,U             Undo last edit/Restore current line
J               Join two lines
~~~

#### {Ex edit commands}
~~~
:d              Delete lines
:m              Move lines
:co OR :t       Copy lines
~~~

#### {Exit commands}
~~~
:w              Write file
:w!             Write file [Force]
:wq             Write file and quit
:x              Write file and quit
ZZ              Write file and quit
:{range}w {file}
                Write line from {range} to {file}
:{range}w>> {file}
                Append line from {range} to {file}
Q               Ex mode
:e {file}       Edit {file}
:n              Edit next file
:e!             Return to last file saved state
%               Current filename
#               Alternate filename
~~~


### [Normal]
~~~
ZZ              Write current file, if modified, and exit.
gf              Edit the file whose name is under or after the cursor. Mnemonic: "goto file".
gd              Goto definition
gD              Goto Global definition
~~~

~~~
gg=G            Indent all buffer 
                    gg -> beginning of the buffer
                    =  -> indent until
                    G  -> end of the buffer
==              Indent the line under cursor
={txt_obj}      Indent text object(example: =i{ to indent inside a block)
={motion}       Indent motion(example: =% to indent under bracket)
~~~

~~~
V               Enter visual mode linewise
C-v             Enter visual mode for block selection
R               Replace mode
A               Place at the end of the line and enter Insert mode
~~~

~~~
f               Finds specified character to the right of the cursor position
F               Finds specified character to the left of the cursor position
;               Move to next occurrence of f/F
,               Move to previous occurrence of f/F
C-r             Redo
o               Begin a new line BELOW the cursor and insert text
s               Substitutes the character(or the selection of characters)
S               Substitutes the entire line
c               Change(not very well understand for the moment)
cc              Erase current line and set insert mode
cw              Erase word and set insert mode
D               Delete the characters under the cursor until the end of the line
~               Switch case of the character under the cursor and move the cursor to the right. 
                    If a [count] is given, do that many characters.
.               Repeats the last INSERT edit
gx              Opens the URL under the cursor in a web browser
~~~

~~~
q[a-z]          Start recording, everything will be recorded including movement actions
@[a-z]          Execute the recorded actions
~~~

~~~
w               Jump by start of words (punctuation considered words)
e               Jump to end of words (punctuation considered words)
b               Jump backward by words (punctuation considered words)
0               Start of line
^               First non-blank character of line
$               End of line(include newline)
g_              Goto end of the line(no newline include better for copy)
G               Bottom of file
gg              Top of file
%               Moves cursor to the next bracket(or parenthesis)
(               Moves cursor to the previous sentence
)               Moves cursor to the next sentence
{               Moves cursor to the previous paragraph
}               Moves cursor to the next paragraph
{n}G            Goto line {n}
~~~

~~~
]'              Next mark line position
['              Previous mark line position
]`              Next mark line and column position
[`              Previous mark line and column position
~~~

~~~
]c              Move to next diff change
[c              Move to previous diff change
~~~

~~~
'.              Jump back to last edited line
g;              Jump back to previous edited position
g,              Jump back to next edited position
%               Jump to the end of a block
C-]             Jump to definition (work only with ctags)
~~~

~~~
ma              Set mark a at current cursor location
'a              Jump to line of mark a (first non-blank character in line)
`a              Jump to line and column of mark a
g'a             Jump to line of mark a without affect the jumps list
g`a             Jump to line and column of mark a without affect the jump list
:marks          List all the current marks
:delm!          Clear all marks[a-z]
~~~

~~~
H               Jump to TOP of screen
M               Jump to MIDDLE of screen
L               Jump to BOTTOM of screen
C-l             Refresh screen
C-f             Move forward one full screen (page down)
C-b             Move back one full screen (page up)
C-d             Move forward 1/2 screen; half page down
C-u             Move back (up) 1/2 screen; half page up
C-e             Show one more line at bottom
C-y             Show one more line at top of window
~~~

~~~
z<CR>           Reposition line with cursor: to top of screen
z.              Reposition line with cursor: to middle of screen
z-              Reposition line with cursor: to bottom of screen
zt              Scroll the screen so the cursor is at the top
zb              Scroll the screen so the cursor is at the bottom
zz              Shifts page content so current line sits at the middle of the viewport
~~~

~~~
zf              Create a fold
zc              Close the fold
zo              Open the fold
za              Alternate the fold
zM              Close all folds
zR              Open all folds
~~~

~~~
/<pattern>      Search forward for pattern
?<pattern>      Search backward for pattern
C-g             Move to the next match in 'incsearch' mode [command-line]
C-T             Move to the previous match in 'incsearch' mode [command-line]
#               Searches backward for word under cursor
*               Searches forward for word under cursor
g#              Searches backward for line content word under cursor
g*              Searches forward for line content word under cursor
~~~

~~~
C-a             Increment number under cursor
C-x             Decrement number under cursor
~~~

~~~
g-              Move backward through history, including previous branches
g+              Move forward through history, including previous branches
~~~

~~~
C-o             Move to previous jump position
C-i             Move to next jump position
~~~

~~~
gn              Search and edit next
gN              Search and edit previous
~~~

~~~
Q               Ex Mode
~~~

~~~
J               Join lines, with a minimum of two lines(remove line break)
~~~

~~~
gq{Text Object}
                Reformat {Text Object}
gw{Text Object}
                Reformat {Text Object} without move the cursor
lgqG            Reformat all paragraph in a file
~~~


### [Insert/Replace]
~~~
C-o             Go to normal mode and return to insert mode after the first command
C-r<REG>        Get the <REG> register content
C-r=            Enter an expression register
~~~


### [Completion]
~~~
C-x{what}       Call completion for specific {what}
~~~

#### {what}
~~~
    C-f         Completion for filename
    C-l         Completion for whole line
    C-k         Completion with dictionary
                    Don't forget to set dictionary
                    :set dictionary+={dictionary_pat
    C-o         Omnicompletion(AKA personal user completion)
                    Don't forget to set omnifunc
                    :set omnifunc={Personal_completion_function}
~~~


### [Visual]
~~~
I               Insert
A               Append
~~~

~~~
o               Move the cursor to the opposite side
O               Move the cursor to the opposite side of the same line
~~~

~~~
"<REG>y         Copy selected region into register <REG> (Register [a-z])
"<REG>p         Paste selected region into register <REG>
c               Cut selection
gq              Reformat selection
gw              Same as gq but without moving cursor
~~~

~~~
i               Selected inside(use it with Text Object, ex: iw to select the word inside the cursor)
a               Selected around(use it with Text Object)
t               Selected until condition
                    example: va[t) if you want to select block begin by '[' until ')' is found
~~~


#### {Text Object} (using for selection)
~~~
w[ord]
s[entences]
p[aragraphs]
t[ags]
'|"|`[quotes]
{}|()|[]|<>[block]
~~~


### [Windows]
~~~
c-w s           Split window horizontally
c-w v           Split window vertically
c-w [H|J|K|L]   Move windows to Left|Down|Up|Right
~~~

~~~
c-w +           Increase the window height by one row
c-w -           Reduces the window height by one row
c-w >           Increase the window width by one column
c-w <           Reduces the window width by one column
~~~

~~~
c-w _           Enlarges current window height to full capacity
c-w |           Enlarges current window with to full capacity
c-w =           Resize all windows to balanced dimension (equal space)
~~~

~~~
c-w T           Move window to a Tab
~~~

~~~
:sp {file}      Create horizontal window split
:vp {file}      Create vertical window split
~~~


### [Tab]
~~~
:tabnew +{cmd}  Open a new tab and execute {cmd}
:tabonly        Closing all tab
:tabmove 1      Move tab to position 1 [fist tab is 0]
~~~


### [Command]
~~~
:wa             Saves all modified buffer
:x              Save and quit
:r[ead] [name]  Insert the file [name] below the cursor.
:r[ead] !{cmd}  Execute {cmd} and insert its standard output below the cursor.
~~~

~~~
:t              Copy
~~~

~~~
:!{cmd}         Execute {cmd} (Terminal command)
:'<,'>! {cmd}   Execute {cmd} on selected line
                    example: :'<,'>! tr '[:lower:]' '[:upper:]'
                    to transform selection to uppercase
:%! {cmd}       Execute {cmd} on the entire buffer
                    example: :%! column -t
                    to align all column
~~~

~~~
:m[ove]{line}   Move content to {line}
~~~

~~~
:bufdo          Apply same command to all buffer
:windo          Apply same command to all windows(visible buffer)
:tabdo          Apply same command to all tab
:argdo          Apply same command to all args(list of args :args)  
~~~

~~~
:args           Display all arguments
~~~

~~~
:wundo {file}   Save change 
:rundo {file}   Load change
~~~

~~~
:undolist       Show change branch list
:undo {n}       Return to state {n}
~~~

~~~
:changes        Show changes list
:changes {n}    Move cursor to the change number n
~~~

~~~
:earlier {when} Go to older buffer state. {when} can be COUNT, s, m, h, d, f
:later {when}   Go to newer buffer state
~~~

~~~
:jumps          Show jumps list
:keepjumps      Jump without recording jump in jump list (useful for plugins)
                    example: :keepjumps normal 5G
:clearjumps     Clear the jump list of the current window.
~~~

~~~
:g/{pattern}/{cmd}
                example :g/\v(a|g)/:d
                Erase all line begin by 'a' or 'g'
:%s/{pattern}/\={vimL}/
                example :%s/today/\=strftime("%c")/
                Replace all 'today' with the actual date
:%s/{pattern}/\=@{register}/
                example :%s/\v(today)/\=@x/
                Replace all 'today' with the content of register x
~~~

~~~
.               Current line
2,5             Range( line 2 to 5 )
~~~

~~~
:sba            Split all buffer in windows
:vert sba       Split vertically all buffer in windows
:bd             Close actual buffer
:bd *.php<c-a>  Close all buffer with filename *.php
:bd 3 5         Close buffer 3 and 5
:4,7 bd         Close buffer 4 to 7(range)
:bufdo bd       Close all buffer
~~~

~~~
:TOhtml         Convert file to HTML, also convert diff
~~~

~~~
:retab          Convert all tab(\t) to space
~~~

~~~
:map {key} {command}
                Map {key} to {command}
                    example:    :map j gg
                    When you press j you go on top of the buffer
:noremap {key} {command}
                No recursive mapping {key} to {command}
                    like map but without recurse
:nmap           Normal mode mapping
:imap           Insert mode mapping
:xmap           Visual mode mapping
:smap           Select mode mapping
:vmap           Visual and Select mode mapping
:cmap           Command-line mode mapping
:omap           Operator pending mode
~~~
_noremap version example vnoremap = Visual and Select no recurse mode mapping_

~~~
:command [attributes] {name_of_command} {command}
                Create custom command
                    example: :command ThisFile put %
                    example with args: :command -nargs=+ Search execute 'vimgrep /' . [<f-args>][0] . '/ **/*.' . [<f-args>][1]
~~~

~~~
:Sexplore       Native vim file explorer with horizontal split window
:Explore        Native vim file explorer
:Nread ftp://{user}@{host}{file_path}
                Open file on a remote server
:Nread {host} {user} {password} {file_path}
                Open file on a remote server
:set bufhidden=hide
                This setting is a trick to edit multiple remote buffer without relog when you switch buffer
~~~

~~~
:echo glob($VIMRUNTIME . '/syntax/*.vim)
                See all supported file type by vim
:set ft?        What filetype setting is used for this buffer
:setf {syntax}  Force {syntax} for this buffer
~~~

~~~
:sort           Sort all line in the buffer
:[range]ce[nter] [width]
                Center text in [range] with line width [width]
~~~

~~~
:vimgrep /{pattern}/[j][g] {range of file}
                Searches {pattern} to {range of file}
:clist          Show all vimgrep search found
:cnext          Go to next vimgrep search result
:cprev          Go to previous vimgrep search result
~~~

~~~
:highlight      Show all defined highlight colors
~~~

~~~
:UseVimball {dir}
                Install the vimball on specified directory {dir}
:VimballList    Show all files contained in the vimball
:RmVimball {vimball}
                Uninstall vimball {vimball}
~~~

~~~
:delfunction {function-name}
                Delete function named {function-name}
~~~

~~~
:debug call {function}()
                Active debug mode for {function}
~~~

~~~
:enew           Open a new empty buffer
~~~

~~~
:perl {perl_command}
                Execute {perl_command}
:python3 {python3_command}
                Execute {python3_command}
:pyfile {python_file}
                Load {python_file}
:ruby {ruby_command}
                Execute {ruby_command}
:rubyfile {ruby_file}
                Load {ruby_file}
~~~


### [Diff]
~~~
:difft[his]     Make the current window part of the diff windows
:windo difft    Diff all windows
:diffs[plit] {filename}
                Open a new window horizontally on the file {filename} to diff
:vert diffsplit {filename}
                Open a new window vertically on the file {filename} to diff
:diffoff[!]     Turn off diff tools
:diffget        Gets change
:diffput        Puts change
do              Gets change
dp              Puts change
:diffupdate     Refresh all window viewports and update the diff highlighting
~~~

~~~
[c              Goto start of the previous change
]c              Goto start of the next change
~~~

```viml
function DiffWithFileFromDisk()
    let filename = expand('%')
    let diffname = filename . '.fileFromBuffer'
    exec 'saveas! ' . diffname
    diffthis
    vsplit
    exec 'edit ' . filename
    diffthis
endfunction
```

### [Ex]
~~~
vim -E -s config.txt <<-EOF
    :%s/foo/bar
    :update
    :quit
EOF
~~~


### [Macro]
~~~
q{register}{commands}q
                Record macro{register}[0-9/a-z] with {commands}
                    example: qa0f=wvg_xalog()<Esc>""Pjq
~~~

~~~
@{register}     Execute macro{register}
@@              Execute the last executed macro
~~~

~~~
5@:.            Execute the last command 5 times
~~~

~~~
:bufdo normal @a
                Execute macro 'a' on all buffers(Work only if set hidden)
:bufdo exe "normal @a" | write
                Execute macro 'a' on all buffers and write the changes
~~~


#### {Redefine macro}
~~~
Add some action at the end 'qA'
Change macro:
    :put a
    Change what you want
    0V
    "ay
~~~


### [Marks]
~~~
:marks          List all the current marks.
:marks {arg}    List the marks that are mentioned in {arg} 
:delm {marks}   Delete the specified marks
~~~


#### {List of Marks Vim Automatically Generates}
~~~
'               Marks the line where the cursor jumped from (in current buffer)
`               Marks the position where the cursor jumped from (in current buffer)
.               Marks the position where the last change occurred (in current buffer)
"               Marks the position where the user last exited the current buffer
[               Marks the beginning of the previously changed or yanked text
]               Marks the end of the previously changed or yanked text
<               Marks the beginning of the last visual selection
>               Marks the end of the last visual selection
~~~


### [Read-only registers]
~~~
"%              Name of the file of current active buffer
"#              Name of the previous name of current active buffer, also called alternate file
".              Last insered text
":              Last command exectuted
~~~


### [Special registers]
~~~
"*              Clipboard of your windowing system
"+              Selected text clipboard
"~              Last selection dropped into vim
~~~

~~~
"-              Black Hole register
                    Think of this like a trash
"/              Search pattern register
~~~

~~~
"=              Expression register
                    Don't forget to use p to paste the result
                    In Insert mode you can use c-r= to paste the result of the expression register
~~~


### [View]
~~~
:mkview [1-9|path]
                Create a view for the current file
:loadview [1-9] Load a view
:source {path}  Load a view from file
~~~


### [Session]
~~~
:mks[ession][!] [file]
                Write a Vim script that restores the current editing session
                    When [!] is included an existing file is overwritten.
                    When [file] is omitted "Session.vim" is used.
:mkview {file}  Write a Vim script that restores the current view(like :mksession but for view)
                    You can specify the view directory with
                    :set viewdir={view_dir}
:loadview {file}
                Load a view from {file}
:source {path}  Loading session from {path}
~~~

~~~
>$ vim -S {path}
                Loading session, command line version
~~~


### [Spell checking]
~~~
:setlocal spell spelllang=en_gb
                Set spellchecking for English(GB) !!On neowin not functionnal
:setlocal nospell
                Disable spellchecking
z=              Suggest alternative word
<C-w>s          In insert mode auto-complete drop down list for word sugestion
]s              Move to the next misspelled word
[s              Move to the previous misspelled word
:spellr         Repeat last spelling correction
~~~


### [Format]
Format function have 3 variables
~~~
v:num           The line number of the first line to format
v:count         The number of lines to format
v:char          This variable holds a character that is going to be insered(it can be empty)
~~~

#### {Formating function example}
```viml
function MyFormatter()
    let first = v:num
    let last  = v:num + v:count
    while(first<-last)
        call setline(first, '> ' . getline(first))
        let first = first + 1
    endwhile
endfunction
```
~~~
:[range]center {width}
                Center line contain in [range](if empty current line) with width {width}
:[range]left [indent]
                Left align with indetation [indent]
:[range]right {width}
                Right align with width {width}
~~~

~~~
yypVr=          Add text headline(copy, paste, replace all characters by '=')
~~~


#### {Function for numbered list example}
```viml
function! NumberList() range
    " set line numbers in front of lines
    let beginning   = line("'<")
    let ending  = line("'>")
    let difsize     = ending-beginning + 1
    let pre     = ' '
    while (beginning <= ending)
        if match(difsize, '^9*$') == 0
            let pre = pre . ' '
        endif
        call setline(ending, pre . difsize . "\t" . getline(ending))
        let ending = ending - 1
        let difsize = difsize - 1
    endwhile
endfunction
```


#### {Function for make indentation, use it with indentexpr}
```viml
function! MyIndenter()
    " Find previous line and get its indentation
    let prev_lineo  = s:prevnonblank(v:lnum)
    let ind     = indent(prev_lineo)
    return ind
endfunction
```

### [Help]
~~~
:h <Plug>       See all about special key name <Plug>
:h <SID>        See all about special key name <SID>
:h autocmd      See how to use autocmd
:h co           See comment format option
:h compiler     See how you can compile in vim
:h ex-command-index
                See all Ex command
:h expression   See how to put together a valid Vim expression
:h feature-list See the complete list of features you can check with has() function
:h fo-table     See how to set format option table
:h formatoptions
                See vim format option
:h function-list
                See all builtin function of Vim
:h functions    See all vimL functions
:h help-translated
                See how to distribute documentation in multiple languages
:h holy-grail   See all vim commands
:h indent-expression
                See more about indent expression
:h indentexpr   See indentexpr documentation
:h ins-completion
                See insert completion help
:h netrw        See help for native file explorer(NETwork Read Write)
:h netrw-externapp
                See help of tool use by native file explore(NETwork Read Write)
:h netrw-netrc  See how to use configuration file for native file explore(NETwork Read Write)
:h pattern-atoms
                See list of all available atoms
:h quickfix     See all about quickfix list
:h ruby-vim     See ruby-vim documentation
:h script-local See help about local script
:h spell        See help for spell checking
:h sts          See Soft tab stop(Converted TAB to space)
:h syn-arguments
                See syntax argument documentation
:h syn-oneline  See help for syntax oneline option
:h tags         See tags help(command, usage, key bidding)
:h ts           See space tab option
:h vimdiff      See how to use vimdiff
:h write-compiler-plugin
:h write-filetype-plugin
:h write-library-script
~~~

~~~
:helptags {documentation_directory}
                Install documentation from {documentation_directory}
~~~

~~~
:helpgrep {pattern} Search {pattern} in vim help
                Use clist to navigage(:cl, :cn, :cp)
~~~


### [Settings]
~~~
:set nu[mber]   Active line number
:set nonu[mber] Disable line number
:set cursorline Active current line highlight
:set nocursorline
                Disable current line highlight
:set cursorcolumn
                Active current line and column highlight
:set nocursorcolumn
                Disable current line and column highlight
:set spelllang=en,us,fr
                Activate spell language [English, US, French]
:set list       Activate view all hidden characters
:set nolist     Disable view all hidden characters
:set textwidth={n}
                Activate format of {n} characters by line
:set formatexpr={lang}#{format_function}
                Use {format_function} to format language {lang}
:set autoindent Activate automatic indentation
:set smartindent
                Activate smart indentation(for C style code)
:set indentexpr={indent_function}
                Activate indentation with {indent_function}
:set paste      Activate paste mode (for avoid stair effect when paste from external)
:set nopaste    Disable paste mode
:set equalprog={command}
                Activate the use of {command} to indent
:set formatprg={command}
                Use {command} to format
                    example: :set formatprg=par\ -w78
                    to format lines with no more than 78 characters
:set nocompatible
                Active no compatible mode to have more vim features
~~~

--------------------------------------------------------------------------------

### [Vim init]
```viml
autocmd {event} {pattern} {cmd}
    " Add {cmd} to the list of commands that Vim will execute automatically on {event} for a file matching {pattern}
```

```viml
autocmd BufNewFile *.html or ~/skeleton.html
    Insert a skeleton file if the file in the buffer don't exist
```

```viml
autocmd BufNewFile * silent! Or ~/templates/%:e.tpl
```

```viml
function! LoadTemplate(extension)
    silent! :execute 'Or ~/templates/' . a:extension . '.tpl'
    silent! execute 'source ~/templates/' . a:extension . '.abbr'
endfunction
autocmd BufNewFile * silent! call LoadTemplate('%:e')
```

```viml
filetype indent on
    Active auto indentation
```

```viml
autocmd FileType sh,cucumber,ruby,yaml,zsh,vim setlocal shiftwidth=2 tabstop=2 expandtab
```

```viml
autocmd Bufread,BufNewFile *.md set filetype=markdown
```

```viml
autocmd FileType xml execute ":silent 1,$!tidy --input-xml true --indent yes -q"
autocmd FileType html, htm execute ":silent 1,$!tidy --indent yes -f /dev/null -q"
```


### [Abbreviations]
~~~
:abbreviate     Abbreviations for all modes
:iabbrev        Abbreviation for Insert mode
:cabbrev        Abbreviation for Command mode
~~~

~~~
:iabbrev {abbrev} {repl}
                Set abbreviation {abbrev} for replacement {repl}
                    example:
                    :iabbrev myAddr 32 Lincoln Road, Birmingham B27 6PA, United Kingdom
~~~


### [Sign]
~~~
:sign define {name} {argument}
                Define a sign for visual markup
                    example:
                    :sign define information text=!> linehl=Warning texthl=Error
~~~

~~~
:exe ":sign place 77 line=" . line('.') . " name=information file=" . expand("%:p")
                Place the information sign with id 77 on current line
~~~

~~~
:map <F7> :exe ":sign place 77 line=" . line('.') . " name=information file=" . expand("%:p")<CR>
                For mapping the sign placement to <F7>
~~~

~~~
:sign unplace {id}
                Unplace the sign with {id}
:sign unplace   Unplace the sign for the current line
~~~

~~~
:sign jump {id} file={file}
                Jump to sign {id} on file {file}
:sign jump {id} buffer={buffer}
                Jump to sign {id} on buffer {buffer}
~~~


### [Templates]

#### {Example}
put this on a file
```html
<html>
    <head>
    <title><+TITLE+></title>
    <meta name="generator" content="<+GENERATOR+>" />
    <meta name="author" content="<+AUTHOR+>" />
    </head>

    <body>
        <p><+CONTENT+></p>
    </body>
</html>
```

put this on your vimrc
```viml
nnoremap <c-j> /<+.\{-1,}+><cr>c/+>/e<cr>
inoremap <c-j> <esc>/<+.\{-1,}+><cr>c/+>/e<cr>
```

you can mark `<+{replace}+>` with
~~~
match Todo /<+.\++>/
~~~

You can make template with abbreviation with
```viml
iabbrev for for(!cursor!; <++>; <++>)<cr>{<cr><tab><++><cr><backspace>}<esc>:call search('!cursor!', 'b')<cr>cf!
```

### [Tags]
~~~
:set tags={tags_path}
                Use the tag file in {tags_path}
:tags           See the tag stack
:tag            Goto the next tag in the stack
:pop            Goto the previous tag in the stack
:tselect        Get a list of matching tags
:ptselect       Show list of matching tags in a preview window
:tnext          Goto the next tag in the list
:tprev          Goto the previous tag in the list
~~~

~~~
c-]             Goto tag definition
c-t             Jump back from the definition
c-w c-]         Open the definition in a horizontal split
g]              Select one tag on a list
~~~


### [Session/View]
~~~
set viewdir={view_path}
autocmd BufWinLeave * mkview
autocmd BufWinEnter * silent loadview
~~~

~~~
autocmd VimEnter * call LoadSession()
autocmd VimLeave * call SaveSession()
~~~

```viml
function SaveSession()
    execute 'mksession! {path_to_vim_session}'
endfunction
function LoadSession()
    if argc() == 0
        execute 'source {path_to_vim_session}'
    endif
endfunction
```
~~~
:set sessionoptions={options}
:echo &sessionoptions
~~~

~~~
silent source! Session.vim
~~~

--------------------------------------------------------------------------------


### Vim command line
~~~
>$ nvim --headless -c "TOhtml|update|quit|quit" framedata.py
                To convert framedata.py to framedata.py.html
~~~

--------------------------------------------------------------------------------


### Vim tricks
~~~
:e **/*.py<TAB> Cycle to all .py file of your project

d/{search}      Delete until found {search}

:t.             Duplicate line(like yyp)

:1,3t4          Duplicate line 1 to 3 and paste after line 4

4d 4            Start line 4 and delete 4 lines

c2l             Delete 2 character and place on Insert mode

:1,10 w {other_file)
                Write line 1 to 10 to {other_file}

:1,10 w >> {other_file}
                Append line 1 to 10 to the end of {other_file}

2f!             Move the cursor to the second '!' found of the current line

:%normal A!     Place '!' in the end of all line

:later 2f       File states, go back 2 buffer writes

:set scrollbind
                Synchronize scroll with other windows
:set noscrollbind
                Stop scroll synchronization
~~~

#### {Files renaming example with an empty buffer}
```viml
:r! ls
ggdd
:%s/\v(\w)(\.txt)/mv & \L\1-\2/ | %s/\.txt$/\=strftime("%Y-%b-%d") . ".txt"/
:w !sh
```

Add this to your ~/.bashrc to use nvim to read man
```bash
# Use nvim for read man pages
function man(){
    for arg in "$@"; do
        nvim -c 'execute "normal! :let no_man_maps = 1\<cr>:runtime ftplugin/man.vim\<cr>:Man '"${arg}"'\<cr>:wincmd o\<cr>"'
    done
}
```

--------------------------------------------------------------------------------


### [Vim Script]

#### {Simple synthax color}
syntax match myComments "/\*.*\*/"
```viml
" Alternative
" syntax region myComments start=/\/\*/ end=/\*\//
" Or more efficient with keyword colorization on commentary
" syntax region myComments start=/\/\*/ end=/\*\// contains=myKeywords
" With
" syntax keyword myKeywords OBSOLETE FIXME TODO
syntax keyword myVars x y
syntax match mySymbols "[{}();=]"
syntax keyword myKeywords if return

highlight myVars ctermfg=red guifg=red
highlight mySymbols ctermfg=blue guifg=blue
highlight myKeywords ctermfg=green guifg=green
highlight myComments ctermfg=yellow guifg=yellow
```

#### {File type detection}
```viml
augroup filetypedetect
autocmd BufNewFile,BufRead *.my setfiletype my
augroup END
```

#### {Variable Scope}
~~~
v:  Vim predefined global scope
g:  Global scope
b:  Buffer scope        - Only available in the buffer where it was defined
t:  Tab scope           - Only available in the Vim tab where it was defined
w:  Window scope        - Only available to the current Vim window (viewport)
l:  Function scope      - Local to the function it is defined in
s:  Sourced file scope  - Local to Vim script loaded using :source
a:  Argument scope      - Used in arguments for functions
~~~


#### {Variable Scope example}
```viml
let g:sum=0
function SumNumbers(num1, num2)
    let l:sum = a:num1 + a:num2
    " check if previous sum was lower than this
    if g:sum < l:sum
        let g:sum = l:sum
    endif
    return l:sum
endfunction

" Test code, this will print 7 (value of l:sum)
echo SumNumbers(3,4)
" This should also print 7 (value of g:sum)
echo g:sum
```

#### {Logical operator}
~~~
==  equal
!=  not equal
>   higher than
<   Lower than
>=  higher than or equal
<=  Lower than or equal
~~~

String specific operator
~~~
=~  contains or equal
!~  not contains
~~~

#### {Function with ...}
```viml
function PrintSum(num1, num2, ...)
    let sum = a:num1 + a:num2
    let argcounter = 1
    " a:0 size of ...
    while argcounter <= a:0
        " a:{n} is the value of the variable argument number n
        let sum += a:{argcounter}
        let argcounter += 1
    endwhile
    echo "the sum is " . sum
    return sum
endfunction
```

```viml
" Alternative
function PrintSum(num1, num2, ...)
    let sum = a:num1 + a:num2
    " a:000 list of argument in ...
    for arg in a:000
        let sum += arg
    endfor
    echo "the sum is " . sum
    return sum
endfunction
```

#### {Standard Vim script header}
```viml
" myscript.vim  : Example script to show how a script is strutured
" Version       : 1.0.5
" Maintener     : bignos@gmail.com
" Last modified : 10/04/18
" License       : This script is release under the Vim License
```

#### {Script-loaded check}
```viml
if exists("loaded_myscript")
    finish "Don't reload the script"
endif
let loaded_myscript = 1
```

#### {Save compatible mode}
```viml
let s:global_cpo = &cpo     " Store current compatible-mode
                            " in local variable
set cpo&vim                 " Go into nocompatible-mode
```

```viml
" And a the end of the script
let &cpo = s:global_cpo
unlet s:global_cpo
```

#### {Script configuration}
```viml
" variable myscript_path
if !exist("myscript_path")
    let s:vimhomepath = split(&runtimepath, ',')
    let s:myscript_path = s:vimhomepath[0] . "/plugin/myscript.vim"
else
    let s:myscript_path = myscript_path
    unlet myscript_path
endif

" variable myscript_indent
if !exist("myscript_indent")
    let s:myscript_indent = 4
else
    let s:myscript_indent = myscript_indent
    unlet myscript_indent
endif
```

#### {Key mappings}
```viml
if !hasmapto('<Plug>MyscriptMyfunctionA')
    map <unique> <Leader>a <Plug>MyscriptMyfunctionA
endif

noremap <unique> <script> <Plug>MyscriptMyfunctionA <SID>MyfunctionA
noremap <SID>MyfunctionA :call <SID>MyfunctionA()<CR>
```

#### {Local script function}
```viml
" this is our local function with a mapping
function s:MyfunctionA()
    echo "This is the script-scope function MyfunctionA speaking"
endfunction

" this is a global function which can be called by anyone
function MyglobalfunctionB()
    echo "Hello from the global-scope function myglobalfunctionB"
endfunction

" this is another global function which can be called by anyone
function MyglobalfunctionC()
    echo "Hello from MyglobalfunctionC() now calling locally:"
    call <SID>MyfunctionA()
endfunction
```

#### {Gvim or Vim}
```viml
if has("gui_running")
    " execute gui-only commands here
endif
```

#### {Which operating system}
```viml
if has("win16") || has("win32") || has("win64") || has("win95")
    " do some shit for windows
elseif has("unix")
    " do real thing for linux/unix
endif
```

#### {Check Vim version}
```viml
if v:version >= 702 || v:version == 701 && has("patch123")
    " Code here is only done for version 7.1 with patch 123
    " and version 7.2 and above
endif
```

#### {Using Perl in your function}
```viml
function MoveCursor(row, col)
    if has("perl")
        perl << EOF
```
```perl
        ($oldrow, $oldcol) = $curwin->Cursor();
        VIM::Msg("Old position was: ($oldrow, $oldcol)");
        $curwin->Cursor(row, col);
```
```viml
EOF
    else
        echo "Perl not available. Canceling function call"
    endif
endfunction
```
--------------------------------------------------------------------------------


### [Debug mode]
~~~
:debug {command}
                Debug mode for {command}
~~~

#### {Debug mode command}
~~~
c[ont]          Continue executing code
q[uit]          Quit the debuggin process without executing the last lines
i[nterrupt]     Stop the current process and go back to the debugger
s[tep]          Execute the next line of code and come back to the debugger
n[ext]          Execute the next command and come back to the debugger
f[inish]        Continue executing the script without stopping on breakpoint
~~~

~~~
breakadd func {linenum} {functionname}
                Add a breakpoint for function {functionname} at line {linenum}
breakadd file {linenum} {finename}
                Add a breakpoint at line {linenum} for file {filename}
breakadd here   Add a breakpoint at this line
breakdel {sameAsbreakadd}
                Delete breakpoint
breakdel *      Delete all breakpoints
>$ vim -D -c 'breakadd file 15 */.vimrc' somefile.txt
                Add a breakpoin with command line
~~~

--------------------------------------------------------------------------------


### [Vim documentation]

first line:
~~~
*docname.txt* single line of description
*myscript.txt* Documentation for example script myscript.vim
~~~


Example
~~~
*myscript.txt* Documentation for example script myscript.vim

Script  :   myscript.vim - Example script for vim developpers
Author  :   Bignose
Email   :   <bignos@gmail.com>
Changed :   10/04/18
================================================================================
                                *myscript-intro*

1. Overview~

This document gives a short introduction to the example
script myscript.vim.
This script is made as an example for vim users on how to
struture a simple vim plugin script such that it is easy
to read and figure out.
The following is covered in this document:

    1. Overview             |myscript-intro|
    2. Mappings             |myscript-mappings|
    3. Functions            |myscript-functions|
    4. Todo                 |myscript-todo|

================================================================================
                                *myscript-functions*

3. Functions~
Besides the functions available via mappings (as descibed 
in |myscript-mappings|) there are some extra global functions
available.

Myglobalfunction()~
This function is one of the global functions in this script.
An example of usage could be: >
    :call Myglobalfunction()

<
    Vim returns:
    Hello from the global-scope function myglobalfunctionB~

MyglobalfunctionC()~
This function is a global function that also calls one of
the internal functions ("s:MyfunctionA()") in the script.
An example of usage could be: >
    :call MyglobalfunctionC()

<

    Vim returns:
    Hello from MyglobalfunctionC() now calling locally:~
    This is the script-scope function MyfunctionA speaking~
================================================================================
~~~

--------------------------------------------------------------------------------

### [Urls]

- [Vim Home](https://www.vim.org/ "Vim Home")
- [Vim Tips](http://vim.wikia.com/wiki/Vim_Tips_Wiki "Vim Tips")

--------------------------------------------------------------------------------

### [Vim games]

- [Vim Golf](https://www.vimgolf.com "Vim Golf")
- [Vim Adventure](https://vim-adventures.com "Vim Adventure")

--------------------------------------------------------------------------------
