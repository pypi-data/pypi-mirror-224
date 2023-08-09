# -*- coding:utf-8 -*-
"""
@Time : 2023/3/25
@Author : skyoceanchen

@TEL: 18916403796
@File : mdb_operation.py 
@PRODUCT_NAME : PyCharm 
"""

import pyodbc  # pyodbc-4.0.39

p_path = r'E:\Programs\FBG86002-客户端2.9.2带时间戳\客户端带时间戳\历史记录\报警记录.mdb'
# p_path = r'E:\Project\报警记录.mdb'
driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
# 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + p_path + ';PWD=007'
conn = pyodbc.connect(f'Driver={driver};DBQ={p_path}')
cur = conn.cursor()
# 打印表名
tables = []
for table_name in cur.tables(tableType='TABLE'):
    print(table_name.table_name)
    tables.append(table_name.table_name)
print(tables)
for table in tables:
    sql = "SELECT * FROM " + f'{table}'  # 取表 ActualValues_T
    cur.execute(sql)
    alldata = cur.fetchall()  # 取 ActualValues_T 所有数据
    total_rows = len(alldata)
    total_cols = len(alldata[0])
    print("****************Begin to process\"表:ActualValues_T\"****************")
    print("\"表:%s\"总行数 = %d" % ('ActualValues_T', total_rows))
    print("\"表:%s\"总列数 = %d" % ('ActualValues_T', total_cols))
    print(type(alldata))
    print(alldata)

    # dfTable = pd.read_sql(f"select * from '{table}'", cnxn)
conn.close()  # 关闭数据库
