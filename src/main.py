from fastapi import FastAPI

from .routes.agent_routes import router as agent_router

app = FastAPI()

app.include_router(agent_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
