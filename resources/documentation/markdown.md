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
You can also place under the header: 
-   `===` for h1
-   `---` for h2 

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


[ List: Ordered ] 
------------------
Creating ordered lists is done by using `[1. - n.]`

### Markdown
    1. First element
    2. Second element
        1. first under element
    3. Third element
    4. Fourth element

### Output
1. First element
2. Second element
    1. first under element
3. Third element
4. Fourth element

--------------------------------------------------------------------------------


[ List: Dynamic Ordered ] 
------------------------
Creating dynamic ordered lists is done by using only `1.`  
*This option is less readable in text mode*

### Markdown
    1. First element
    1. Second element
    1. Third element
    1. Fourth element

### Output
1. First element
1. Second element
1. Third element
1. Fourth element

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


[ Links: Auto ] 
----------------
Autolinks are absolute URIs and email addresses inside `<` and `>`.  
They are parsed as links, where the URI or email address itself is used as the link's label.

### Markdown
    <https://www.google.com>

### Output
<https://www.google.com>

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


[ Links: Named Anchor ] 
------------------------
Named anchors enable you to jump to the specified anchor point on the same page.
_Note that placement of achors is arbitrary, you can put them anywhere you want, not just in headings.  
This makes adding cross-references easy when writing markdown._

### Markdown
~~~
# Table of Contents
* [Chapter 1](#chapter-1)
* [Chapter 2](#chapter-2)
* [Chapter 3](#chapter-3)

## Chapter 1 <a name="chapter-1"></a>
Content for chapter one.

## Chapter 2 <a name="chapter-2"></a>
Content for chapter one.

## Chapter 3 <a name="chapter-3"></a>
Content for chapter one.
~~~

### Output
# Table of Contents
* [Chapter 1](#chapter-1)
* [Chapter 2](#chapter-2)
* [Chapter 3](#chapter-3)

## Chapter 1 <a name="chapter-1"></a>
Content for chapter one.

## Chapter 2 <a name="chapter-2"></a>
Content for chapter one.

## Chapter 3 <a name="chapter-3"></a>
Content for chapter one.

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
Also you can use nested level of quoting with `more >`.

### Markdown
    > ## Blockquoted header
    >
    > This is a blockquoted text
    >> This is a level 2 
    >>> This is a level 3

### Output
> ## Blockquoted header
>
> This is a blockquoted text
>> This is a level 2 
>>> This is a level 3


--------------------------------------------------------------------------------


[ Code:Inline ]
---------------
If you want to mark inline element as code, use __`__ (backtick)

### Markdownn
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
You can create fenced code blocks by placing:
- __```__
- __~~~__

before and after the code block.  
*We recommend placing a blank line before and after code blocks to make the raw formatting easier to read.*

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

Align text in column with
- `---` Left
- `-:-` Center
- `--:` Right

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
