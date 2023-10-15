from fastapi import FastAPI
from app.api import initialize_api

app = FastAPI()
initialize_api(app)

if __name__ == '__main__':
    print("Hello!@@!")
    