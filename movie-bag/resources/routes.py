from .movie import MoviesApi, MovieApi
from .event_detail import EventDetailsApi, EventDetailApi
from .couple_image import CoupleImagesApi, CoupleImageApi
from .auth import SignupApi, LoginApi
from .reset_password import ForgotPassword, ResetPassword


def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')

    api.add_resource(EventDetailsApi, '/api/event_details')
    api.add_resource(EventDetailApi, '/api/event_details/<id>')

    api.add_resource(CoupleImagesApi, '/api/couple_images')
    api.add_resource(CoupleImageApi, '/api/couple_image/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')

