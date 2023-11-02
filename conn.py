import mysql.connector


conexion = mysql.connector.connect(user = 'root', 
                                   password = 'admin',
                                   host = 'localhost',
                                   database = 'PRODUCTO',
                                   port = '3306')

cursor = conexion.cursor()

    