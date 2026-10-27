def register_user(name, age, email):
    if not name:
        return {"status": "no name"}
    if age is None:
        return {"status": "no age"}
    if age < 18:
        return {"status": "too young"}
    if not email:
        return {"status": "no email"}
    if "@" not in email or '.' not in email:
        return {"status": "invalid email"}
    return {"status": "ok"}
