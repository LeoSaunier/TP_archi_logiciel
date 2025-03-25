from flask import abort, jsonify,render_template, request, redirect, url_for
from .app import app, db
from .models import *

def make_public_questionnaire(questionnaire):
    new_questionnaire = {}
    for field in questionnaire:
        if field == 'id':
            new_questionnaire['uri'] = url_for('questionnaire_detail', questionnaire_id=questionnaire['id'], _external=True)
        else:
            new_questionnaire[field] = questionnaire[field]
    return new_questionnaire

def make_public_question(question):
    new_question = {}
    for field in question:
        if field == 'numero_question':
            new_question['uri'] = url_for('question', questionnaire_id=question['questionnaire_id'], numero_question=question['numero_question'], _external=True)
        else:
            new_question[field] = question[field]
    return new_question



@app.route('/quizz/api/v1.0/questionnaires', methods=['GET'])
def questionnaires():
    return jsonify({'questionnaires': [make_public_questionnaire(questionnaire) for questionnaire in get_all_questionnaires()]})

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>', methods=['GET'])
def questionnaire_detail(questionnaire_id):
    return jsonify({"questionnaire" : get_questionnaire(questionnaire_id), "questions" : url_for('questions', questionnaire_id=questionnaire_id, _external=True)})

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions', methods=['GET'])
def questions(questionnaire_id):
    return jsonify({'questions': [ make_public_question(question) for question in get_all_questions(questionnaire_id)]})

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions/<int:numero_question>', methods=['GET'])
def question(questionnaire_id, numero_question):
    return jsonify(get_question(questionnaire_id, numero_question))

@app.route('/quizz/api/v1.0/questionnaires', methods=['POST'])
def create_questionnaire():
    if not request.json or not 'name' in request.json:
        abort(400)
    return add_questionnaire(request.json['name']), 201

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions', methods=['POST'])
def create_question(questionnaire_id):
    if not request.json or not 'title' in request.json or not 'questionType' in request.json or not 'reponse' in request.json:
        abort(400)
    if request.json['questionType'] == 'simple_question':
        if not 'proposition1' in request.json or not 'proposition2' in request.json:
            abort(400)
        return add_question(request.json['questionType'], questionnaire_id, request.json), 201
    elif request.json['questionType'] == 'open_question':
        return add_question(request.json['questionType'], questionnaire_id, request.json), 201
    abort(400)
    

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions/<int:numero_question>', methods=['DELETE'])
def remove_question(questionnaire_id, numero_question):
    return delete_question(questionnaire_id, numero_question)

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>', methods=['DELETE'])
def remove_questionnaire(questionnaire_id):
    return delete_questionnaire(questionnaire_id)

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>', methods=['PUT'])
def up_questionnaire(questionnaire_id):
    if not request.json or not 'name' in request.json:
        abort(400)
        
    return update_questionnaire(questionnaire_id, request.json['name']), 201

@app.route('/quizz/api/v1.0/questionnaires/<int:questionnaire_id>/questions/<int:numero_question>', methods=['PUT'])
def up_question(questionnaire_id, numero_question):
    id = get_id_question(questionnaire_id, numero_question)
    type = get_type_question(id)
    if type == 'open_question':
        if not request.json or not 'title' in request.json or not 'reponse' in request.json:
            abort(400)
        return update_question(questionnaire_id, numero_question, request.json, 'open_question'),
    elif type == 'simple_question':
        if not request.json or not 'title' in request.json or not 'reponse' in request.json or not 'proposition1' in request.json or not 'proposition2' in request.json:
            abort(400)
        return update_question(questionnaire_id, numero_question, request.json, 'simple_question')
    return update_question(questionnaire_id, numero_question, request.json['title'], request.json['questionType']), 201


   