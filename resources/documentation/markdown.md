Markdown
========

--------------------------------------------------------------------------------


[ Emphasis: Italic ]
---------------------
To emphasize text wrap it with either a `*` or `_`.

### Markdown
    This is *emphasized* _text_.

### Output
This is *emphasized* _text_.


--------------------------------------------------------------------------------


[ Emphasis: Bold ]
--------------------
To boldly emphasize text, wrap it with either `**` or `__`.

### Markdown
    This is very heavily **emphasized** __text__.

### Output
This is very heavily **emphasized** __text__.


--------------------------------------------------------------------------------


[ Emphasis: Strikethrough ]
--------------------
To Strikethrough emphasize text, wrap it with either `~~` .

### Markdown
    This is a ~~mistaken text~~.

### Output
This is a ~~mistaken text~~.


--------------------------------------------------------------------------------


[ Header ]
----------
HTML headings are produced by placing a number of `#` before the header text corresponding to the level of heading desired (HTML offers 6 levels of headings).  
You can also place under the header `===` for h1  or `---` for h2. 

### Markdown

    # First-level heading

    First-level heading
    ==================

    Second-level heading
    --------------------

    #### Fourth-level heading

### Output
# First-level heading
  
First-level heading
===================
  
Second-level heading
--------------------
  
#### Fourth-level heading


--------------------------------------------------------------------------------


[ Line Return ]
---------------
To force a line return, place `2 empty spaces at the end of a line`.

### Markdown
    Forcing a line-break\s\s
    Next line in the list

### Output
Forcing a line-break  
Next line in the list

--------------------------------------------------------------------------------


[ Paragraphs ]
--------------
A paragraph is `1 or more consecutive lines of text separated by 1 or more blank lines`.  
*Normal paragraphs should not be indented with spaces or tabs.*

### Markdown

    This is a paragraph. It has two sentences.
    
    This is another paragraph. It also has two sentences.

### Output
This is a paragraph. It has two sentences.

This is another paragraph. It also has two sentences.

--------------------------------------------------------------------------------


[ Lists: Simple ]
-----------------
Creating simple lists is done by using ̀`+` , `-` or `*` as list markers.  
These list markers are interchangeable.

### Markdown
    + One
    - Two
    * Three

### Output
+ One
- Two
* Three

--------------------------------------------------------------------------------


[ Lists: Nested ]
-----------------
Nest a list requires you to indent by `exactly 4 spaces`.

### Markdown
    + One
    + Two
    + Three
        - Nested One
        - Nested Two

### Output
+ One
+ Two
+ Three
    - Nested One
    - Nested Two

--------------------------------------------------------------------------------


[ Horizontal rules ]
--------------------
You can create a horizontal rule (`<hr />`) by placing `3 or more -, *, or _ on a single line by themselves`.  
You can also place spaces between them.

### Markdown
    * * *
    
    ***
    
    *****
    
    - - -
    
    ---------------------------------------

### Output
* * *

***

*****

- - -

---------------------------------------
  

--------------------------------------------------------------------------------


[ Links: Inline ]
-----------------
Inline-style links use `[text](link)`

### Markdown
    This is a [Google link](https://www.google.com).

### Output
This is a [Google link](https://www.google.com).

--------------------------------------------------------------------------------


[ Links: Inline with title ]
----------------------------
Inline-style links with title use `[text](link "title")`.

### Markdown
    This is a [Google link](https://www.google.com "The Google link").

### Output
This is a [Google link](https://www.google.com "The Google link").


--------------------------------------------------------------------------------


[ Links: Reference ]
--------------------
Reference-style links allow you to refer to your links by names, which you define elsewhere.

### Markdown
    This is a guide on Markdown [Markdown][1].
    
    [1]: http://en.wikipedia.org/wiki/Markdown "Markdown"

### Output
This is a guide on Markdown [Markdown][1].

[1]: http://en.wikipedia.org/wiki/Markdown "Markdown"


--------------------------------------------------------------------------------


[ Images: Inline ]
------------------
Image syntax is like Link syntax, but prefixed with an `!`.

### Markdown
    ![Google logo](https://www.google.fr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png "Google Logo")

### Output
![Google logo](https://www.google.fr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png "Google Logo")

--------------------------------------------------------------------------------


[ HTML ]
--------
You can use HTML code to customise the display

### Markdown
```html
<p align="center">
  <b>Some Links:</b><br>
  <a href="#">Link 1</a> |
  <a href="#">Link 2</a> |
  <a href="#">Link 3</a>
  <br><br>
  <img src="https://www.google.fr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png">
</p>
```

### Output
<p align="center">
  <b>Some Links:</b><br>
  <a href="#">Link 1</a> |
  <a href="#">Link 2</a> |
  <a href="#">Link 3</a>
  <br><br>
  <img src="https://www.google.fr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png">
</p>


--------------------------------------------------------------------------------


[ Blockquote ]
--------------
To enclose a segment of text in blockquotes, one must prefix each written line with a `>`.

### Markdown
    > ## Blockquoted header
    >
    > This is a blockquoted text
    >
    > This is a second paragraph withing the blockquoted text

### Output
> ## Blockquoted header
>
> This is a blockquoted text
>
> This is a second paragraph withing the blockquoted text


--------------------------------------------------------------------------------


[ Code:Inline ]
---------------
If you want to mark inline element as code, use _`_ (backquote)

### Markdown
    Markdown is a `<em>text-to-html</em>` convertion tool for writers

### Output
Markdown is a `<em>text-to-html</em>` convertion tool for writers


--------------------------------------------------------------------------------


[ Code:Block ]
--------------
If you want to mark something as code, indent it by `4 spaces`

### Markdown
>    `<p>This as been indented by 4 spaces.<\p>`

### Output
    <p>This as been indented by 4 spaces.</p>


--------------------------------------------------------------------------------


![github flavored markdown](https://lh3.googleusercontent.com/UCXiIJ_T8BDlpqTMp6YsqCo-bkajIl92lDqcuz2z0Nil4VjJzHnYYhbx_G_IkU60ICFRfj0dzF0=w128-h128-e365)

[ Fenced code blocks ]
----------------------
You can create fenced code blocks by placing a `triple backquote before and after the code block`.  
We recommend placing a blank line before and after code blocks to make the raw formatting easier to read.

### Markdown
    ```
    
    function test() {
      console.log("notice the blank line before this function?");
    }
    
    ```

### Output
```

function test() {
  console.log("notice the blank line before this function?");
}

```

--------------------------------------------------------------------------------


![github flavored markdown](https://lh3.googleusercontent.com/UCXiIJ_T8BDlpqTMp6YsqCo-bkajIl92lDqcuz2z0Nil4VjJzHnYYhbx_G_IkU60ICFRfj0dzF0=w128-h128-e365)

[ Syntax highlighting ]
-----------------------
You can add an optional language identifier to enable syntax highlighting in your fenced code block.

### Markdown
    ```ruby
    require 'redcarpet'
    markdown = Redcarpet.new("Hello World!")
    puts markdown.to_html
    ```
### Output
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

--------------------------------------------------------------------------------


![github flavored markdown](https://lh3.googleusercontent.com/UCXiIJ_T8BDlpqTMp6YsqCo-bkajIl92lDqcuz2z0Nil4VjJzHnYYhbx_G_IkU60ICFRfj0dzF0=w128-h128-e365)

[ Table ]
---------
You can create tables with `|` and `-`.  
Hyphens are used to create each column's header, while pipes separate each column.  
You must include a blank line before your table in order for it to correctly render.

### Markdown
    
    | First Header  | Second Header |
    | ------------- | ------------- |
    | Content Cell  | Content Cell  |
    | Content Cell  | Content Cell  |

### Output

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

--------------------------------------------------------------------------------


![github flavored markdown](https://lh3.googleusercontent.com/UCXiIJ_T8BDlpqTMp6YsqCo-bkajIl92lDqcuz2z0Nil4VjJzHnYYhbx_G_IkU60ICFRfj0dzF0=w128-h128-e365)

[ Task lists ] 
--------------
To create a task list, preface list items with a regular space character followed by `[ ]`. To mark a task as complete, use `[x]`.

### Markdown
    - [x] Finish my changes
    - [ ] Push my commits to GitHub
    - [ ] Open a pull request

### Output
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

--------------------------------------------------------------------------------
