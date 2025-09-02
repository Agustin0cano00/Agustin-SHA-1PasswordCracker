import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Abrir archivo de contraseñas comunes
    with open("top-10000-passwords.txt", "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f]

    # Si se usan salts, leer archivo de salts
    salts = []
    if use_salts:
        with open("known-salts.txt", "r", encoding="utf-8") as f:
            salts = [line.strip() for line in f]

    # Caso sin salts
    if not use_salts:
        for password in passwords:
            hashed = hashlib.sha1(password.encode("utf-8")).hexdigest()
            if hashed == hash:
                return password

    # Caso con salts
    else:
        for password in passwords:
            for salt in salts:
                # Salt + password
                combo1 = hashlib.sha1((salt + password).encode("utf-8")).hexdigest()
                if combo1 == hash:
                    return password
                # Password + salt
                combo2 = hashlib.sha1((password + salt).encode("utf-8")).hexdigest()
                if combo2 == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
