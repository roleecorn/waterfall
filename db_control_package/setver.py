import sqlite3

# 連線到 SQLite 資料庫
dbname = 'psg'
conn = sqlite3.connect(f'{dbname}.db')
cursor = conn.cursor()

# 更新符合條件的資料
qry = f'''
      UPDATE {dbname}
      SET ver = 100
      WHERE gender = 0
      '''
cursor.execute(qry)

# 提交變更並關閉連線
conn.commit()
conn.close()
