from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr, validator
import datetime
from ludis.core.constants import OUTDOOR_SPORTS, INDOOR_SPORTS, OTHER_SPORTS, ATHLETIC_ABILITY_RANGE
import re

class FitnessProfile(BaseModel):

    outdoor: List[str]
    indoor: List[str]
    other: List[str]

    aa: int

    @validator("outdoor")
    def validate_outdoor_selection(cls, v):

        for sport in v:
            if(sport not in OUTDOOR_SPORTS):
                raise ValueError("Invalid Outdoor Sport preference.")
        
        return v
    
    @validator("indoor")
    def validate_indoor_selection(cls, v):

        for sport in v:
            if(sport not in INDOOR_SPORTS):
                raise ValueError("Invalid Indoor Sport preference.")

        return v

    @validator("other")
    def validate_other_selection(cls, v):

        for sport in v:
            if(sport not in OTHER_SPORTS):
                raise ValueError("Invalid Other Sport preference.")
            
        return v

    @validator("aa")
    def validate_athletic_ability(cls, v):

        if(v not in ATHLETIC_ABILITY_RANGE):
            raise ValueError("Invalid numerical value for Athletic Ability.")
            
        return v

class SupplementaryProfile(BaseModel):

    gender: int
    age: int
    weight: int
    zipcode: constr(max_length=10)
    phone: constr(max_length = 11)
    bio: constr(max_length = 200)

    @validator('zipcode')
    def zipcode_validator(cls, v):

        if("-" not in v):
            raise ValueError("Invalid format for ZipCode (meant to be XXXXX-XXXX). Got {} instead.".format(v))
        
        comp = v.split("-")
        if(len(comp) == 2 and (len(comp[0]) == 5 and len(comp[1]) == 4) and ("".join(comp).isnumeric())):
            return v
        
        raise ValueError("Invalid format for ZipCode (meant to be XXXXX-XXXX). Got {} instead.".format(v))
    
    @validator('phone')
    def phone_validator(cls, v):

        out = re.match("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", v)

        if(out == None):
            raise ValueError("Invalid format for Phone Number.")
        
        return v

class User(BaseModel):

    # is_google: bool = False
    # is_facebook: bool = False
    # is_twitter: bool = False

    email: EmailStr
    first_name: str
    last_name: str
    password: constr(min_length=8, max_length=20)
    username: Optional[constr(max_length=15)]
    date_created: datetime.datetime = datetime.datetime.now()

    f_profile: Optional[FitnessProfile]
    su_profile: Optional[SupplementaryProfile]

    @validator('password')
    def validate_password(cls, v):

        out = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$", v)
       
        if(out):
            return v

        raise ValueError("Invalid password.")
    
    # @validator("username")

print(datetime.datetime.now())