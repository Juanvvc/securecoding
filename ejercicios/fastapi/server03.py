from fastapi import FastAPI
import sqlite3
import bcrypt

app = FastAPI()


@app.get("/create")
async def create(name, password):
    conn = sqlite3.connect('users.db')
    sql = 'INSERT INTO users(name,password) VALUES(?,?)'
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cur = conn.cursor()
    cur.execute(sql, (name, hashed))
    conn.commit()
    return {"message": f"I created user {name}"}

