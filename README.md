# FSND: Final Project: Capstone 

## Description: 
A API for setting up speaking events for a venue.

## Motivation: 
Final Project for Udacity's Full-Stack Web Developer NanoDegree program.
- postgres & sqlalchemy used to build database=> Check: model.py
- Main operations ran from main app file containing endpoints=> Check: app.py
- App deployed via heroku service=> Check: (Heroku link below)
- Contains test file to autimatically test app=> Check: test_app.py


### Dependencies:
- Python 3.7
## Use following command in terminal to install required dependencies:

- pip3 install -r requirements.txt (to install pip dependencies)

### Models:
- The endpoints are as follows: 

- GET '/events'
    - Retrieves events in the database and returns json
    - Request Arguments: json object contains (events)
    - Returns: Json object containing ({'success': True, "events": paginate_events})
    - sample : curl -X GET https://eventspeakcapstone.herokuapp.com/events
    
{
        return jsonify({
            "success": True, 
            "events": paginate_events
        })
}

- GET '/speakers'
    - Retrieves speakers in the database and returns json
    - Request Arguments: json object contains (speakers)
    - Returns: Json object containing ({'success': True, "speakers": paginate_speakers})
    - sample : curl -X GET https://eventspeakcapstone.herokuapp.com/speakers

{
    return jsonify({
        "success": True, 
        "speakers": paginate_speakers
    })
}

- POST '/events'
    - Add event to the database and returns json
    - Request Arguments: json object contains (event)
    - Returns: Json object containing ({'success': True, "created": event})
    - sample : curl -X POST https://eventspeakcapstone.herokuapp.com/events

{
    return jsonify({
        "success": True, 
        "created": event
    })
}

- POST '/speakers'
    - Add speaker to the database and returns json
    - Request Arguments: json object contains (speaker)
    - Returns: Json object containing ({"success": True, "created": speaker})
    - sample : curl -X POST https://eventspeakcapstone.herokuapp.com/speakers

{

    return jsonify({
        "success": True, 
        "created": speaker
    })
}

- PATCH '/events/int:event_id' 
    - Updates a event in the database and returns json
    - Request Arguments: json object contains (event)
    - Returns: Json object containing ({'success': True, "event": updated_event})
    - sample : curl -X PATCH https://eventspeakcapstone.herokuapp.com/events/int:event_id

{
    return jsonify({
        "success": True, 
        "event": updated_event
    })
}

- PATCH '/speakers/int:speaker_id'
    Updates a speaker in the database and returns json
    - Request Arguments: json object contains (speaker)
    - Returns: Json object containing ({"success": True, "speaker": updated_expertise})
    - sample : curl -X PATCH https://eventspeakcapstone.herokuapp.com/speakers/int:speaker_id

{
    return jsonify({
        "success": True, 
        "speaker": updated_expertise
    })
}

- DELETE '/events/int:event_id'
    - Removes a event in the database and returns json
    - Request Arguments: json object contains (event_id)
    - Returns: Json object containing ({'success': True, "event": event_id})
    - sample : curl -X DELETE https://eventspeakcapstone.herokuapp.com/events/int:event_id

{
    return jsonify({
        "success": True, 
        "delete": event_id
    })
}

- DELETE '/speakers/int:speaker_id'
    - Removes a speaker in the database and returns json
    - Request Arguments: json object contains (speaker_id)
    - Returns: Json object containing ({"success": True, "speaker": speaker_id})
    - sample : curl -X DELETE https://eventspeakcapstone.herokuapp.com/speakers/int:speaker_id

{
    return jsonify({
        "success": True, 
        "speaker": speaker_id
    })
}

#### Authentication:

# Heroku App URL: https://eventspeakcapstone.herokuapp.com/ 

# Example of appended token(this example not valid, active included in submission):
 
# Event Planer: 
GET https://eventspeakcapstone.herokuapp.com/events HTTP/1.1
Host: localhost:5000
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRaRFA2Y1ZZZm96cGVXX3cyaFJrTCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzbmQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzVlYjljZTNlYmM4MGM2YjNmZjZjMiIsImF1ZCI6ImNvZmZlZUFQSSIsImlhdCI6MTU5MDg5MDI0MSwiZXhwIjoxNTkwODk3NDQxLCJhenAiOiJWRFBjV1hkT1VjdlNKdzZLN0Zqdm5Yb3NNQVpRRDFqeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsInBhdGNoOmRyaW5rcyIsInBvc3Q6ZHJpbmtzIl19.UODLQZvibQYsfSKk25Ej-cDqOn9U_DM5tArDXGmB4sWCAKVZcsRD89A3hYmIVteluRaT30TLoube5geY7YgqpUVU-KxrONosOKAbX4lrxHZTZtFnB-NCs7XjbDDHwYOvjwGUdaOMmR3enlcxDsdf3fLbFZroWJ5TPeyjl_pP4le99WKYiOm-X7YKPqszp0RdTkvAWYSSP_db73AiG5zm_EsLHQXcpY8y0toLNXXcbrcGmk9ahjEibvilwSGucqcNAcZSmoCAtO4SQe4yGAvYF5RlB438GY-79VOwtEErYmUlq_6kLlIJ1yzgK6_leA3O3CsfoFs4YRQA4VDz40i8yQ

## Heroku API:
- Use to export needed credentials: source setup.sh


