from tools import getResults
import requests

# state = 'RRBBUFBFBRLRRRFRDDURUBFBBRFLUDUDFLLFFLLLLDFBDDDUUBDLUU'
# res, success = getResults(state)
# print(res, success)

url = 'http://127.0.0.1:5000/solve'
d = {'state': 'LRLDURBDUFDBFLLFFFRLLLBDDFLRRDBDURFDBBUBRBUUBDUUUFRRLF'}
r = requests.post(url, data=d)
print(r.text)