def get_user_role(user):
    if user["role"] == "admin" or user["role"] == "moderator":
        return "privileged"
    return "regular"
