from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()



@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"

@app.get("/user/{us_id}")
async def user_id(us_id: int = Path(ge=1, le=100, description="Enter User ID", example="5")) -> str:
    return f"Вы вошли как пользователь № {us_id}"

@app.get("/user/{username}/{age}")
async def name_and_age(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                       age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    return f"Информация о пользователе. Имя: {username}, Возраст {age}. "


@app.get("/")
async def root():
    return "Главная страница"