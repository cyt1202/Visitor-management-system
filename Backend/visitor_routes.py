from flask import Blueprint, request, jsonify
from models import (
    create_reservation,
    get_reservations_by_user,
    update_reservation,
    delete_reservation,
    get_user_profile,
    update_user_profile
)


'''
This file is for the visitors' operations
'''
visitor_bp = Blueprint("visitor", __name__)


# create reservations
@visitor_bp.route("/reservations", methods=["POST"])
def submit_reservation():
    data = request.json
    reservation_id = create_reservation(
        data["user_id"], data["date"], data["time"], data["location"], data["purpose"]
    )
    return jsonify({"success": True, "reservation_id": reservation_id})


# get visitor's history reservations
@visitor_bp.route("/reservations", methods=["GET"])
def list_reservations():
    # Retrieve user_id from the query parameters (request.args)
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({"success": False, "message": "User ID is required"}), 400

    try:
        # Call the database function
        rows = get_reservations_by_user(user_id)
        
        return jsonify([dict(r) for r in rows])
        
    except Exception as e:
        print(f"Database query error: {e}")
        return jsonify({"success": False, "message": "Failed to retrieve reservations."}), 500


# change the reservation@visitor_bp.route("/reservations/<int:res_id>", methods=["PUT"])
@visitor_bp.route("/reservations/<int:res_id>", methods=["PUT"])
def edit_reservation(res_id):
    data = request.json
    update_reservation(res_id, data["date"], data["time"], data["location"], data["purpose"])
    return jsonify({"success": True})


# delete reservation
@visitor_bp.route("/reservations/<int:res_id>", methods=["DELETE"])
def remove_reservation(res_id):
    delete_reservation(res_id)
    return jsonify({"success": True})

# Get visitor's personal profile information
# Endpoint: GET /api/profile/<int:user_id>
@visitor_bp.route("/profile/<int:user_id>", methods=["GET"])
def get_profile_data(user_id):
    # NOTE: In a secure system, the user_id should be extracted from the token/session
    # and compared to the requested user_id, or simply rely on the token's ID.

    profile = get_user_profile(user_id)

    if profile:
        return jsonify({
            "success": True,
            "profile": dict(profile) 
        })
    else:
        return jsonify({"success": False, "message": "Profile not found"}), 404

# Update visitor's personal profile information
# Endpoint: PUT /api/profile/<int:user_id>
@visitor_bp.route("/profile/<int:user_id>", methods=["PUT"])
def update_profile_data(user_id):
    data = request.get_json()
    
    name = data.get("name")
    phone = data.get("phone")
    affiliation = data.get("affiliation")

    # Call the database function to update the Visitor_Info table
    updated_rows = update_user_profile(user_id, name, phone, affiliation)

    if updated_rows > 0:
        return jsonify({"success": True, "message": "Profile updated successfully"})
    else:
        return jsonify({"success": False, "message": "Failed to update profile or no changes were made"}), 400