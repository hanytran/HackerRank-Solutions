Regex_Pattern = r'^[24680a-zA-Z]{40}[13579\s]{5}$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())