import pickle

def input_user_data():
    surname = input("vvedite familiu: ")
    passwords = {}
    
    for _ in range(6):
        s = input("vvedite nazvanie caita: ")
        password = input("vvedite parol: ")
        passwords[s] = password
    
    return surname, passwords

users = {}
for _ in range(7):
    surname, passwords = input_user_data()
    users[surname] = passwords

for user, passwords in users.items():
    avg_length = sum(len(p) for p in passwords.values()) / len(passwords)
    min_password_site = min(passwords, key=lambda x: len(passwords[x]))
    print(f"polzovatel: {user}, dlina paroley: {avg_length:.2f}, minimalnuy parol: {min_password_site}")

for user, passwords in users.items():
    seen_passwords = {}
    new_passwords = {}
    
    for s, password in passwords.items():
        if password in seen_passwords:
            new_passwords[s] = password + "_new" 
        else:
            new_passwords[s] = password
            seen_passwords[password] = True
    
    users[user] = new_passwords

facebook_users = {user: passwords for user, passwords in users.items() if passwords.get('Facebook', '').startswith('F')}
print("y gotorogo zaglavnay bykva:")
for user in facebook_users:
    print(user)

with open('data.pickle', 'wb') as f:
    pickle.dump(users, f)

with open('data.pickle', 'rb') as f:
    loaded_users = pickle.load(f)

print("dannue iz binarnogo fales:")
print(loaded_users)

