from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/create")
async def create(name, password):
    conn = sqlite3.connect('users.db')
    sql = f'INSERT INTO users(name,password) VALUES("{name}","{password}")'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return {"message": f"I created user {name}"}
