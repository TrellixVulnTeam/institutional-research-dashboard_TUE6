## Oracle Database 11g Enterprise Edition

## SQL Developer

```
狀態 : 失敗 -測試失敗: Listener refused the connection with the following error:ORA-12505, TNS:listener does not currently know of SID given in connect descriptor
```

解決：SID 名稱不正確

## SQL Reference

### Database version

```sql
SELECT * FROM v$version;
```


### Get list of all tables

```sql
SELECT table_name FROM all_tables;
SELECT COUNT(table_name) FROM all_tables;

-- FROM user_tables
-- FROM dba_tables
```

[ALL_TAB_COLUMNS](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2103.htm#REFRN20277)

```sql
SELECT * FROM all_tab_columns;
SELECT * FROM all_constraints;

```





### Reference

http://blog.darkthread.net/post-2011-06-18-get-oracle-schema-info.aspx

https://stackoverflow.com/questions/22298005/how-to-find-schema-name-in-oracle-when-you-are-connected-in-sql-session-using
