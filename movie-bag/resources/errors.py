class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class MovieAlreadyExistsError(Exception):
    pass

class UpdatingMovieError(Exception):
    pass

class DeletingMovieError(Exception):
    pass

class MovieNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class EmailDoesnotExistsError(Exception):
    pass

class BadTokenError(Exception):
    pass

class EventDetailAlreadyExistsError(Exception):
    pass

class UpdatingEventDetailError(Exception):
    pass

class DeletingEventDetailError(Exception):
    pass

class EventDetailNotExistsError(Exception):
    pass


class CoupleImageAlreadyExistsError(Exception):
    pass

class UpdatingCoupleImageError(Exception):
    pass

class DeletingCoupleImageError(Exception):
    pass

class CoupleImageNotExistsError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
    "EventDetailAlreadyExistsError": {
        "message": "EventDetail with given name already exists",
        "status": 400
    },
    "UpdatingEventDetailError": {
        "message": "Updating movie added by other is forbidden",
        "status": 403
    },
    "DeletingEventDetailError": {
        "message": "Deleting movie added by other is forbidden",
        "status": 403
    },
    "EventDetailNotExistsError": {
        "message": "EventDetail with given id doesn't exists",
        "status": 400
    },
"CoupleImageAlreadyExistsError": {
        "message": "CoupleImage with given name already exists",
        "status": 400
    },
    "UpdatingCoupleImageError": {
        "message": "Updating Couple Image added by other is forbidden",
        "status": 403
    },
    "DeletingCoupleImageError": {
        "message": "Deleting Couple Image added by other is forbidden",
        "status": 403
    },
    "CoupleImageNotExistsError": {
        "message": "CoupleImage with given id doesn't exists",
        "status": 400
    },
    "MovieAlreadyExistsError": {
         "message": "Movie with given name already exists",
         "status": 400
     },
     "UpdatingMovieError": {
         "message": "Updating movie added by other is forbidden",
         "status": 403
     },
     "DeletingMovieError": {
         "message": "Deleting movie added by other is forbidden",
         "status": 403
     },
     "MovieNotExistsError": {
         "message": "Movie with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },
     "EmailDoesnotExistsError": {
         "message": "Couldn't find the user with given email address",
         "status": 400
     },
     "BadTokenError": {
         "message": "Invalid token",
         "status": 403
     }
}