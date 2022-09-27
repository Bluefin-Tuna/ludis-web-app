import factory
from factory import alchemy
import random

import sqlalchemy
from ..sql import * 

class UserFactory(alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Users
        sqlalchemy_session = db.session
    
    username = factory.Sequence(lambda n: f"User {n}")
    password = factory.Faker("password")
    email = factory.Sequence(lambda n: f"user{n}@gmail.com")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    
    profile = factory.RelatedFactory(
        "core.factories.ProfileFactory", 
        factory_related_name = "user",
    )

    is_staff = True if random.random() < 0.05 else False
    is_superuser = True if random.random() < 0.05 else False
    is_active = True if random.random() < 0.5 else False

class ProfileFactory(alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Profiles
        sqlalchemy_session = db.session
    
    fitness_level = random.randint(1, 10)  if random.random() < 0.8 else 5
    gender = random.randint(0, 1) if random.random() < 0.8 else -1
    weight = random.randint(0, 100000) if random.random() < 0.8 else -1
    description = factory.Faker("paragraph", nb_sentences = 3)
    phone_number = factory.Faker("phone_number")

    user = factory.SubFactory(
        "ludis.UserFactory", 
        profile = None,
    )