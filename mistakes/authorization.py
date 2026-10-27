def login1(user):
    if user is None:
        return "Пользователь не найден"
    if not user.get("active"):
        return "Неактивен"
    if user.get("banned"):
        return "Забанен"
    if user.get("password") != user.get("password_hash"):
        return "Неверный пароль"
    return "OK"

def login2(user):
    result = [
        (user is None, "Пользователь не найден"),
        (user.get('active'), "Неактивен"),
        (user.get("banned"), "Забанен"),
        ((user.get("password") != user.get("password_hash")), "Неверный пароль")
    ]
    for condition, message in result:
        if condition:
            return result
    return "OK"