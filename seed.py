from models import Profile, db
from app import app

with app.app_context():
    print ("start seeding")

    Profile.query.delete()

    print ("seeding Profile")

    Profile1 = Profile(user_name="John", email="johndoe1@gmail.com")
    Profile2 = Profile(user_name="kinuthia", email="kinuthia1@gmail.com")
    Profile3 = Profile(user_name="samuel", email="samuelfg1@gmail.com")

    db.session.add_all([Profile1, Profile2, Profile3])
    db.session.commit()
    print("Profile seeded...")
    print("database seeded...")