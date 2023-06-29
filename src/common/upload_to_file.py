import uuid
from .translit import get_english_translit


def user_avatar(instance, filename: str) -> str:
    user_full_name = get_english_translit(instance.get_full_name())
    filename: str = f'{uuid.uuid4().hex}.{filename.split(".")[-1]}'
    return f"users/{user_full_name}/avatars/{filename}"
