from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
  summary: str

first_task = Task(summary="first_task")

second_task = Task(summary="second_task")

tasks = {
    0: first_task,
    1: second_task 
}



@app.post("/tasks")
def create_new_task(task: Task):
    id = len(tasks)
    tasks[id] = task
    return {"id" : id, "task" : task, "action": "created"}

@app.get("/")
def read_root():
    return {"Service": "Task Manager changed"}

@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.get("/task/{id}")
def get_task_by_id(id):
    return tasks[int(id)]

@app.put("/tasks/{id}")
def update_task(id: int, task: Task):
    tasks[id] = task
    return {"id" : id, "task" : task, "action": "updated"}

@app.delete("/tasks/{id}")
def delete_task_by_id(id: int):
    copy_task = tasks[id]
    del tasks[id]
    return {"id" : id, "task" : copy_task, "action" : "deleted"}

@app.delete("/tasks")
def delete_all_tasks():
    global tasks
    tasks = {}
    return {"action" : "deleted all tasks"}

