from sqlalchemy.orm import Session
from app.repositories.post_repository import post_repository
from app.schemas.post_schema import PostCreate, PostUpdate
from app.exceptions import PostNotFoundException

class PostService:
    def create_post(self, db: Session, data: PostCreate):
        return post_repository.create(db, data)

    def get_post(self, db: Session, post_id: int):
        post = post_repository.get_by_id(db, post_id)
        if not post:
            raise PostNotFoundException(post_id)
        return post

    def get_posts(self, db: Session, skip: int, limit: int):
        return post_repository.get_all(db, skip, limit)

    def update_post(self, db: Session, post_id: int, data: PostUpdate):
        post = post_repository.get_by_id(db, post_id)
        if not post:
            raise PostNotFoundException(post_id)
        return post_repository.update(db, post, data)

    def delete_post(self, db: Session, post_id: int):
        post = post_repository.get_by_id(db, post_id)
        if not post:
            raise PostNotFoundException(post_id)
        post_repository.delete(db, post)

post_service = PostService()