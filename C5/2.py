import requests
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)
    return r.content
htmldata = getdata("https://www.rust-lang.org/")
soup = BeautifulSoup(htmldata,'html.parser')

print("SJC23MCA-2053 : SREYAS SATHEESH")
print("Batch : MCA 2023-25\n")

links = soup.find_all("a")
print("Total number of links : ",len(links))
for link in links:
    if link.get("href") != "":
        print("Link :",link.get("href"),"Text :",link.string)