def hash_email(email: str):
    import hashlib
    return hashlib.sha256(email.encode()).hexdigest()
