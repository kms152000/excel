import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook("test.xlsx")
ws = wb.active  #활성화 되어있는 시트 설정


#Cell data 읽기

data1 = ws.cell(row=1, column=2).value
print(data1)

data2 = ws["A1:C3"]
for data in data2:
	for cell_data in data:
		print(cell_data.value, end=" ") 


#Cell data 쓰기
wa = wb["sheet2"]


#Cell data 삭제하기