import myparser

fileParser = myparser.MyParser()

def create(data):
    query_string=f"INSERT INTO dimonds(carat, cut, color, clarity, depth, table, price, x, y, z) VALUES {data['carat'],data['cut'],data['color'],data['clarity'],data['depth'],data['table'],data['price'],data['x'],data['y'],data['z']}"
    return query_string 

def get(data):
    data=[data]   
    cat=data[0]
    value=data[1]
    query_string=f"SELECT * FROM diamonds WHERE {cat} ={value}"
    return query_string 

def getAll(): 
    query_string=f"SELECT * FROM diamonds"
    return query_string 

def update(data):
    data=[data]
    cat=data[0]
    oldvalue=data[1]
    newvalue=data[2]
    query_string=f"UPDATE diamonds SET{cat} ={newvalue} WHERE {cat} ={oldvalue}"
    return query_string 

def delete(data):
    data=[data]
    cat=data[0]
    value=data[1]
    query_string=f"DELETE FROM diamonds WHERE {cat} ={value}"
    return query_string         