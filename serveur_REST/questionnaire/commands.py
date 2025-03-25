from .app import db, app
from .models import *

@app.cli.command('create_tables')
def create_tables():
    db.drop_all()
    db.create_all()

    db.session.add(Questionnaire('Questionnaire 1'))
    db.session.add(Questionnaire('Questionnaire 2'))
    db.session.add(Questionnaire('Questionnaire 3'))
    db.session.commit()
    db.session.add(SimpleQuestion('Question 1', Questionnaire.query.get(1), 1, 1, 'text', 'answer'))
    db.session.add(SimpleQuestion('Question 2', Questionnaire.query.get(1), 2, 2, 'text', 'answer'))
    db.session.add(OpenQuestion('Question 3', Questionnaire.query.get(2), 1, 'Léo'))
    db.session.commit()
    print('Tables created')
