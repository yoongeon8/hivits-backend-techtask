from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.post_schema import PostCreate, PostUpdate, PostResponse
from app.services.post_service import post_service

router = APIRouter(prefix="/posts", tags=["posts"])

# Create
@router.post("", response_model=PostResponse, status_code=201)
def create_post(data: PostCreate, db: Session = Depends(get_db)):
    return post_service.create_post(db, data)

# Read - 단건 조회
@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return post_service.get_post(db, post_id)

# Read - 목록 조회
@router.get("", response_model=list[PostResponse])
def get_posts(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return post_service.get_posts(db, skip, limit)

# Update
@router.patch("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, data: PostUpdate, db: Session = Depends(get_db)):
    return post_service.update_post(db, post_id, data)

# Delete
@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post_service.delete_post(db, post_id)