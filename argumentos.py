import sys
from urllib.parse import urlencode
_url = sys.argv[0]
print(_url)
time='{0}?{1}'.format(_url, urlencode(action='play',video='Creativerse'))
print(time)
