Regex_Pattern = r"^\d\w{4}.$"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())