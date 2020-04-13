Regex_Pattern = r'^\D[^aeiou][^bdDF]\S[^AEIOU][^\.,]$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())