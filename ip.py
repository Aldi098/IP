#!usr/bin/python
#Open source



















































































































































































































import os
import json
import requests

b='\033[1;94m'

i='\033[1;92m'

c='\033[1;96m'

m='\033[1;91m'

u='\033[1;95m'

k='\033[1;93m'

p='\033[1;97m'

h='\033[1;92m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

__logo__ = """

%s _ ___    ____ ___  ___  ____ ____ ____ ____ 
%s | |__]   |__| |  \ |  \ |__/ |___ [__  [__  
%s | |      |  | |__/ |__/ |  \ |___ ___] ___] 

           %s•%s•%s• %sAldi Bachtiar Rifai %s•%s•%s•
"""%(O,O,O,M,K,H,P,M,K,H)

def ___main___():
	os.system("clear")
	print(__logo__)
	with requests.Session() as ses:
		try:
			j = ses.get("https://ipapi.co/json/").json()
			print("%s╭─[%s•%s] %sIP Anda     %s:%s %s"%(O,P,O,P,O,H,j["ip"]))
			print("%s├─[%s•%s]────────────────────────────────────"%(O,P,O))
			print("%s├─[%s•%s] %sNegara      %s:%s %s"%(O,P,O,P,O,H,j["country_name"]))
			print("%s├─[%s•%s] %sKota        %s:%s %s"%(O,P,O,P,O,H,j["city"]))
			print("%s├─[%s•%s] %sProvinsi    %s:%s %s"%(O,P,O,P,O,H,j["region"]))
			print("%s├─[%s•%s]────────────────────────────────────"%(O,P,O))
			print("%s├─[%s•%s] %sKode Negara %s:%s %s"%(O,P,O,P,O,H,j["country_calling_code"]))
			print("%s├─[%s•%s] %sMata Uang   %s:%s %s"%(O,P,O,P,O,H,j["currency_name"]))
			print("%s├─[%s•%s] %sBahasa      %s:%s %s"%(O,P,O,P,O,H,j["languages"]))
			print("%s├─[%s•%s]────────────────────────────────────"%(O,P,O))
			print("%s├─[%s•%s] %sPopulasi    %s:%s %s"%(O,P,O,P,O,H,j["country_population"]))
			print("%s├─[%s•%s] %sOrganisasi  %s:%s %s"%(O,P,O,P,O,H,j["org"]))
			print("%s├─[%s•%s] %sTime Zone   %s:%s %s"%(O,P,O,P,O,H,j["timezone"]))
			print("%s├─[%s•%s]────────────────────────────────────"%(O,P,O))
			print("%s╰─[%s•%s] %sWebsite     %s:%s https://ipapi.co \n"%(O,P,O,P,O,H))
			input("  %s[%s•%s] %sKeluar"%(O,P,O,P))
		except Exception as e:
			print("  "+O+"["+M+"!"+O+"] "+P+"Error "+O+":"+M+" "+str(e)) 
			input("\n  %s[%s•%s] %sKembali "%(O,P,O,P))
			___main___()

___main___()
