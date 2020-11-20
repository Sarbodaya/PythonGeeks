"""
[] -> Represent the character class
^  -> Matches the beginning
$  -> Matches End
.  -> Matches any character except new line
?  -> Matches zero or one occurrence
|  -> Means OR (Matches with any of the characters separated by it.
*  -> Any number of occurrences (including 0 occurrences).
+  -> One or more occurrences
{} -> Indicate number of occurrences of a preceding RE to match.
() -> Enclose a group of REs
"""

import re
p = re.compile('[a-e]')
print(p.findall('Aye, said Mr. Gibenson Stark'))

