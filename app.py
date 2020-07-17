import os
import json
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from auth import AuthError, requires_auth
from models import setup_db, db, Speaker, Event
from flask import Flask, request, abort, jsonify


RESULTS_PER_PAGE = 10


def paginate_results(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * RESULTS_PER_PAGE
    end = start + RESULTS_PER_PAGE

    results = [result.format() for result in selection]
    return results[start:end]


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization, true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PATCH,POST,DELETE,OPTIONS"
        )
        return response

    @app.route("/")
    def welcome():
        return jsonify({"message": "Welcome to my Capstone!"})

    # ========================================#
    # GET Request Endpoints
    # ========================================#

    # =v= GET request for retriving events  =v= #

    @app.route("/events", methods=["GET"])
    def get_events():

        selection = Event.query.all()
        paginate_events = paginate_results(request, selection)

        if len(paginate_events) == 0:
            abort(404)

        try:

            return jsonify({"success": True, "events": paginate_events})

        except Exception:
            abort(422)

    # =v= GET request for retriving speakers  =v= #

    @app.route("/speakers", methods=["GET"])
    def get_speakers():

        selection = Speaker.query.order_by(Speaker.id).all()
        paginate_speakers = paginate_results(request, selection)

        if len(paginate_speakers) == 0:
            abort(404)

        try:

            return jsonify({"success": True, "speakers": paginate_speakers})

        except Exception:
            abort(422)

    # ========================================#
    # POST Request Endpoints
    # ========================================#

    # =v= POST to add events  =v= #

    @app.route("/events", methods=["POST"])
    @requires_auth("post:events")
    def add_events(payload):

        body = request.get_json()

        new_subject = body.get("event", None)
        new_event_date = body.get("event_date", None)

        if body is None:
            abort(400)

        try:
            event = Event(subject=new_subject, event_date=new_event_date)
            event.insert()

            return jsonify({"success": True, "created": event})

        except Exception:
            abort(422)

    # =v= POST to add speakers  =v= #

    @app.route("/speakers", methods=["POST"])
    @requires_auth("post:speakers")
    def add_speakers(payload):

        body = request.get_json()

        new_name = body.get("event", None)
        new_expertise = body.get("event_date", None)

        if body is None:
            abort(400)

        try:
            speaker = Speaker(name=new_name, expertise=new_expertise)
            speaker.insert()

            return jsonify({"success": True, "created": speaker})

        except Exception:
            abort(422)

    # ========================================#
    # PATCH Request Endpoints
    # ========================================#

    # =v= PATCH event  =v= #

    @app.route("/events/<int:event_id>", methods=["PATCH"])
    @requires_auth("patch:events")
    def update_event(payload, event_id):

        event = Event.query.filter(Event.id == event_id).one_or_none()

        if event is None:
            abort(404)

        body = request.get_json()
        if body is None:
            abort(400)

        new_subject = body.get("subject")
        new_event_date = body.get("event_date")

        try:
            if new_subject is not None:
                event.subject = new_subject

            if new_event_date is not None:
                event.event_date = new_event_date

            event.update()

            updated_event = [event.format()]

            return jsonify({"success": True, "event": updated_event})

        except Exception:
            abort(422)

    # =v= PATCH speaker  =v= #

    @app.route("/speakers/<int:speaker_id>", methods=["PATCH"])
    @requires_auth("patch:speaker")
    def update_speaker(payload, speaker_id):

        speaker = Speaker.query.filter(Speaker.id == speaker_id).one_or_none()

        if speaker is None:
            abort(404)

        body = request.get_json()
        if body is None:
            abort(400)

        new_name = body.get("name")
        new_expertise = body.get("expertise")

        try:
            if new_name is not None:
                speaker.name = new_name

            if new_expertise is not None:
                speaker.expertise = new_expertise

            speaker.update()

            updated_expertise = [speaker.format()]

            return jsonify({"success": True, "speaker": updated_expertise})

        except Exception:
            abort(422)

    # ========================================#
    # DELETE Request Endpoints
    # ========================================#

    # =v= DELETE an event  =v= #

    @app.route("/events/<int:event_id>", methods=["DELETE"])
    @requires_auth("delete:events")
    def delete_event(payload, event_id):

        event = Event.query.filter(Event.id == event_id).one_or_none()

        if event is None:
            abort(404)

        body = request.get_json()
        if body is None:
            abort(400)

        try:
            event.delete()

            return jsonify({"success": True, "delete": event_id})

        except Exception:
            abort(422)

    # =v= DELETE speaker  =v= #

    @app.route("/speakers/<int:speaker_id>", methods=["DELETE"])
    @requires_auth("delete:speaker")
    def delete_speaker(payload, speaker_id):

        speaker = Speaker.query.filter(Speaker.id == speaker_id).one_or_none()

        if speaker is None:
            abort(404)

        body = request.get_json()
        if body is None:
            abort(400)

        try:

            speaker.delete()

            return jsonify({"success": True, "speaker": speaker_id})

        except Exception:
            abort(422)

    return app

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(AuthError)
    def auth_error(error):
        return (
            jsonify(
                {"success": False, "error": 401, "message": "unauthorized request"}
            ),
            401,
        )


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
