#users details
#regirter user
users_list=[]
def registerUsers(name):
 if name not in users_list:
  users_list.append(name)

#view users
def show_users():
 print(f"Users registered: {users_list}")

