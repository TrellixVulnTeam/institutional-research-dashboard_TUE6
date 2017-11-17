## Oracle Database 11g Enterprise Edition 指南

## 資料庫管理工具 

### SQL Developer

```
狀態 : 失敗 -測試失敗: Listener refused the connection with the following error:ORA-12505, TNS:listener does not currently know of SID given in connect descriptor
```

解決：SID 名稱不正確，向 DBA 詢問正確名稱


## SQL 指令


[Documentation 11g Release 2 (11.2) Database Administration](https://docs.oracle.com/cd/E11882_01/nav/portal_4.htm)


### 資料庫版本

```sql
SELECT * FROM v$version;
```

### 資料庫內所有表格的資訊

Oracle 三個表視圖
* `dba_tables`: 系統內所有的表格訊息，需有 DBA 權限。
* `all_tables`: 當前用戶具權限的表格訊息（包括你自己名下的表格及其他用戶授權給你的表格）。
* `user_tables`: 當前用戶名下擁有的表格訊息。

```sql
SELECT table_name FROM all_tables;
SELECT COUNT(table_name) FROM all_tables;

-- FROM user_tables
-- FROM dba_tables
```

[ALL_TAB_COLUMNS](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2103.htm#REFRN20277)

[ALL_CONSTRAINTS](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1047.htm#REFRN20047)

`CONSTRAING_TYPE`
* `P`: Primary key
* `U`: Unique key
* `C`: Check constraint on a table
* `R`: Referential integrity

```sql
SELECT * FROM all_tab_columns C WHERE C.OWNER  = "SCHEMA NAME";
SELECT * FROM all_constraints C WHERE C.OWNER  = "SCHEMA NAME";
```

[DUAL Table](https://docs.oracle.com/cd/E11882_01/server.112/e41084/queries009.htm#SQLRF20036)

```sql
SELECT sysdate FROM DUAL;
SELECT sys_context( 'userenv', 'current_schema' ) FROM DUAL;
```

### 特定 Schema 下所有表格及欄位型別、長度、精準位數、NULLABLE、預設值

```sql
SELECT
  C.OWNER, C.TABLE_NAME, C.COLUMN_ID, C.COLUMN_NAME, 
  DATA_TYPE, DATA_LENGTH, DATA_PRECISION, DATA_DEFAULT, 
  NULLABLE, COMMENTS
FROM
  ALL_TAB_COLUMNS C JOIN ALL_TABLES T 
ON 
  C.OWNER = T.OWNER AND 
  C.TABLE_NAME = T.TABLE_NAME
LEFT JOIN ALL_COL_COMMENTS R ON
  C.OWNER = R.Owner AND 
  C.TABLE_NAME = R.TABLE_NAME AND 
  C.COLUMN_NAME = R.COLUMN_NAME
WHERE  
  C.OWNER  = "SCHEMA NAME"
ORDER BY C.TABLE_NAME, C.COLUMN_ID;
```

[ALL_COL_COMMENTS](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1039.htm#REFRN20040)

```sql



```




### 列出 Index

[ALL_INDEXES](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1109.htm#REFRN20088)

[ALL_IND_COLUMNS](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1103.htm#REFRN20084)

```sql
SELECT 
  I.TABLE_OWNER, I.TABLE_NAME, I.INDEX_NAME, I.INDEX_TYPE,
  I.UNIQUENESS, C.COLUMN_POSITION, C.COLUMN_NAME, C.DESCEND
FROM 
  ALL_INDEXES I JOIN ALL_IND_COLUMNS C
ON 
  I.TABLE_OWNER = C.TABLE_OWNER AND
  I.INDEX_NAME = C.INDEX_NAME
WHERE
  C.TABLE_OWNER = "SCHEMA NAME"
ORDER BY I.TABLE_NAME, I.INDEX_NAME, COLUMN_POSITION;
```

### 列出 Primary Key

[ALL_CONS_COLUMNS](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1045.htm#REFRN20045)

```sql
SELECT 
  C.OWNER, C.TABLE_NAME, D.POSITION, D.COLUMN_NAME  
FROM 
  ALL_CONSTRAINTS C JOIN ALL_CONS_COLUMNS D
ON
  C.OWNER = D.OWNER AND
  C.CONSTRAINT_NAME = D.CONSTRAINT_NAME
WHERE
  C.CONSTRAINT_TYPE = 'P' AND 
  C.OWNER = "SCHEMA NAME"
ORDER BY C.TABLE_NAME, D.POSITION;
```






## 參考

http://blog.darkthread.net/post-2011-06-18-get-oracle-schema-info.aspx

https://stackoverflow.com/questions/22298005/how-to-find-schema-name-in-oracle-when-you-are-connected-in-sql-session-using

---

## Python Client Cx_Oracle

1. 確認版本

* Python 3.6
* Oracle Database 11g Release 2 (11.2)

1. 安裝 cx_Oracle

```shell
$ pip install cs_Oracle
```

2. 安裝 Oracle Instant Client

[Oracle Instant Client](http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html)

3. 將 Oracle Instant Client
    * C:\Oracle\
    * 將目錄位置加進環境變數

3. 設定TNS 組態

```
<addressname> =
 (DESCRIPTION =
   (ADDRESS_LIST =
     (ADDRESS = (PROTOCOL = TCP)(Host = <hostname>)(Port = <port>))
   )
 (CONNECT_DATA =
   (SERVICE_NAME = <service_name>)
 )
)
```

  * addressname: TNS 名稱，自行命名
  * hostname: 資料庫的 IP 位置
  * port: 預設 1521
  * service_name: 資料庫全局 SID

4. 編輯完後以 TNSNAMES.ORA 命名，儲存至 C:\Oracle\network\admin
    * 將目錄位置加進環境變數

5. 測試連接

```python
import cx_Oracle

conn = cx_Oracle.connect("User Name", "Password", "IP/SID")

cursor = conn.cursor()

cursor.execute("SELECT * FROM test_table")
```


## 參考

http://www.oracle.com/technetwork/articles/dsl/python-091105.html

http://bhan0507.logdown.com/posts/1855591-oracle-x-python-how-to-use-python-oracle-database

