from .app import db
from sqlalchemy.orm import *

class Questionnaire(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Questionnaire (%d) %s>' % (self.id, self.name)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
    

class Question(db.Model):
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    questionType = db.Column(db.String(120))
    questionnaire = db.relationship('Questionnaire', backref=db.backref('questions', lazy='dynamic'))
    numero_question = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity':'question',
        'polymorphic_on':questionType
    }

    def __init__(self, title, questionnaire, numero_question):
        self.title = title
        self.questionnaire = questionnaire
        self.numero_question = numero_question
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'questionType': self.questionType,
            'questionnaire_id': self.questionnaire_id,
            'numero_question': self.numero_question
        }
    
class SimpleQuestion(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    reponse = db.Column(db.Integer())
    proposition1 = db.Column(db.String(120))
    proposition2 = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity':'simple_question',
    }

    def __init__(self, title, questionnaire, numero_question, reponse, proposition1, proposition2):
        super().__init__(title, questionnaire, numero_question)
        self.reponse = reponse
        self.proposition1 = proposition1
        self.proposition2 = proposition2
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'questionType': self.questionType,
            'questionnaire_id': self.questionnaire_id,
            'numero_question': self.numero_question,
            'reponse': self.reponse,
            'proposition1': self.proposition1,
            'proposition2': self.proposition2
        }
    
class OpenQuestion(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    reponse = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity':'open_question',
    }

    def __init__(self, title, questionnaire, numero_question, reponse):
        super().__init__(title, questionnaire, numero_question)
        self.reponse = reponse
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'questionType': self.questionType,
            'questionnaire_id': self.questionnaire_id,
            'numero_question': self.numero_question,
            'reponse': self.reponse
        }


def get_all_questionnaires():
    liste = []
    for questionnaire in Questionnaire.query.all():
        liste.append(questionnaire.to_json())
    return liste

def get_questionnaire(questionnaire_id):
    return Questionnaire.query.get(questionnaire_id).to_json() if Questionnaire.query.get(questionnaire_id) else None

def get_all_questions(id_questionnaire):
    liste = []
    for question in Question.query.filter_by(questionnaire_id=id_questionnaire):
        liste.append(question.to_json())
    return liste

def get_question(questionnaire_id, numero_question):
    return Question.query.filter_by(questionnaire_id=questionnaire_id, numero_question=numero_question).first().to_json() if Question.query.filter_by(questionnaire_id=questionnaire_id, numero_question=numero_question).first() else None

def add_questionnaire(name):
    questionnaire = Questionnaire(name)
    db.session.add(questionnaire)
    db.session.commit()
    return questionnaire.to_json()

def add_question(questionType, questionnaire_id, json):
    if questionType == 'simple_question':
        question = SimpleQuestion(json['title'], Questionnaire.query.get(questionnaire_id), len(Question.query.filter_by(questionnaire_id=questionnaire_id).all()) + 1, json['reponse'], json['proposition1'], json['proposition2'])
    elif questionType == 'open_question':
        question = OpenQuestion(json['title'], Questionnaire.query.get(questionnaire_id), len(Question.query.filter_by(questionnaire_id=questionnaire_id).all()) + 1, json['reponse'])
    db.session.add(question)
    db.session.commit()
    return question.to_json()

def delete_question(questionnaire_id, numero_question):
    question = Question.query.filter_by(questionnaire_id=questionnaire_id, numero_question=numero_question).first()
    for q in Question.query.filter_by(questionnaire_id=questionnaire_id):
        if q.numero_question > numero_question:
            q.numero_question -= 1
    db.session.delete(question)
    db.session.commit()
    return {'result': True}, 204

def delete_questionnaire(questionnaire_id):
    for question in Question.query.filter_by(questionnaire_id=questionnaire_id):
        db.session.delete(question)
    questionnaire = Questionnaire.query.get(questionnaire_id)
    db.session.delete(questionnaire)
    db.session.commit()
    return {'result': True}, 204

def update_questionnaire(questionnaire_id, name):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    questionnaire.name = name
    db.session.commit()
    return questionnaire.to_json()

def update_question(questionnaire_id, numero_question, json, questionType):
    if questionType == 'simple_question':
        question = SimpleQuestion.query.filter_by(questionnaire_id=questionnaire_id, numero_question=numero_question).first()
        question.title = json['title']
        question.reponse = json['reponse']
        question.proposition1 = json['proposition1']
        question.proposition2 = json['proposition2']
    elif questionType == 'open_question':
        question = OpenQuestion.query.filter_by(questionnaire_id=questionnaire_id, numero_question=numero_question).first()
        question.title = json['title']
        question.reponse = json['reponse']
    db.session.commit()
    return question.to_json()

def get_id_question(questionnaire_id, numero_question):
    return Question.query.filter_by(questionnaire_id=questionnaire_id, numero_question=numero_question).first().id

def get_type_question(question_id):
    return Question.query.get(question_id).questionType
    