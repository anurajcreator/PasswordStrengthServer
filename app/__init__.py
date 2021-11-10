from os import path
from flask_restx import Api
from flask import Blueprint

from app.main.config import authorizations, version

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Password Strength Classification Project',
          version='1.0',
          description='Output 0 -> weak , 1 -> medium, 2 -> strong',
          authorizations=authorizations
          )



from app.main.controller.password_classification_controller import api as password_clf_ns

api.add_namespace(password_clf_ns, path='/password')

