from flask import Response, request, Flask, flash, request, redirect, render_template, jsonify, make_response
from database.models import CoupleImage, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, CoupleImageAlreadyExistsError, InternalServerError, \
    UpdatingCoupleImageError, DeletingCoupleImageError, CoupleImageNotExistsError
from mongoengine import FileField
from werkzeug.utils import secure_filename
from flask_mongoengine import MongoEngine
import io
from flask import send_file

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class CoupleImagesApi(Resource):
    #to get html for uploading image
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('file-upload.html'), 200, headers)

    # to upload file
    def post(self):
        if 'files[]' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp

        files = request.files.getlist('files[]')

        errors = {}
        success = False

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                couple_image = CoupleImage(image_id=1, image_name='Elavarasan')
                couple_image.image_data.new_file()
                couple_image.image_data.write(file)
                couple_image.image_data.close()
                couple_image.save()

                success = True
            else:
                errors[file.filename] = 'File type is not allowed'

        if success and errors:
            errors['message'] = 'File(s) successfully uploaded'
            resp = jsonify(errors)
            resp.status_code = 206
            return resp
        if success:
            resp = jsonify({'message': 'Files successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            print(errors)
            resp = jsonify(errors)
            resp.status_code = 400
            print(resp)
            return resp


class CoupleImageApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            couple_image = CoupleImage.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            CoupleImage.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingCoupleImageError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            couple_image = CoupleImage.objects.get(id=id, added_by=user_id)
            couple_image.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingCoupleImageError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            couple_images = CoupleImage.objects.get(id=id).to_json()
            return Response(couple_images, mimetype="application/json", status=200)
        except DoesNotExist:
            raise CoupleImageNotExistsError
        except Exception:
            raise InternalServerError
