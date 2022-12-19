class PostData:
    def __init__(self, post_id, user_id, title, body):
        self.id = post_id
        self.user_id = user_id
        self.title = title
        self.body = body

    @classmethod
    def from_json(cls, **kwargs):
        return cls(post_id=kwargs['id'], user_id=kwargs['user_id'], title=kwargs['title'], body=kwargs['body'])

    def is_valid_response(self):
        try:
            assert self.id is not None
            assert self.user_id is not None
            assert self.title is not None
            assert self.body is not None
            return True
        except AssertionError:
            return False

