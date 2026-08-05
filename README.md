# 하이비츠 백엔드 기술 과제 : CRUD API 구현

## 실행 방법

1. 저장소 클론
   ```bash
   git clone https://github.com/[계정]/hivits-backend.git
   cd hivits-backend
   ```

2. 가상환경 생성 및 패키지 설치
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows는 venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. .env 파일 생성 (.env.example 참고)
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/hivits_db
   ```

4. 서버 실행
   \`\`\`bash
   uvicorn app.main:app --reload
   \`\`\`

5. http://localhost:8000/docs 접속

## 사용한 기술

- Python 3.x
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic (Validation)

## API 실행 예시

### 게시글 생성
```bash
curl -X POST http://localhost:8000/posts \\
  -H "Content-Type: application/json" \\
  -d '{"title": "제목", "content": "내용"}'
```

### 게시글 목록 조회
```bash
curl http://localhost:8000/posts
```

### 게시글 단건 조회
```bash
curl http://localhost:8000/posts/1
```

### 게시글 수정
```bash
curl -X PATCH http://localhost:8000/posts/1 \\
  -H "Content-Type: application/json" \\
  -d '{"title": "수정된 제목"}'
```

### 게시글 삭제
```bash
curl -X DELETE http://localhost:8000/posts/1
```