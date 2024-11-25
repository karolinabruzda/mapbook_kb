users: list = [
    {'name': 'Karolina', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Poznań'},
    {'name': 'Szymon z wąsem', 'posts': 5, 'city': 'Toruń'},
    {'name': 'Szymon', 'posts': 7, 'city': 'Szczecin'},
    {'name': 'Patrycja', 'posts': 9, 'city': 'Warszawa'},
    {'name': 'Patrycja', 'posts': 3, 'city': 'Łódź'},
    {'name': 'Amelia', 'posts': 11, 'city': 'Toruń'},
    {'name': 'Kinga', 'posts': 4, 'city': 'Iława'},
    {'name': 'Dominik', 'posts': 2, 'city': 'Szczecin'},


]
#TODO please update user list

print(f'Witaj {users[0]['name']}!!')
for user in users[1:]:
    print(f'Twój znajomy {user['name']}, z miejscowości {user['city']} opublikował {user['posts']} postów')

# for idx, _ in enumerate(users[1:]):
#     print(f'Twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
