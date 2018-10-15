TMux
====

--------------------------------------------------------------------------------
__%P = TMux prefix key(default: c-b)__

| Command                                           | Information                    |
| ------------------------------------------------- | ------------------------------ |
| %P:list-keys                                      | TMux key bidding information   |
| %P:list-commands                                  | TMux commands list             |
| %P:info                                           | TMux session information       |
|                                                   |                                |
| %P~                                               | TMux messages                  |
| %P:show-messages                                  | TMux messages                  |
|                                                   |                                |
| %P:choose-session                                 | To change TMux session         |
| %P(                                               | Move to next session           |
| %P)                                               | Move to previous session       |
| %P$                                               | Renaming session               |
| %P:rename-session -t {current_id} {new_id}        | Renaming session               |
| `>$ tmux rename-session -t {current_id} {new_id}` | Renaming session               |
|                                                   |                                |
| %P:copy-mode                                      | Copy mode                      |
| %P[                                               | Copy mode                      |
| %P:paste-mode                                     | Paste last copy                |
| %P]                                               | Paste last copy                |
| %P:list-buffers                                   | List all copy buffer           |
| %P#                                               | List all copy buffer           |
| %P:show-buffer                                    | Show last copy                 |
| %P:capture-pane                                   | Copy the entire pane           |
| %P:save-buffer {file}                             | Save the entire pane to {file} |
| %P:choose-buffer                                  | Choose buffer to paste         |
| %P=                                               | Choose buffer to paste         |


#### {copy-mode}

| Command                                           | Information                        |
| ------------------------------------------------- | ---------------------------------- |
| :50                                               | Goto line 50                       |
| /{pattern}                                        | Search forward through the buffer  |
| ?{pattern}                                        | Search backward through the buffer |
| `<space>`                                         | Active selection                   |
| `<CR>`                                            | Quit copy-mode                     |
| q                                                 | Quit copy-mode                     |

{Panes}
%P:split-window -h
%P%         Split pane horizontally
%P:split-window -v
%P"         Split pane vertically
<C-d>           Close a pane
%Px         Force quit pane

%Po         Cycle through pane
%P:select-pane -L   
%P<left>        Move to pane Left
%P:select-pane -R   
%P<right>       Move to pane Right
%P:select-pane -U   
%P<up>          Move to pane Up
%P:select-pane -D   
%P<down>        Move to pane Down
%Pq         Display numeric value on top of each pane
%Pq{pane_id}        Move to pane {pane_id}
%P;         Goto last pane

%P<C-left>      Resize pane on left
%P<C-right>     Resize pane on right
%P<C-up>        Resize pane on up
%P<C-down>      Resize pane on down
%P<M-left>      Resize pane on left by 5
%P<M-right>     Resize pane on right by 5
%P<M-up>        Resize pane on up by 5
%P<M-down>      Resize pane on down by 5
%P:resize-pane
%Pz         Resize pane to take all the place / return to normal size
%P:break-pane
%P!         Detach pane(transform pane to window)

%P{         Rotate pane clockwise
%P}         Rotate pane counterclockwise
%P<space>       Switch pane layout

%P:select-layout even-horizontal
            Distribute same space horizontally on all pane
%P:select-layout even-vertical
            Distribute same space vertically on all pane

{Windows}
%P:new-window
%Pc         Create a new window
%P:rename-window -t {window_id|window_name} {new_name}
            Rename windows({window_id} or {window_name}) with {new_name}

%P:join-pane -s {source_window} -t {target_window}
            Join the source window into the target window
            Transform window to pane

%P{window_id}       Goto {window_id} window
%Pn         Goto next window
%Pp         Goto previous window
%P:choose-window
%Pw         Choose a window
%P:kill-window
%P&         Close current window
%P:find-window
%Pf         Find window

%P:move-window -t 4 Move current window to position 4
%P:move-window -t {session:window_id}
            Move window
%P.         Move window
%P:swap-window -s 1 -t 3
            Swap window 1 and 3

>$ tmux move-window -s foo:1 -t bar
            Move the window 1 in foo session to bar session

%P:link-window -t bar:2
            Share window 2 in bare session to current session

{Synchronize pane}
%P:setw synchronize-panes on
            Active pane synchronization
%P:setw synchronize-panes off
            Disable pane synchronization

{Scripting}

>$ tmux send-key -t 1 "vim" "C-m" "i" "Hello world"
            Send key sequence to last session and pane 1 [vim, <Enter>, i, Hello world]

>$ tmux send-key -t foo:2 "vim" "C-m"
            Send key sequence to foo session and pane 2

#!/bin/bash
tmux new -s foo -d "top" && \
tmux split-window -t foo:1 && \
tmux break-pane && \
tmux send-key "vim" "C-m" "i"
#End bash script

%P:run-shell [-b] [-t {pane_id}] "{shell_command}"
            Run {shell_command} without use of window

bind-key u if-shell "test $(ls | grep Dropbox | wc -l) -gt 0" "display-message 'Folder does not exist'" "display-message 'Folder exist'"
            Conditional key bindings, if directory "Dropbox" exist %Pu display a message and if not %Pu display a different message

--------------------------------------------------------------------------------
