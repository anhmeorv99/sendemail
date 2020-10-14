# import requests, re
#
# req = requests.get("https://www.siteprice.org/website-worth/vnexpress.net")
#
# result = re.search('<span id="lblDailyPageviews" class="SiteDetailLabel">', req.text)
#
# result1 = req.text.split('<span id="lblDailyPageviews" class="SiteDetailLabel">')
# result2 = result1[1].split('</span>')
#
# print(result2[0])

import xlrd
from xlwt import Workbook
import requests, re

wb1 = Workbook()
sheet1 = wb1.add_sheet('Sheet1')
result = []
file_location = "/home/anhmeo/Downloads/data.xlsx"
wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)
row = 1
col = 0

for rows in range(sheet.nrows - 1):
    item = []
    domain = sheet.cell_value(rows + 1, 0).split('//')[1]
    sheet1.write(row, col, sheet.cell_value(rows + 1, 0))
    try:
        req = requests.get("https://www.siteprice.org/website-worth/" + domain)

        page_views = req.text.split('<span id="lblDailyPageviews" class="SiteDetailLabel">')

        page_views = page_views[1].split('</span>')[0]

        if page_views:
            sheet1.write(row, col + 1, page_views)
            row += 1
        else:
            sheet1.write(row, col + 1, '0')
            row += 1
        print('success : ' + domain)
    except Exception as e:
        sheet1.write(row, col + 1, '0')
        row += 1
        print('cant connect:' + domain)

wb1.save('result.xlsx')
