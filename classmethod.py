class Myclass:
    class_variable = 0

    @classmethod
    def my_class_method(cls):
        print("this is a class method")


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email  # Fixed: removed space after @
    
    @classmethod
    def create_user(cls, name, email):
        if not cls.validate_email(email):
            raise ValueError("Invalid email address")
        return cls(name, email)
    
    def __str__(self):  # Added: string representation method
        return self.name

# Example usage
user1 = User.create_user("John Doe", "hashir@truly.com")
print(user1)  # Output: John Doe