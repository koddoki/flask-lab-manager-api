from app.models import User


def create_user(data):
    try:
        user = User(
            username=data['username'],
            name=data['name'],
            cpf=data['cpf'],
            user_id=data['user_id'],
            email=data['email'],
            phone=data.get('phone'),
            roles=data.get('roles', ['admin', 'teacher'])
        )
        user.set_password(data['password'])
        user.save()
        return user.to_json()
    except Exception as e:
        return {'error': str(e)}


def get_user(user_id):
    user = User.objects(user_id=user_id).first()
    return user.to_json() if user else None


def get_all_users():
    return [user.to_json() for user in User.objects]


def update_user(user_id, data):
    user = User.objects(user_id=user_id).first()
    if not user:
        return None
    user.update(**data)
    return user.reload().to_json()


def delete_user(user_id):
    user = User.objects(user_id=user_id).first()
    if user:
        user.delete()
        return True
    return False
