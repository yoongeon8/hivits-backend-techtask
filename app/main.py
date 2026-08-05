from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.database import Base, engine
from app.routers import post_router
from app.exceptions import PostNotFoundException

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HiVITS Backend")

app.include_router(post_router.router)

@app.exception_handler(PostNotFoundException)
def post_not_found_handler(request: Request, exc: PostNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"detail": f"Post with id {exc.post_id} not found"},
    )