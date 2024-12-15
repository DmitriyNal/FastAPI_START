from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Главная страница "}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "ВЫ вошли как администратор"}


@app.get("/user/{user_id}")
async def user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get('/user')
async def user_name(name: str, age: int) -> dict:
    return {"message": f'Имя: {name}, Возраст: {age} '}