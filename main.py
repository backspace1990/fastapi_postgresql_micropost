from fastapi import FastAPI


description = """
                try.ai@yandex.ru 🚀
                
                ## POST
                
                В сервисе должно быть реализовано REST API, 
                принимающее на вход POST запросы с содержимым вида {"questions_num": integer}
                
                ## Users
                                
                Реализовать на Python3 простой веб сервис (с помощью FastAPI или Flask, например)
                После получения запроса сервис, в свою очередь, запрашивает с публичного API 
                (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное 
                в полученном запросе количество вопросов.
            """

app = FastAPI(
    title="Python3 простой веб сервис",
    description=description,
    version="0.0.1",
    contact={
        "name": "Умит",
        "url": "umut90asan@gmail.com",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)
