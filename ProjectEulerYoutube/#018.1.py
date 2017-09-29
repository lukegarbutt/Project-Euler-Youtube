import urllib.request
import re

page_source = urllib.request.urlopen('https://projecteuler.net/problem=18')
page_source = str(page_source.read())
#print(page_source)
numbers = re.findall(r'<p>(\d*)</p>', page_source, flags=re.DOTALL)
print(numbers)