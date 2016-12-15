import requests
from bs4 import BeautifulSoup

#You can change head and tail url to scrape other categories also :)
headurl="http://www.alexa.com/topsites/category;"
tailurl="/Top/Computers/Hacking"

#You can change head and tail url to scrape other categories also :)


linkslist=[]

for i in range(0,20):
    baseurl=headurl+str(i)+tailurl;
    print "scrapping "+ str((i+1)*5)+"% done"
    rootpage=requests.get(baseurl).text
    soup = BeautifulSoup(rootpage,"html5lib")
    for link in soup.find_all('a'):
        tt=link.get('href')
        tt = str(tt)
        if ('/siteinfo/' in tt)&(len(tt)>10):
            tt = "www."+tt[10:]
            linkslist.append(tt)


filename = tailurl.split('/')[-1]
print filename
thefile = open(filename,'w+');
thefile.write(tailurl+"\n")


for links in linkslist:
    print links
    thefile.write(links+"\n")


print "Links saved to file:"+filename


