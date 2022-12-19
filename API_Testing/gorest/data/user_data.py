class UserData:
    def __init__(self, user_id, name, email, gender, status):
        self.id = user_id
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs['id'], kwargs['name'], kwargs['email'], kwargs['gender'], kwargs['status'])

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
