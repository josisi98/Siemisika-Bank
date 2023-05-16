import sys
import csv
import os
from database import Base,Comptes,Clients,Utilisateurs,Carnet_client,Transactions
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_bcrypt import Bcrypt
from flask import Flask

app = Flask(__name__)
engine = create_engine('sqlite:///sikabank.db',connect_args={'check_same_thread': False},echo=True)
Base.metadata.bind = engine
db = scoped_session(sessionmaker(bind=engine))
bcrypt = Bcrypt(app)


def compte():
    # user 1
    nom_utilisateur = 'C00000001'
    nom = 'moise'
    user_type = 'gestionnaire'
    mdp = 'Moiseo@001'
    mdp_hash = bcrypt.generate_password_hash(mdp).decode('utf-8')
    db.execute("INSERT INTO utilisateurs (id,nom,user_type,mot_de_passe) VALUES (:u,:n,:t,:p)",
                {"u": nom_utilisateur,"n":nom,"t":user_type ,"p": mdp_hash})
    db.commit()
    print("compte Terminé ............................................ ")
    # user 2
    nom_utilisateur = 'C00000002'
    nom = 'josias'
    user_type = 'caissier'
    mdp = 'Josias@002'
    mdp_hash = bcrypt.generate_password_hash(mdp).decode('utf-8')
    db.execute("INSERT INTO utilisateurs (id,nom,user_type,mot_de_passe) VALUES (:u,:n,:t,:p)",
                {"u": nom_utilisateur,"n":nom,"t":user_type ,"p": mdp_hash})
    db.commit()
    print("compte Terminé ............................................ ")
    # user 3
    nom_utilisateur = 'C00000003'
    nom = 'anas'
    user_type = 'caissier'
    mdp = 'Anas@003'
    mdp_hash = bcrypt.generate_password_hash(mdp).decode('utf-8')
    db.execute("INSERT INTO utilisateurs (id,nom,user_type,mot_de_passe) VALUES (:u,:n,:t,:p)",
                {"u": nom_utilisateur,"n":nom,"t":user_type ,"p": mdp_hash})
    db.commit()
    print("compte Terminé ............................................ ")

if __name__ == "__main__":
    compte()