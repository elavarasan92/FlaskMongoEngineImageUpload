from flask import Response, request
from database.models import EventDetail, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, EventDetailAlreadyExistsError, InternalServerError, \
    UpdatingEventDetailError, DeletingEventDetailError, EventDetailNotExistsError
from mongoengine import FileField


class EventDetailsApi(Resource):
    def get(self):
        query = EventDetail.objects()
        event_details = EventDetail.objects().to_json()
        return Response(event_details, mimetype="application/json", status=200)

	#{"bride_name" : "Saradha",
    #"groom_name" : "Muthu",
    #"mobile_no" : "8531990331",
    #"event_date" : "Jun 1 2005  1:33PM",
    #"venue" : "Sakthi mahal",
    #"venue_address" : "Koilambakam main road, Chennai -600117."}

# "event_date" : "Jun 1 2005  1:33PM" date should be in this format
    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            print("user_id : " + str(user_id))
            body = request.get_json()
            print("body : " + str(request.get_json()))
            user = User.objects.get(id=user_id)
            event_detail = EventDetail(**body, added_by=user)
            event_detail.save()
            user.update(push__event_detail=event_detail)
            user.save()
            id = event_detail.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise EventDetailAlreadyExistsError
        except Exception as e:
            print(e)
            raise InternalServerError


class EventDetailApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            event_detail = EventDetail.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            EventDetail.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingEventDetailError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            event_detail = EventDetail.objects.get(id=id, added_by=user_id)
            event_detail.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingEventDetailError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            event_details = EventDetail.objects.get(id=id).to_json()
            return Response(event_details, mimetype="application/json", status=200)
        except DoesNotExist:
            raise EventDetailNotExistsError
        except Exception:
            raise InternalServerError
