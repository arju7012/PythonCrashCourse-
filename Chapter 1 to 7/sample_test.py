def greet_user(names):
    """Greeting induvidual user from a list."""

    for name in names:
        print(f"Hello,{name.title()}")

usernames = ['arjun', 'nanditha', 'vishnu babi']
greet_user(usernames)