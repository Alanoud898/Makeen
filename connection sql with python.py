import pyodbc
# 1. Establish a connection with a Microsoft SQL Server database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-LI4G1EA\MSSQLSS;'
                      'Database=TMS;'
                      'Database=productDB;'
                      'Trusted_Connection=yes;'
                      )
conn.autocommit=True
cursor = conn.cursor()
# cursor.execute('SELECT TOP 5 * FROM db.booKTopic')
# for i in cursor:
#         print(i)
conn.commit()

#Q2:
#curser.execute("creat database Alanoud")
#3
cursor.execute('''
                INSERT INTO bookTopic (tp_bkid, tb_desc)
                VALUES
                (1003,'SQL')
                ''')
conn.commit()
#Q5:
retrieve = "Select bk_totalCopies AS average from book;"
# Execute the queries
cursor.execute(retrieve)
rows = cursor.fetchall()
total=0
for i in rows:
    total=total + i[0]
avg=total/len(rows)
print("Average totalCopies:,avg")
#committing the connection then closing it.
conn.commit()
cursor.close()
conn.close()

#Q6:
import statistics

 cursor.execute('SELECT bk_totalCopies FROM book')
    # Fetch the results
 rows = cursor.fetchall()

    # Convert the rows to a list of integers
 integer_rows = []
    for row in rows:
        integer_rows.append(int(row[0]))

    # Calculate the sum of the integers
    sum_num = sum(integer_rows)

    # Calculate the mean 
    mean = statistics.mean(integer_rows)
    print("The mean of totalCopies of book table is ", mean)
    
    
    
    #standard devision
    std_=statistics.stdev(integer_rows)
    print("The standard deviation  of totalCopies of book table is",std_)
