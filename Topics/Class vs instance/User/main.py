class User:
    # create the class attributes
    n_active = 0
    users = []

    # create the __init__ method
    def __init__(self, is_active, user_name):
        self.active = is_active
        self.user_name = user_name
