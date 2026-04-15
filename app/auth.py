from flask import Flask, request, jsonify
from app.auth import login_user, verify_token
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get(
            "Authotiration", ""
        )
        token = auth_header.replace("Bearer","")

        # Vérifier le token
        payload = verify_token(token)
        if not payload:
            return jsonify({"error": "Non autorisé"}), 401
        
        # Passer le payload à la fonction
        return f(payload, *args, **kwargs)
    return decorated



