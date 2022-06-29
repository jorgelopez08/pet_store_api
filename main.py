import uvicorn

if __name__ == '__main__':
    uvicorn.run("pet_store.app:app", host='0.0.0.0', port=8000, reload=False)