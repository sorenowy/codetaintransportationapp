import hashlib
from random import randbytes
from fastapi import Request


def generate_activation_link(token, request: Request):
    url = f"{request.url.scheme}://localhost:{request.url.port}/api/v1/register/verify/{token.hex()}"
    return url

def generate_verification_data() -> dict[str, str]:
    token = randbytes(10)
    hashedCode = hashlib.sha256()
    hashedCode.update(token)
    verification_code = hashedCode.hexdigest()
    return { "verification_code": verification_code, "token": token }

def decrypt_verification_code_from_token(token):
    hashedCode = hashlib.sha256()
    hashedCode.update(bytes.fromhex(token))
    verification_code = hashedCode.hexdigest()
    return verification_code