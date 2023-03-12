import requests
import os
import certifi
import sys
import locale
from urllib.request import urlopen
from openpyxl import load_workbook
import json

# codirovka = 'C:\Windows\System32\chcp 65001'
# os.system(codirovka)
# print(sys.getfilesystemencoding())
# print(locale.getpreferredencoding())
headers = {"User-Agent": "Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/ 49.0.2623.110 YaBrowser / 16.4.1.8564 Safari/537.36",
		   'Content-Type': 'application/json',
		   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


# url = 'https://rosreestr.gov.ru/fir_lite_rest/api/gkn/fir_object/42:30:0415002:361'



# with requests.get(url, headers=headers, stream=True, timeout=600) as r:
#     print(r)
# print(certifi.where())


# r = requests.get(url, headers=headers, verify="CertBundle.pem")
# print(r)
# print(r.text)
# print(r.cookies)

# r = requests.get(url, headers=headers, verify="CertBundle.pem")
# print(type(r))
# i = 0
# print(r.json())
# for data in r.json():
# 	print(data)
# 	i += 1
# print(i)

#---------------------поиск по адресу и запись в файл
# wb = load_workbook('C:/Users/18098/OneDrive/Desktop/Поиск кад номера/list.xlsx')
# sheet = wb.active
# for i in range(1, 271):
# 	ul = sheet[i][4].value
# 	number = sheet[i][6].value
# 	url = 'https://rosreestr.ru/fir_lite_rest/api/gkn/address/fir_objects?macroRegionId=132000000000&regionId=132431000000&street='+ str(ul) + '&house=' + str(number)
# 	print(url)
# 	r = requests.get(url, headers=headers, verify="CertBundle.pem")
# 	print(ul, number)
# 	for a in r.json():
# 		print(a)
# 		with open('C:/Users/18098/OneDrive/Desktop/Поиск кад номера/1.txt', 'a') as file:
# 			for key, value in a.items():
# 				file.write(f'{key}, {value}')
# 			file.write('\n')

#---------------------сведения ГКН по кад номеру и запись в файл
wb = load_workbook('C:/Users/18098/OneDrive/Desktop/Поиск кад номера/list.xlsx')
sheet: object = wb.active
for i in range(2, 441):
	cadnum = sheet[i][2].value
	url = 'http://rosreestr.ru/fir_lite_rest/api/gkn/fir_object/' + str(cadnum)
	print(cadnum)
	r = requests.get(url, headers=headers, verify="CertBundle.pem")
	# разбираем respons ответ в формате json это словарь. из словаря достаем пару ключа parcelData, а из него rightsReg
	a = r.json().get("parcelData")
	rightsReg = a.get("rightsReg")
	# аналогично из словаря достаем пару ключа objectData, а из него removed (0 на учете, 1 снят с учета)
	b = r.json().get("objectData")
	objectType = b.get('objectType')
	objectName = b.get('objectName')
	removed = b.get('removed')
	addressNote = b.get('addressNote')
	print(objectType)
	print(objectName)
	print(addressNote)
	print(rightsReg)
	print(removed)
	# with open('C:/Users/18098/OneDrive/Desktop/Поиск кад номера/parcel.txt', 'a') as file:
	# 	file.write(r.text)
	# 	file.write('\n')
	sheet[i][6].value = objectType
	sheet[i][7].value = objectName
	sheet[i][8].value = addressNote
	sheet[i][9].value = rightsReg
	sheet[i][10].value = removed
	wb.save('C:/Users/18098/OneDrive/Desktop/Поиск кад номера/list.xlsx')
