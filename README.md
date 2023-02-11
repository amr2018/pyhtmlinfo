 
 # pyhtmlinfo
 pyhtmlinfo is a python library it can be used to get html tags and description
 not only that you can get deprecated html tags or html elements
 by using  is_old_or_deprecated(tag) this function return True
 if the tag old or deprecated

 ## Examples 

 convert name to tag ex: h2 -- > <h2>

 ```python
 from pyhtmlinfo import name_to_tag

 name_to_tag('h2') - > '<h2>'

 ```



 convert tag to name ex: <h2> -- > h2

 ```python
 from pyhtmlinfo import tag_to_name

 tag_to_name('h2') - > '<h2>'


 ```

 check if tag or element not old or deprecated

 ```python

 from pyhtmlinfo import is_old_or_deprecated

 is_old_or_deprecated('<noframes>') -> True

 
 ```

 get all new tags by default if you want old tags set only_new = False

 ```python

 from pyhtmlinfo import get_all_tags

 get_all_tags() -> tags list

 
 ```


  get tag Description 

 ```python

 from pyhtmlinfo import get_tag_description

 get_tag_description('<body>') -> 

 The <body> HTML element represents the content of an HTML document. There can be only one <body> element in a document.

 
 ```



   check if word may be html tag 

 ```python

 from pyhtmlinfo import is_maybe_html_tag

 is_maybe_html_tag('h2') - > True
 
 
 ```
