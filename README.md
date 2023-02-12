# Pyhtmlinfo

Pyhtmlinfo is a python library that can be used to learn about html tags
you can get info about latest tags and deprecated tags too

## Installation

* Using PyPi
```
python pip install pyhtmlinfo
````

* Using this Github Repo
```
python pip install git+https://github.com/amr2018/pyhtmlinfo.git
````

## Examples

```python
from pyhtmlinfo import HtmlInfo

html_info = HtmlInfo()

tags_list = html_info.all_tags(deprecated=True) # Returns all tags, set deprecated False to return only working tags.

tag = html_info.name_to_tag('h1') # --> <h1>

tag_name = html_info.tag_to_name('<h1>') # --> h1

tag_description = html_info.is_deprecated('<img>') # --> The <img> HTML element embeds an image into the document.

is_tag = html_info.is_html_tag('<h1>') # --> True

is_deprecated = html_info.is_deprecated('acronym') # --> True
```

## Credits

* Tags and Description from [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#main_root)
