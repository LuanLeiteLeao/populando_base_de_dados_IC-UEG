from connection import mycursor,mydb

def insert(data, it, tmax, tmed, tmin, ur, vv, vvfinal):
    sql = "INSERT INTO \
           variaveis_climaticas \
           (`DATA`, `IT`, `TMAX`, `TMED`, `TMIN`, `UR`, `VV`, `Vvfinal`) \
           VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
    
    val = (data, it, tmax, tmed, tmin, ur, vv, vvfinal)
    mycursor.execute(sql, val)
   
    mydb.commit()
    
    print(mycursor)
    print(mycursor.rowcount, "record inserted.")

def tratar_campos_vazios(lista):
    tamanho = len(lista)

    for index in range(tamanho):
        if lista[index] == '' or lista[index] == 'null' :
            print("trantando nulos")
            lista[index] = None


# insert()