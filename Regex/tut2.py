"""
\d :  Matches any decimal digit, this is equivalent to the set class [0-9].
\D :  Matches any non-digit character.
\s :  Matches any whitespace character.
\S :  Matches any non-whitespace character
\w :  Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].
\W :  Matches any non-alphanumeric character.
"""

import re

p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

p = re.compile('\w')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))


