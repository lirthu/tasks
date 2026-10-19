DEFAULT_SETTINGS = {"theme": "light", "lang": "ru"}

def update_settings(new_settings):
    settings = DEFAULT_SETTINGS
    settings = settings | new_settings
    return settings

# Вызов 1
update_settings({"theme": "dark"})
# {'theme': 'dark', 'lang': 'ru'}

# Вызов 2
print(update_settings({}))  # что выведет?
# {'theme': 'light', 'lang': 'ru'}