import pandas

reptPath = 'C:\\SUROS_BI\\Panorays_Reports_220810A\\'
excelFile = 'DBsourceData_220810.xlsx'
baseData = pandas.read_excel(excelFile, sheet_name=0, usecols=[0,19])
baseHead = ['DB編號', 'URL']


#input search url to get dbNoList
searchURL = "howweih"


dbNoListURL = []
for i in range(0,1902): #pandas已預設第一列為Head，故從0開始。若Excel資料無標題，則需給Head = None指令。
	cellValue = baseData[baseHead[1]].values[i]
	if searchURL.lower() in str(cellValue).lower():
		dbNo = str(baseData[baseHead[0]].values[i]).strip()
		if dbNo not in dbNoListURL:
			dbNoListURL.append(dbNo)
			print(i)
	i+=1

print(dbNoListURL) 