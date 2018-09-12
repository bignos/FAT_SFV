--------------------------------------------------------------------------------
			Vim plugins install notes
--------------------------------------------------------------------------------

{ New shortcuts }

- [ Python-mode ]
	
	{ Code navigation }
	[[    			Jump to previous class or function (normal, visual, operator modes)
	]]    			Jump to next class or function  (normal, visual, operator modes)
	[M    			Jump to previous class or method (normal, visual, operator modes)
	]M    			Jump to next class or method (normal, visual, operator modes)
	aC    			Select a class. Ex: vaC, daC, yaC, caC (normal, operator modes)
	iC    			Select inner class. Ex: viC, diC, yiC, ciC (normal, operator modes)
	aM    			Select a function or method. Ex: vaM, daM, yaM, caM (normal, operator modes)
	iM    			Select inner function or method. Ex: viM, diM, yiM, ciM (normal, operator modes)

	{ Code helper }
	K			Show documentation for current word (selection)
	\r			Run python code
	F7			Check code in current buffer
	F8			Auto-fix code in current buffer
	<C-c>d			Show documentation for object under cursor
	<C-Space>		Python code autocompletion
	<C-C>g			Go to definition

	{ Refactoring }
	<C-c>rr			Do renaming
	<C-c>r1r		Rename current module
	<C-c>ro			Oraganize import
	<C-c>r1p		Convert module to package
	<C-c>rm			Extract method from selected lines
	<C-c>rl			Extract variable from selected lines
	<C-c>ru			find the places in which a function can be used and changes the code to call it instead
	<C-c>rv			Move method/field
	<C-c>rs			Change function signature

** More precise help whith ':help pymode'

- [ SimpylFold ]
	Space			Fold/unfold

- [ NERDTree ]
	<M-e>			Toggle NERDTree

- [ CtrlP ]
	<C-p>			Activate file search

- [ Ack ]
	:Ack! {pattern}		Do pattern search in all project file
- [ Tabular ]
	:Tabularize {pattern}	Do pattern tabulation ( see example in https://github.com/godlygeek/tabular/blob/master/doc/Tabular.txt )

--------------------------------------------------------------------------------
