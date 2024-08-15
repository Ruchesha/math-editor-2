from flask import render_template, jsonify, request
from . import db
from .models import MathOperation
from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/status')
def status():
    return jsonify({'message': 'Server is up and running'})

@routes.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    value1 = data.get('value1')
    value2 = data.get('value2')

    if operation == 'add':
        result = value1 + value2
    elif operation == 'subtract':
        result = value1 - value2
    elif operation == 'multiply':
        result = value1 * value2
    elif operation == 'divide':
        result = value1 / value2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    math_operation = MathOperation(operation=operation, value1=value1, value2=value2, result=result)
    db.session.add(math_operation)
    db.session.commit()

    return jsonify({'result': result})
