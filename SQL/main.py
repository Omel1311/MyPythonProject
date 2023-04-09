import pymysql
from config import host, user, password, db_name

# создаем обьект класса pymysql
try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        #cursorclass=pymysql.cursors.DictCursor)
        cursorclass = pymysql.cursors.Cursor)
    print('successfully connected...')
    print('#'*30)

    try:
        '''
         # создать таблицу в  mysql
        with connection.cursor() as cursor:
            create_table = "create table test22(id int primary key, name varchar(20));"
            cursor.execute(create_table)
            print('create_table succsesfully')

        '''
        '''
        # вставить данные в таблицу в  mysql
        with connection.cursor() as cursor:
            insert_table = "insert into test33 values(5, 'lanna');"
            cursor.execute(insert_table)
            connection.commit()
            print('insert Table succsesfully')
        
        '''

        '''
        # создать базу данных в mysql
        with connection.cursor() as cursor:
            create_db = "create database python_sql"
            cursor.execute(create_db)
            connection.commit()
            print('create db succsesfully')
        '''
        '''
        # посмотреть даитабейсы в mysql
        with connection.cursor() as cursor:
            cursor.execute('show databases')
            for db in cursor:
                print(db)
        '''
         # посмотреть таблицы в базе данных
        with connection.cursor() as cursor:
             cursor.execute('show tables')
             for t in cursor:
                 print(t)

    finally:
        connection.close()


except Exception as ex:
    print('Connection refused...')
    print(ex)



