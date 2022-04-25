from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pet_store.endpoints import pets

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/', tags=['main'])
def index():
    return {"detail": "Welcome to the Pet Store API"}

app.include_router(
    pets.router,
    prefix='/pets'
)