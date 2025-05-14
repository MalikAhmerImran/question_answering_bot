from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user_router


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Adjust this list to restrict as needed.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods. Adjust as needed.
    allow_headers=["*"],  # Allows all headers. Adjust as needed.
)


app.include_router(user_router)

@app.get("/")
async def home():
    return {
        "message": "Welcome to the Application. Access the documentation at /docs or /redoc."
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, port=5000)