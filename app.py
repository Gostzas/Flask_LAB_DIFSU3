from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Projektas, AtliktasDarbas

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

# Marsrutai
@app.route('/')
def home():
    search_text = request.args.get('paieska')
    if search_text:
        projects = Projektas.query.filter(Projektas.pavadinimas.ilike(search_text + '%'))
    else:
        projects = Projektas.query
    return render_template('index.html', projects=projects)


@app.route('/projektai/<int:projektas_id>')
def one_project(projektas_id):
    project = Projektas.query.get(projektas_id)
    if project:
        return render_template('vienas_projektas.html', project=project)
    else:
        return 'Blogas ID, projektas neegzistuoja'


if __name__ == '__main__':
    app.run()