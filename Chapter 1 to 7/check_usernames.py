current_users = ["Naval RAVIKANT", "Nassim taleb", "SHerlock homes", "Elon musk", "chandler bing"]
users_database =[user.lower() for user in current_users]
new_users = ["elon musk", "joy", "racheal","nassim taleb", "usman"]

for new_user in new_users:
    if new_user in users_database:
        print(f"{new_user} has already been used.")
    else:
        print(f"{new_user} is available.")