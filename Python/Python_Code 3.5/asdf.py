import re
#check = re.compile('(^[\+|\-]?\d+)')
check = re.compile('[\s]*([\+|\-]?\d+)')
print(check.search('     +-123'))
