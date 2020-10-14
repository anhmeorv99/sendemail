import xlrd
from xlwt import Workbook
import requests, re

wb1 = Workbook()
result = []
file_location = "/home/anhmeo/Downloads/gmail.xlsx"
wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)
row = 1
col = 0

data = []
# for rows in range(sheet.nrows - 1):
#     try:
#         # print(sheet.cell_value(rows + 1, 0) + '\t' + sheet.cell_value(rows + 1, 1))
#         item = {
#             "name": "Bot" + str(rows),
#             "password": sheet.cell_value(rows + 1, 1),
#             "phone_number": "0222222222",
#             "email": sheet.cell_value(rows + 1, 0)+"@gmail.com",
#             "token": sheet.cell_value(rows + 1, 3)
#         }
#         req = requests.post('http://192.168.140.240:30095/api/youtube_bot/', data=item)
#         print(req.status_code)
#         print("success ", item)
#     except Exception as e:
#         print(e)

req = requests.get("http://192.168.140.240:30095/api/youtube_bot")
for x in req.json():
    print(x, "\n")
