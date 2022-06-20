from ludis.schemas.sql.models import ( 
    Users, Profiles, Preferences, Activities, 
    Locations, Events, Relationships, Groups
)
from ludis.schemas.sql.associations import (
    UserEventAssociation, UserGroupAssociation, locations_activities
)
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class UserObject(SQLAlchemyObjectType):

    class Meta:
        model = Users
        interfaces = (graphene.relay.Node)


class ProfileObject(SQLAlchemyObjectType):

    class Meta:
        model = Profiles
        interfaces = (graphene.relay.Node)

class PreferenceObject(SQLAlchemyObjectType):

    class Meta:
        model = Preferences
        interfaces = (graphene.relay.Node)

class ActivityObject(SQLAlchemyObjectType):

    class Meta:
        model = Activities
        interfaces = (graphene.relay.Node)

class LocationObject(SQLAlchemyObjectType):

    class Meta:
        model = Locations
        interfaces = (graphene.relay.Node)

class EventObject(SQLAlchemyObjectType):

    class Meta:
        model = Events
        interfaces = (graphene.relay.Node)

class RelationshipObject(SQLAlchemyObjectType):

    class Meta:
        model = Relationships
        interfaces = (graphene.relay.Node)

class GroupObject(SQLAlchemyObjectType):

    class Meta:
        model = Groups
        interfaces = (graphene.relay.Node)
