import os
import csv
import sys
from selenium import webdriver
from bs4 import BeautifulSoup

arg = sys.argv
mydir = os.path.dirname('data')
ke, x = 1, 0
perpage = len(arg) > 1 and (arg[1].isdigit() and int(arg[1]) or 1000) or 1000
limitpage = len(arg) > 2 and (arg[2].isdigit() and int(arg[2]) or 84) or 84
fname = len(arg) > 3 and arg[3] or "data.csv"

f = open(os.path.join(mydir, fname),  "w")
tab = "no,kodepos,kel,kodewilayah,kec,dt2,kota,prov"
out = csv.writer(f)
out.writerow(tab.split(","))


def parse(ss):
    global x
    soup = BeautifulSoup(ss, 'html.parser')
    for data in soup.findAll("tr", bgcolor="#ccffff"):
        row = [s.text for s in data.findAll("td")]
        out.writerow(row)
        x += 1


while True:
    if ke>1: url="https://www.nomor.net/_kodepos.php?_i=desa-kodepos&daerah=&jobs=&perhal=%s&urut=8&asc=0001000&sby=000000&no1=%s&no2=%s&kk=%s"%(perpage, (perpage*(ke-2))+1, ((perpage*(ke-1))+1)-1, ke)
    else: url="https://www.nomor.net/_kodepos.php?_i=desa-kodepos&daerah=&jobs=&perhal=%s&sby=000000&asc=0001000&urut=8"%perpage
    print(url)
    PATH = "C:\Program Files\Google\Chrome\Application\chromedriver.exe" # Path to chromedriver (Adjust as needed)
    driver = webdriver.Chrome(PATH)
# If you need to add headers to the request
#chrome.header overrides = {
    driver.get (url) # Get the URL you need to scrape
    c = driver.page_source # Extract the HTML
    driver.quit()
    if c.find("#ccffff") < 1 or ke > limitpage:
        break
    parse(c)
    ke += 1
f.close()
