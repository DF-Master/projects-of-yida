def is_contain_English(check_str):
    for ch in check_str:
        if ch in set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"):
            return (True)

    return False


print(is_contain_English('a'))
