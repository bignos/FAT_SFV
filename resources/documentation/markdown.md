			   <center>Markdown</center>
================================================================================

--------------------------------------------------------------------------------

[ Blockquote ]
--------------
To enclose a segment of text in blockquotes, one must prefix each written line with a **>**.

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


[ Code:Block ]
--------------
If you want to mark something as code, indent it by **4 spaces**

### Markdown
>    `<p>This as been indented by 4 spaces.<\p>`

### Output
    <p>This as been indented by 4 spaces.</p>


--------------------------------------------------------------------------------


[ Code:Inline ]
---------------
If you want to mark inline element as code, use **\`** (backquote)

### Output

### Markdown
    Markdown is a `<em>text-to-html</em>` convertion tool for writers

### Output
Markdown is a `<em>text-to-html</em>` convertion tool for writers


--------------------------------------------------------------------------------


[ Emphasis: Italics ]
---------------------
To emphasize text wrap it with either a **\*** or **\_**.

### Markdown
    This is *emphasized* _text_.

### Output
This is *emphasized* _text_.


--------------------------------------------------------------------------------


[ Emphasis: Strong ]
--------------------
To boldly emphasize text, wrap it with either __\*\*__ or **\_\_**.

### Markdown
    This is very heavily **emphasized** __text__.

### Output
This is very heavily **emphasized** __text__.


--------------------------------------------------------------------------------


[ Header ]
----------
HTML headings are produced by placing a number of **#** before the header text corresponding to the level of heading desired (HTML offers six levels of headings).

### Markdown
    # First-level heading

    Fist-level heading
    ==================

    Seconde-level heading
    ---------------------

    #### Fourth-level heading

### Output
# First-level heading
                         
Fist-level heading
==================
                         
Seconde-level heading
---------------------
                         
#### Fourth-level heading


--------------------------------------------------------------------------------


[ Horizontal rules ]
--------------------
You can create a horizontal rule (`<hr />`) by placing **3 or more -, *, or _ on a single line by themselves**.  
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


[ Images: Inline ]
------------------
Image syntax is very similar to Link syntax, but prefixed with an **!**.

### Markdown
    ![Google logo](https://www.google.fr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png "Google Logo")

### Output
![Google logo](https://www.google.fr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png "Google Logo")

--------------------------------------------------------------------------------


[ Line Return ]
---------------
To force a line return, place **2 empty spaces at the end of a line**.

### Markdown
    Forcing a line-break\s\s
    Next line in the list

### Output
Forcing a line-break  
Next line in the list

--------------------------------------------------------------------------------

[ Links: Inline ]
-----------------
Inline-style links use **()** immediately after the link text.

### Markdown
    This is a [Google link](https://www.google.com).

### Output
This is a [Google link](https://www.google.com).

--------------------------------------------------------------------------------


[ Links: Inline with title ]
----------------------------

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


[ Lists: Simple ]
-----------------
Creating simple lists is done by using __+__, __-__ or __*__ as list markers.  
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
Nest a list requires you to indent by **exactly 4 spaces**.

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


[ Paragraphs ]
--------------
A paragraph is one or more consecutive lines of text separated by one or more blank lines.  
**Normal paragraphs should not be indented with spaces or tabs.**

### Markdown
    This is a paragraph. It has two sentences.
    
    This is another paragraph. It also has two sentences.

### Output
This is a paragraph. It has two sentences.

This is another paragraph. It also has two sentences.


--------------------------------------------------------------------------------
