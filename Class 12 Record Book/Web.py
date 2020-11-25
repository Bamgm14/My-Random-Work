import requests as r
p=r.get('https://www.york.ac.uk/teaching/cws/wws/webpage1.html')
print(p.text)
