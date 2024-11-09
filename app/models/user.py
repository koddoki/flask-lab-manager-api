from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from bson import ObjectId


class User:
    def __init__(self, username, name, cpf, user_id, password, email, phone=None, roles=None):
        self.username = username
        self.name = name
        self.cpf = cpf
        self.user_id = user_id
        self.password = generate_password_hash(password)
        self.email = email
        self.phone = phone
        self.roles = roles if roles else ['admin', 'teacher']
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.active = True

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        # Prepara os dados para salvar no MongoDB
        return {
            "username": self.username,
            "name": self.name,
            "cpf": self.cpf,
            "user_id": self.user_id,
            "password": self.password,
            "email": self.email,
            "phone": self.phone,
            "roles": self.roles,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "active": self.active,
        }

    @staticmethod
    def from_dict(data):
        # Carrega um usuário a partir de um dicionário (útil para leitura do MongoDB)
        user = User(
            username=data['username'],
            name=data['name'],
            cpf=data['cpf'],
            user_id=data['user_id'],
            password=data['password'],  # Assume senha já criptografada para evitar conflito
            email=data['email'],
            phone=data.get('phone'),
            roles=data.get('roles', ['admin', 'teacher'])
        )
        user.created_at = data.get('created_at', datetime.utcnow())
        user.updated_at = data.get('updated_at', datetime.utcnow())
        user.active = data.get('active', True)
        return user

    def update(self, data):
        # Atualiza os campos e a data de atualização
        for key, value in data.items():
            if hasattr(self, key) and key != 'user_id':  # Ignora o ID de usuário
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()

    def __repr__(self):
        return f"<User {self.username}>"
