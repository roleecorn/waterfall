import sqlite3

dbname = 'psg'
# 連線到 SQLite 資料庫
conn = sqlite3.connect(f'{dbname}.db')
cursor = conn.cursor()

# 新增欄位 ver，並設定初始值為 0
qry = f'''
      ALTER TABLE {dbname}
      ADD COLUMN ver INTEGER DEFAULT 0
      '''
cursor.execute(qry)

# 提交變更並關閉連線
conn.commit()
conn.close()
