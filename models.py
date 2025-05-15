from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Projektas(db.Model):
    __tablename__ = 'nt_projektai'
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String)
    kaina = db.Column(db.Float)
    ivedimo_data = db.Column(db.DateTime, default=datetime.datetime.now)
    atlikti_darbai = db.relationship('AtliktasDarbas', backref='projektas', cascade='all, delete-orphan')

    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

    @property
    def kaina_su_pvm(self):
        return round(self.kaina * 1.21, 2)

    def __repr__(self):
        return f'{self.id} {self.pavadinimas} {self.kaina} {self.ivedimo_data}'

class AtliktasDarbas(db.Model):
    __tablename__ = 'atlikti_darbai'
    id = db.Column(db.Integer, primary_key=True)
    darbas = db.Column(db.String)
    samata = db.Column(db.Float)
    imone = db.Column(db.String)
    projektas_id = db.Column(db.Integer, db.ForeignKey('nt_projektai.id'), nullable=False)

    def __init__(self, darbas, samata, imone):
        self.darbas = darbas
        self.samata = samata
        self.imone = imone

    def __repr__(self):
        return f'{self.id} {self.darbas} {self.imone} {self.samata}'