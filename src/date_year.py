import re

def date_year(x):
    mat = ''
    pattern = (r'(\w{4})(\.b)?$')
    matches = re.search(pattern, x)
    
    return matches.group(1)





print(date_year('1000 2000'))
