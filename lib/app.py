from  insert import  insert,tratar_campos_vazios

arq_csv = open('../data/_variaveis_climaticas.csv','r')

index = 0

for line in arq_csv.readlines():
    index+=1
    print("---->LINHA {}".format(index))
    line = line.replace(',','.')
    line = line.replace('"','')
    line = line.replace('\n','')
    lista = line.split(";")
    
    # valida nulos
    tratar_campos_vazios(lista)

    print(lista)
    insert(data=lista[0], it=lista[1], tmax=lista[2], tmed=lista[3], tmin=lista[4], ur=lista[5], vv=lista[6], vvfinal=lista[7])
  