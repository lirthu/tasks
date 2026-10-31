def get_driver_category(age, experience, has_license):
    if not has_license:
        return "Нет прав"
    if age < 18:
        return "Слишком молод"
    if experience < 3:
        return "Новичок"
    if age >= 25:
        return "Профессионал"
    return "Опытный"
