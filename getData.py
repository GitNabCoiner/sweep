#!./pyinterpret/bin/python
import urllib.request as req
from pprint import pprint
import json,csv,qrcode


headers= {}
headers['User-Agent'] = "urllib3 for python on *nix"

def readlist(f="./testdata.list"):
    addr = [] #address
    secr = [] #secret
    with open(f, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            addr.append(row[0].replace(" ","")) #remove all whitespaces
            secr.append(row[1].replace(" ","")) #pack into lists
    return(addr,secr)


def fragen(addresses=["12EVhdCSjpMPLzg6p6hX36fdcfLuLALoK7","1Bot3SXrKTqYr8fVqAVtRmsRUsELZEP4P9"]):
#instantiate belance result list
  balance_c=[]
  balance_sv=[]

#fetch balances
  for a in addresses:
    url_c=("https://api.blockchair.com/bitcoin-cash/dashboards/address/"+a)
    url_sv=("https://api.blockchair.com/bitcoin-sv/dashboards/address/"+a)
    print("asking bch and bcsv for",str(len(balance_c)+1)+". out of",len(addresses),"addresses.")
    urlobj_c = req.Request(url_c, headers = headers)
    urlobj_sv = req.Request(url_sv, headers = headers)
    jdata_c = req.urlopen(urlobj_c).read()
    jdata_sv = req.urlopen(urlobj_sv).read()
    jd_c = json.loads(jdata_c)
    jd_sv = json.loads(jdata_sv)
    balance_c.append(jd_c['data'][a]['address']['balance'])
    balance_sv.append(jd_sv['data'][a]['address']['balance'])
  return(balance_c,balance_sv)


#generate qrcodes with privkeys of addresses(a) with secret(s) and cash/sv-balance(c/sv)
def qrify(a,s,c,sv):

  for i in range(0,len(a)):
    if c[i]!=0:
      print("bch:",a[i],"mit",c[i])
      #create secret qr
      qr=qrcode.make(s[i])
      qr.save("./out/bch/"+a[i]+".png")

  for i in range(0,len(a)):
    if sv[i]!=0:
      print("sv:",a[i],"mit",sv[i])
      #create secret qr
      qr=qrcode.make(s[i])
      qr.save("./out/sv/"+a[i]+".png")



#collect data
a,s = readlist()
c,sv = fragen(a)

#invoke some qr-magic
qrify(a,s,c,sv)
