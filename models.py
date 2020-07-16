import os
import json
from sqlalchemy import Column, String, Integer, create_engine, Date
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_migrate import Migrate

database_name = "eventspeak"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "postgres://{}".format(os.path.join(project_dir, database_name)


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
'''
    db.init_app(app)
    db.create_all()
'''

db = SQLAlchemy()


class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)
    event_date = db.Column(db.Date)
    speakers = db.relationship("Speaker", backref="events")

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "event_date": self.event_date,
            "speakers": self.speakers,
        }


class Speaker(db.Model):
    __tablename__ = "speakers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    expertise = db.Column(db.String)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "expertise": self.expertise,
            "event_id": self.event_id,
        }
