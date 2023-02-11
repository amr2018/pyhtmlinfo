
from html_data import Tags
from html_data import Deprecated_tags
import re

# convert tag to name ex: <h2> -- > h2
def tag_to_name(tag):
	tag_name = re.findall('[a-z0-9]', tag, flags=re.IGNORECASE)
	return ''.join(tag_name)

# convert name to tag ex: h2 -- > <h2>
def name_to_tag(tag_name):
	return f'<{tag_name}>'



# check if tag or element not old or deprecated
def is_old_or_deprecated(tag):
	for i in Deprecated_tags:
		if tag == i:
			return True

	return False



# get all new tags by default if you want old tags set only_new = False

def get_all_tags(only_new = True):

	tags_list = []
	for tag in Tags:
		tags_list.append(tag)

	if not only_new:
		for tag in Deprecated_tags:
			tags_list.append(tag)

	return tags_list


# check if word may be html tag
def is_maybe_html_tag(word):
	tag = name_to_tag(word)
	tags = get_all_tags(only_new=False)
	if tag in tags:
		return True
	else:
		return False



# get tag Description 
def get_tag_description(tag):
	for t in get_all_tags(only_new=False):
		if '|' in t: # if key containe on h2|h3|h4
			h_tags = t.split('|')
			if tag in h_tags:
				return Tags[t]

		if tag == t:
			if tag in Tags:
				return Tags[tag]
			elif tag in Deprecated_tags:
				return Deprecated_tags[tag]
			else:
				return False

