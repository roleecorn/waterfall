import sqlite3
import re

# 連接到您的資料庫
conn = sqlite3.connect('html5upphantom\images\hackett\hackett.db')
c = conn.cursor()

# # 獲取含有貨幣內容的列
# c.execute("SELECT * FROM hackett WHERE oriprice LIKE 'NT%'")

# # 遍歷列並修正貨幣內容
# for row in c.fetchall():
#     price = row[2] # 假設price欄位是第二個欄位
#     new_price = re.sub('[^\d.]', '', price) # 使用正則表達式刪除非數字和小數點的字符
#     imgcode=row[1]
#     c.execute("UPDATE hackett SET oriprice = ? WHERE imgcode = ?", (new_price, imgcode)) # 將修正後的值更新到資料庫
c.execute("UPDATE hackett SET oriprice = oriprice * 1000")
# 提交更改
conn.commit()

# 關閉連接
conn.close()