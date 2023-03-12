import requests
import os
import certifi
import sys
import locale
from urllib.request import urlopen
import ssl

# codirovka = 'C:\Windows\System32\chcp 65001'
# os.system(codirovka)
# print(sys.getfilesystemencoding())
# print(locale.getpreferredencoding())
headers = {"User-Agent": "Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/ 49.0.2623.110 YaBrowser / 16.4.1.8564 Safari/537.36",
		   'Content-Type': 'application/json',
		   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


url = 'https://rosreestr.gov.ru/fir_lite_rest/api/gkn/fir_object/42:30:0415002:361'
# url = 'http://rosreestr.ru/api/online/fir_object/42:30:0415002:361'


# urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))

# os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(sys.argv[0]), certifi.where())
# os.environ['REQUESTS_CA_BUNDLE'] = "rosreestr.gov.ru.crt"
# print(os.environ['REQUESTS_CA_BUNDLE'])

# with requests.get(url, headers=headers, stream=True, timeout=600) as r:
#     print(r)
# print(certifi.where())

# param = {'macroRegionId': '140000000000'}

# r = requests.get(url, headers=headers, verify="CertBundle.pem")
# print(r)
# print(r.text)
# print(r.cookies)

r = requests.get(url, headers=headers, verify="CertBundle.pem")
print(type(r))
i = 0
print(r.json())
for data in r.json():
	print(data)
	i += 1
print(i)

