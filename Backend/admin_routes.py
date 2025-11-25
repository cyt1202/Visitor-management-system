from flask import Blueprint, request, jsonify
from models import (
    admin_get_all_reservations,
    admin_update_reservation_status,
    get_today_approved_visitors,
    get_daily_report,
    get_pending_count, 
    get_today_visitors_count, 
    get_most_popular_location,
    get_admin_by_id, 
    update_admin_info
)

'''
This file is for the Administrators' execution
'''
admin_bp = Blueprint("admin", __name__)


# get the reservation list, which can be filtered by status
@admin_bp.route("/reservations", methods=["GET"])
def list_admin_reservations():
    status = request.args.get("status")
    date = request.args.get("date")
    location = request.args.get("location")

    rows = admin_get_all_reservations(status, date, location)
    
    return jsonify([dict(r) for r in rows])

# GET Admin Profile
@admin_bp.route("/profile/<int:admin_id>", methods=["GET"])
def get_admin_profile(admin_id):
    row = get_admin_by_id(admin_id)
    if row:
        return jsonify({"success": True, "profile": dict(row)})
    return jsonify({"success": False, "message": "Admin not found"}), 404

# PUT Update Admin Profile
@admin_bp.route("/profile/<int:admin_id>", methods=["PUT"])
def update_admin_profile(admin_id):
    data = request.json
    email = data.get("email", "")
    phone = data.get("phone", "")
    
    # Update database
    update_admin_info(admin_id, email, phone)
    
    return jsonify({"success": True, "message": "Profile updated successfully"})

# update the reservation state
@admin_bp.route("/reservations/<int:res_id>", methods=["PUT"])
def admin_update(res_id):
    data = request.json
    admin_update_reservation_status(res_id, data["status"], data["admin_id"], data["comment"])
    return jsonify({"success": True})

# get dashboard metrics
@admin_bp.route("/metrics", methods=["GET"])
def get_dashboard_metrics():
    pending_count = get_pending_count()
    today_visitors_count = get_today_visitors_count()
    
    popular_loc = get_most_popular_location()
    
    if popular_loc:
        popular_location_data = {
            "location": popular_loc["location"],
            "total": popular_loc["total"]
        }
    else:
        popular_location_data = {"location": "N/A", "total": 0}

    return jsonify({
        "pending_count": pending_count,
        "today_visitors_count": today_visitors_count,
        "popular_location": popular_location_data
    })

# get the approved records for today 
@admin_bp.route("/today", methods=["GET"])
def today_visitors():
    rows = get_today_approved_visitors()
    return jsonify([dict(r) for r in rows])


# generate daily records
@admin_bp.route("/report", methods=["GET"])
def daily_report():
    rows = get_daily_report()
    return jsonify([dict(r) for r in rows])
