from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This is our "database" for now (just a list in memory)
todos = []

# This defines what a Todo looks like
class Todo(BaseModel):
    id: int
    title: str
    done: bool = False

# Get all todos
@app.get("/todos")
def get_todos():
    return todos

# Get one todo
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}

# Create a todo
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

# Update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    return {"error": "Todo not found"}

# Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted"}
    return {"error": "Todo not found"}