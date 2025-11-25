from flask import Blueprint, request, jsonify
from models import get_user_by_username, create_user, get_admin_by_username,create_visitor_info
from utils import hash_password, verify_password

'''
This file is for user registration and logging in
'''
auth_bp = Blueprint("auth", __name__)


# ------------------------
# Visitor resgistration
# ------------------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password = data["password"]

    if get_user_by_username(username):
        return jsonify({"success": False, "message": "Username exists"}), 400

    user_id = create_user(username, hash_password(password))
    create_visitor_info(user_id, name="", phone="", affiliation="")
    return jsonify({"success": True, "user_id": user_id})


# ------------------------
# Login: Visitor & Admin 
# ------------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    # try user
    user = get_user_by_username(username)
    if user and verify_password(password, user["password_hash"]):
        return jsonify({
            "success": True,
            "role": "visitor",
            "user_id": user["user_id"]
        })

    # try admin
    admin = get_admin_by_username(username)
    if admin and verify_password(password, admin["password_hash"]):
        return jsonify({
            "success": True,
            "role": "admin",
            "admin_id": admin["admin_id"]
        })

    return jsonify({"success": False, "message": "Invalid credentials"}), 401