import sqlite3

# 建立與資料庫的連線
conn = sqlite3.connect('eddiebauer.db')
cursor = conn.cursor()

# 執行SQL語句，將欄位的所有資料加上.jpg
cursor.execute("UPDATE eddiebauer SET imgcode = imgcode || '.jpg'")

# 提交更改
conn.commit()

# 關閉連線
conn.close()
