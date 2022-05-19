
class BasicConfig():

    """Base config for staging database."""

    THREADING: bool = False
    DEBUG: bool = False
    TESTING: bool = False
    SERVER_LOC: str = "localhost:5432"
    SECRET_KEY: str = "92178367776326828052"

    @property
    def DATABASE_URI(self):
        return "postgres://tanush:299792458@{}/ludis".format(self.SERVER_LOC)

class ProductionConfig(BasicConfig):

    """Production config for AWS"""

    THREADING: bool = True
    SERVER_LOC: str = "localhost:5432"

class DevelopmentConfig(BasicConfig):

    DEBUG: bool = True
    SERVER_LOC: str = "localhost:5432"

class TestingConfig(BasicConfig):

    TESTING: bool = True
    SERVER_LOC: str = "localhost:5432"