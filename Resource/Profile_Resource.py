from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Profile

class ProfileResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('full_name', type=str, required=True, help="Full name is required")
    parser.add_argument('phone_number', type=str, required=False)

    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        profile = Profile.query.filter_by(user_id=user_id).first()
        if not profile:
            return {"message": "Profile not found"}, 404
        return {"profile": profile.to_dict()}, 200

    @jwt_required
    def post(self):
        data = self.parser.parse_args()
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        new_profile = Profile(
            user_id=user_id,
            full_name=data['full_name'],
            phone_number=data.get('phone_number')
            # Add other fields from request as needed
        )

        try:
            db.session.add(new_profile)
            db.session.commit()
            return {"message": "Profile created successfully", "profile": new_profile.to_dict()}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": "Error creating profile", "error": str(e)}, 500

    @jwt_required
    def put(self):
        data = self.parser.parse_args()
        user_id = get_jwt_identity()
        profile = Profile.query.filter_by(user_id=user_id).first()

        if not profile:
            return {"message": "Profile not found"}, 404

        profile.full_name = data['full_name']
        profile.phone_number = data.get('phone_number')

        try:
            db.session.commit()
            return {"message": "Profile updated successfully", "profile": profile.to_dict()}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": "Error updating profile", "error": str(e)}, 500

    @jwt_required
    def delete(self):
        user_id = get_jwt_identity()
        profile = Profile.query.filter_by(user_id=user_id).first()

        if not profile:
            return {"message": "Profile not found"}, 404

        try:
            db.session.delete(profile)
            db.session.commit()
            return {"message": "Profile deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": "Error deleting profile", "error": str(e)}, 500