from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "52.2.83.96"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_seguros2"  

# Get all claims
@app.get("/claims")
def get_claims():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM siniestros2")
    result = cursor.fetchall()
    mydb.close()
    return {"claims": result}

# Get a claim by ID
@app.get("/claims/{id}")
def get_claim(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM siniestros2 WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"claim": result}

# Add a new claim
@app.post("/claims")
def add_claim(item: schemas.Claim):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    poliza_id = item.poliza_id
    descripcion = item.descripcion
    monto = item.monto
    cursor = mydb.cursor()
    sql = "INSERT INTO siniestros2 (poliza_id, descripcion, monto) VALUES (%s,  %s, %s)"
    val = (poliza_id, descripcion, monto)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Claim added successfully"}

