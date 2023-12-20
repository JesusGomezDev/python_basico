lista = [1, 2, 3, 4, '5', 'hola', False]

users = [
    {
        'name': 'José',
        'username': 'josé777',
        'email': 'josé777@correo.com',
    },
    {
        'name': 'Juan',
        'username': 'juan777',
        'email': 'juan777@correo.com',
    },
    {
        'name': 'Pepito',
        'username': 'pp777',
        'email': 'pep777@correo.com',
    },
    {
        'name': 'Ana',
        'username': 'Ana777',
        'email': 'AnA777@correo.com',
    },
]
# print(len(lista))

for i in range(len(users)):
    print(users[i]['name'])
    print(users[i]['email'])

for user in users:
    print(user['name'])
    print(user['email'])