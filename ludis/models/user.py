from typing import List, Optional
import attr
import datetime
from ludis.core.constants import OUTDOOR_SPORTS, INDOOR_SPORTS, OTHER_SPORTS, ATHLETIC_ABILITY_RANGE
from ludis.models import validate_max_length
import re

@attr.s(slots = True)
class UserCreate:

    username = attr.ib(converter = str)
    password = attr.ib(converter = str)
    email = attr.ib(converter = str, validator = [validate_max_length])
    first_name = attr.ib(converter = str, validator = [validate_max_length])
    last_name = attr.ib(converter = str, validator = [validate_max_length])
    profile = attr.ib(init = False)

    @password.validator
    def check_password(self, attribute, value):
        out = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$", value)
        if(out == None):
            raise ValueError("Invalid password.")

@attr.s(slots = True)
class UserRequest:
    
    username: str = attr.ib(converter=str)
    email: str = attr.ib(converter=str, validator = [validate_max_length])
    first_name: str = attr.ib(converter=str, validator = [validate_max_length])
    last_name: str = attr.ib(converter=str, validator = [validate_max_length])
    
    events_created: Optional[List[int]] = attr.ib(init = False, default = None)
    events_joined: Optional[List[int]] = attr.ib(init = False, default = None)
    
    profile = attr.ib(init = False)



@attr.s(slots = True)
class UserInDatabase:

    username = attr.ib(converter=str)
    email = attr.ib(converter=str, validator = [validate_max_length])
    first_name = attr.ib(converter=str, validator = [validate_max_length])
    last_name = attr.ib(converter=str, validator = [validate_max_length])
    profile = attr.ib()