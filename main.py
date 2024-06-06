from typing import Union

from fastapi import FastAPI

app = FastAPI()

tasks = {
    1: {"Summary": "First task"},
    2: {"Summary": "Second task"}
}

@app.get("/")
def read_root():
    return {"Service": "Task Manager changed"}

@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.get("/task/{task_id}")
def get_task_by_id(task_id):
    return tasks[int(task_id)]
