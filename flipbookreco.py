'''
list of all books category wise using flipkart api
'''
from pprint import pprint
import pycurl
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url = "https://affiliate-api.flipkart.net/affiliate/1.0/booksApi/597f25107aae45feb7f6695594aeb41d.json"
ids = []
curl_instance = pycurl.Curl()
curl_instance.setopt(curl_instance.VERBOSE , True)

#Opening a file to read:

f = open('json.txt','w')
curl_instance.setopt(curl_instance.URL, url)
curl_instance.setopt(curl_instance.WRITEDATA,f)
curl_instance.perform()
f.close()
f = open('json.txt', 'r')
body = f.read()
body_json = json.loads(body)
s = "subCategories"
n = "name"
d = body_json["booksCategory"][s]
# Don't get confused. The below loops iterate lists of dictionary(list(dict..... till we get an empty list/
# Basically it is a hierarchical Depth first traversal
file_books = open("booklist.txt","w")
print books
for i in range(0,len(d)):
    e = d[i][s]
    file_books.write(d[i][n])
    file_books.write("\n\t")
    for j in range(0,len(e)):
        f = e[j][s]
        file_books.write(e[j][n])
        file_books.write("\n\t\t")
        for k in range(0,len(f)):
            g = f[k][s]
            file_books.write(f[k][n])
            file_books.write("\n\t\t\t")
            for l in range(0,len(g)):
                h = g[l][s]
                file_books.write(g[l][n])
                file_books.write("\n\t\t\t\t")
                for o in range(0,len(h)):
                    m = h[o][s]
                    file_books.write(h[o][n])
curl_instance.close()
file_books.close()
