import dbcreds
import mariadb

conn = None
cursor = None

try:
    conn = mariadb.connect(
                            user=dbcreds.user,
                            password=dbcreds.password,
                            host=dbcreds.host,
                            port=dbcreds.port,
                            database=dbcreds.database)
    cursor = conn.cursor()
    print("Enter username: ")
    username = input()
    print("Enter blog here: ")
    content = input()

    cursor.execute("INSERT INTO command_line_blog(content) VALUES (?)")
    cursor.execute("SELECT content FROM command_line_blog WHERE id=?,[id,])")
   
    conn.commit()
    print("Blog successfully posted")
    cursor.close()
    conn.close()

except mariadb.DataError:
    print("something went wrong with your data")
except mariadb.OperationalError:
    print("opertational error on the connection")
except mariadb.ProgrammingError:
    print("apparently, you don't know how to code")
except mariadb.IntegrityError:
    print("Error with DB integrity. most likelu constraint failure")
except:
    print("Something went wrong")