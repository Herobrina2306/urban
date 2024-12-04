from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1':'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_dict() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=2, max_length=15, description="Enter name", example='Sasha')],
                      age: Annotated[int, Path(ge=16, le=120, description='Enter age', example='25')]) -> str:
    new_id = str(int(max(users, key=int)) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f'User {new_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path( description="Enter id", example='5')],
                      username: Annotated[str, Path(min_length=2, max_length=15, description="Enter name", example='Sasha')],
                      age: Annotated[int, Path(ge=16, le=120, description='Enter age', example='25')]) -> str:
    users[user_id] = f'Имя: {username}, возраст {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path( description="Enter id", example='5')]) -> str:
    users.pop(str(user_id))
    return f'User {user_id} is delete'