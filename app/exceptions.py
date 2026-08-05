class PostNotFoundException(Exception):
    def __init__(self, post_id: int):
        self.post_id = post_id