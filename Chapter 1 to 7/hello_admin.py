usernames = ["naval", "nassim taleb", "rc", "admin","sherlock homes"]


if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging again.")
else:
    print("We need to find some users.")