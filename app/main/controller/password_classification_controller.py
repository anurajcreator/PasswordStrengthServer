from flask_restx import Resource
from app.main.service.password_prediction_service import password_strength_predict
from app.main.util.password_classification_dto import PasswordClassificationDto
from flask import request
from flask import render_template, make_response

api = PasswordClassificationDto.api 
_password_pred = PasswordClassificationDto.password_pred

@api.route('/predict')
class PasswordPrediction(Resource):
    @api.doc('Password Strenth Prediction')
    @api.expect(_password_pred) 
    def post(self):
        """Password Strenth Prediction"""
        return password_strength_predict(request.json)


@api.route('/')
class HomePage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        status = 200
        message = ""
        color = ""
        return make_response(render_template("app.html", status = status, message = message, color = color), 200,headers)
    
    def post(self):
        headers = {'Content-Type': 'text/html'}
        message = ""
        data = {}
        data['password'] = request.form['password'] 
        response, status = password_strength_predict(data)
        message = response['message']
        strength = response['data']
        if strength == '2':
            color = 'success'
        elif strength == '1':
            color = 'warning'

        else:
            color = 'danger'
        
        return make_response(render_template("app.html", message = message, status = status, color = color), 200,headers)