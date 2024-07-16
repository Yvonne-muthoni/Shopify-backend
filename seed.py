
from faker import Faker
from models import db, User, Product
import random
from app import app

fake = Faker()

def seed_users(num_users=10):
    User.query.delete()
    for _ in range(num_users):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password()
        )
        db.session.add(user)
    db.session.commit()

def seed_products(num_products=20):
    Product.query.delete()
    for _ in range(num_products):
        product = Product(
            name=fake.word(),
            description=fake.sentence(),
            price=random.uniform(10.0, 100.0),
            image=fake.image_url()
        )
        db.session.add(product)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_users()
        seed_products()


=======
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

