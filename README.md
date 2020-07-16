# FSND: Final Project: Capstone 

## Description: 
A API for setting up speaking events for a venue.

### Dependencies:
- Python 3.7
- pip install -r requirements.txt (to install pip dependencies)

### Models:
- The endpoints are as follows: 

- GET '/events'
    Retrieves events in the database and returns json

- GET '/speakers'
    Retrieves speakers in the database and returns json

- POST '/events'
    Add event to the database and returns json

- POST '/speakers'
    Add speaker to the database and returns json

- PATCH '/events/int:event_id' 
    Updates a event in the database and returns json

- PATCH '/speakers/int:speaker_id'
    Updates a speaker in the database and returns json

- DELETE '/events/int:event_id'
    Removes a event in the database and returns json

- DELETE '/speakers/int:speaker_id'
    Removes a speaker in the database and returns json

#### Authentication:

# Heroku App URL: https://eventspeakcapstone.herokuapp.com/ 

# Example of appended token(this example not valid, active included in submission):
 
# Event Planer: 
GET https://eventspeakcapstone.herokuapp.com/events HTTP/1.1
Host: localhost:5000
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRaRFA2Y1ZZZm96cGVXX3cyaFJrTCJ9.eyJpc3MiOiJodHRwczovL2Z1bGxzbmQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzVlYjljZTNlYmM4MGM2YjNmZjZjMiIsImF1ZCI6ImNvZmZlZUFQSSIsImlhdCI6MTU5MDg5MDI0MSwiZXhwIjoxNTkwODk3NDQxLCJhenAiOiJWRFBjV1hkT1VjdlNKdzZLN0Zqdm5Yb3NNQVpRRDFqeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsInBhdGNoOmRyaW5rcyIsInBvc3Q6ZHJpbmtzIl19.UODLQZvibQYsfSKk25Ej-cDqOn9U_DM5tArDXGmB4sWCAKVZcsRD89A3hYmIVteluRaT30TLoube5geY7YgqpUVU-KxrONosOKAbX4lrxHZTZtFnB-NCs7XjbDDHwYOvjwGUdaOMmR3enlcxDsdf3fLbFZroWJ5TPeyjl_pP4le99WKYiOm-X7YKPqszp0RdTkvAWYSSP_db73AiG5zm_EsLHQXcpY8y0toLNXXcbrcGmk9ahjEibvilwSGucqcNAcZSmoCAtO4SQe4yGAvYF5RlB438GY-79VOwtEErYmUlq_6kLlIJ1yzgK6_leA3O3CsfoFs4YRQA4VDz40i8yQ

## Heroku API:

