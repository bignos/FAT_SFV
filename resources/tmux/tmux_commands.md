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

#### {Panes}
| Command                                           | Information                                               |
| ------------------------------------------------- | --------------------------------------------------------- |
| %P:split-window -h                                | Split pane horizontally                                   |
| %P%                                               | Split pane horizontally                                   |
| %P:split-window -v                                | Split pane vertically                                     |
| %P"                                               | Split pane vertically                                     |
| `<C-d>`                                           | Close a pane                                              |
| %Px                                               | Force quit pane                                           |
|                                                   |                                                           |
| %Po                                               | Cycle through pane                                        |
| %P:select-pane -L                                 | Move to pane left                                         |
| %P`<left>`                                        | Move to pane left                                         |
| %P:select-pane -R                                 | Move to pane right                                        |
| %P`<right>`                                       | Move to pane right                                        |
| %P:select-pane -U                                 | Move to pane up                                           |
| %P`<up>`                                          | Move to pane up                                           |
| %P:select-pane -D                                 | Move to pane down                                         |
| %P`<down>`                                        | Move to pane down                                         |
| %Pq                                               | Display numeric value on top of eac                       |
| %Pq{pane_id}                                      | Move to pane {pane_id}                                    |
| %P;                                               | Goto last pane                                            |
|                                                   |                                                           |
| %P`<C-left>`                                      | Resize pane on left                                       |
| %P`<C-right>`                                     | Resize pane on right                                      |
| %P`<C-up>`                                        | Resize pane on up                                         |
| %P`<C-down>`                                      | Resize pane on down                                       |
| %P`<M-left>`                                      | Resize pane on left by 5                                  |
| %P`<M-right>`                                     | Resize pane on right by 5                                 |
| %P`<M-up>`                                        | Resize pane on up by 5                                    |
| %P`<M-down>`                                      | Resize pane on down by 5                                  |
| %P:resize-pane                                    | Resize pane to take all the place / return to normal size |
| %Pz                                               | Resize pane to take all the place / return to normal size |
| %P:break-pane                                     | Detach pane(transform pane to window)                     |
| %P!                                               | Detach pane(transform pane to window)                     |
|                                                   |                                                           |
| %P{                                               | Rotate pane clockwise                                     |
| %P}                                               | Rotate pane counterclockwise                              |
| %P`<space>`                                       | Switch pane layout                                        |
|                                                   |                                                           |
| %P:select-layout even-horizontal                  | Distribute same space horizontally on all pane            |
| %P:select-layout even-vertical                    | Distribute same space vertically on all pane              |

#### {Windows}
| Command                                                | Information                                                  |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| %P:new-window                                          | Create a new window                                          |
| %Pc                                                    | Create a new window                                          |
| %P:rename-window -t {window_id|window_name} {new_name} | Rename windows({window_id} or {window_name}) with {new_name} |
|                                                        |                                                              |
| %P:join-pane -s {source_window} -t {target_window}     | Join the source window into the target window                |
|                                                        |                                                              |
| %P{window_id}                                          | Goto {window_id} window                                      |
| %Pn                                                    | Goto next window                                             |
| %Pp                                                    | Goto previous window                                         |
| %P:choose-window                                       | Choose a window                                              |
| %Pw                                                    | Choose a window                                              |
| %P:kill-window                                         | Close current window                                         |
| %P&                                                    | Close current window                                         |
| %P:find-window                                         | Find window                                                  |
| %Pf                                                    | Find window                                                  |
|                                                        |                                                              |
| %P:move-window -t 4                                    | Move current window to position 4                            |
| %P:move-window -t {session:window_id}                  | Move window                                                  |
| %P.                                                    | Move window                                                  |
| %P:swap-window -s 1 -t 3                               | Swap window 1 and 3                                          |
|                                                        |                                                              |
| `>$ tmux move-window -s foo:1 -t bar`                  | Move the window 1 in foo session to bar session              |
|                                                        |                                                              |
| %P:link-window -t bar:2                                | Share window 2 in bare session to current session            |

#### {Synchronize pane}
| Command                                                | Information                                                  |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| %P:setw synchronize-panes on                           | Active pane synchronization                                  |
| %P:setw synchronize-panes off                          | Disable pane synchronization                                 |

#### {Scripting}
| Command                                                | Information                                                                   |
| ------------------------------------------------------ | ----------------------------------------------------------------------------- |
| `>$ tmux send-key -t 1 "vim" "C-m" "i" "Hello world"`  | Send key sequence to last session and pane 1 [vim, `<Enter>`, i, hello world] |
|                                                        |                                                                               |
| `>$ tmux send-key -t foo:2 "vim" "C-m"`                | Send key sequence to foo session and pane 2                                   |

##### Script example
```bash
#!/bin/bash
tmux new -s foo -d "top" && \
tmux split-window -t foo:1 && \
tmux break-pane && \
tmux send-key "vim" "C-m" "i"
#End bash script
```
##### Tips
| Command                                                | Information                                                                   |
| ------------------------------------------------------ | ----------------------------------------------------------------------------- |
| %P`:run-shell [-b] [-t {pane_id}] "{shell_command}"`   | Run {shell_command} without use of window                                     |
|                                                        |                                                                               |
| `bind-key u if-shell "test $(ls | grep Dropbox | wc -l) -gt 0" "display-message 'Folder does not exist'" "display-message 'Folder exist'"` | Conditional key bindings, if directory "Dropbox" exist %Pu display a message and if not %Pu display a different message |

--------------------------------------------------------------------------------
