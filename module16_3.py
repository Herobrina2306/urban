from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_task(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="Task not found")


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=2, max_length=15, description="Enter name", example='Sasha')],
        age: Annotated[int, Path(ge=16, le=120, description='Enter age', example='25')]) -> dict:
    new_user = User(id=len(users)+1, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(description="Enter id", example='5')],
                      username: Annotated[
                          str, Path(min_length=2, max_length=15, description="Enter name", example='Sasha')],
                      age: Annotated[int, Path(ge=16, le=120, description='Enter age', example='25')]) -> str:
    try:
        user = users[user_id - 1]
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(description="Enter id", example='5')]) -> str:
    try:
        us = users.pop(user_id+1)
        return us
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.get('/', response_class=HTMLResponse)
async def all_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})
