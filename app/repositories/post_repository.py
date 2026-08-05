from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.schemas.post_schema import PostCreate, PostUpdate

class PostRepository:
    def create(self, db: Session, data: PostCreate) -> Post:
        post = Post(title=data.title, content=data.content)
        db.add(post)
        db.commit()
        db.refresh(post)
        return post

    def get_by_id(self, db: Session, post_id: int) -> Post | None:
        return db.query(Post).filter(Post.id == post_id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 20) -> list[Post]:
        return db.query(Post).offset(skip).limit(limit).all()

    def update(self, db: Session, post: Post, data: PostUpdate) -> Post:
        if data.title is not None:
            post.title = data.title
        if data.content is not None:
            post.content = data.content
        db.commit()
        db.refresh(post)
        return post

    def delete(self, db: Session, post: Post) -> None:
        db.delete(post)
        db.commit()

post_repository = PostRepository()