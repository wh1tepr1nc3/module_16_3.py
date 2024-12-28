# uvicorn module_16_3:app --reload
# http://127.0.0.1:8000/docs
from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


# @app.get("/")
# async def main_page() -> dict:
#     return {"message": "Главная страница"}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str,
            Path(max_length=30, description='Введите имя', examples='Vasiliy')],
        age: Annotated[int,
            Path(le=120, description='Введите возраст', examples='20')]
) -> str:
    new_user_id = str(int(max(users, key=int)) + 1)
    users[new_user_id] = f'Имя: {username}: Возраст: {age}'
    return f'Пользователь {new_user_id} зарегестрирован'


@app.put('/user/{user_id}/{username}/{age}')
async def put_users(
        user_id: int,
        username: Annotated[str,
        Path(max_length=30, description='Введите свое имя', examples='Vasiliy')],
        age: Annotated[int,
        Path(ge=18, le=120, description='Введите возраст', examples='24')]
) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь {user_id} обновлен'


@app.delete('/user/{user_id}')
async def del_users(user_id: Annotated[str,
Path(description='Введите ID для удаления', examples='1')]) -> str:
    users.pop(user_id)
    return f'Пользователь {user_id} удален'
