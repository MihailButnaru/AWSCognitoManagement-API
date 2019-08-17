<div align="center">
<h1> AWS Cognito Management RESTful API </h1>
<p1>Simple and complete Restful API that allows you to manage users, appclients and resource servers.</p1>
</div>
<hr/>

## The problem 
You want to access AWS Cognito resources through a customize API without touching the AWS UI. As part
of this goal, AWS Cognito Management API allows you to access different Cognito resources very easy
and efficient.

## This solution
The AWS Cognito Management API is a very lightweight solution for using this Restful API for managing
different services from AWS. It provides light utility functionality.

## Instalation
Start by building a development environment

1. Install the dependencies of project
```
$ pip install -r requirements.txt
```
2. Config the file with the correct env variables
```
$ config.py
```
3. Run the AWS Cognito Management API
```
$ export FLASK_APP=api
$ flask run
```

## Endpoints Structure

| Endpoint        | Method  | Description  |
| ------------- |:-------------:| :-----|
| /users/     | GET | List all users |
| /users/     | POST      |   Create a new user |
| /users/{username} | GET |  Get the specific user based on the username |
| /users/{username} | DELETE |  Delete the specific user based on the username |
| /users/{username} | PUT |  Update the specific user based on the username |
| /appclients/     | GET | List all appclients |
| /appclients/     | POST      |   Create a new appclient |
| /appclients/{clientId}     | GET | Get the specific appclient based on the clientId |
| /appclients/{clientId}     | DELETE      |   Delete a specific appclient based on the clientId |
| /scopes/     | GET | List all scopes |
| /scopes/     | POST | Create a new scope|
| /scopes/{identifier}     | DELETE | Delete the specific scope based on the identifier |



## Deployment
Used gunicorn for production, because Gunicorn is a WSGI server that takes care
of everything which happens in-between the web server and the web application.
It is used because it is stable and can handle more requests at once and is very fast.

Docker deploy
1. Go to your root folder where the Dockerfile is located: Run this
```
docker build -t aws-api .
```
2. Run the docker image
```
docker run -d -p 5000:5000 aws-api
```
Access the aws-api on ```localhost:5000/api/v1```

## License
License © MIHAIL BUTNARU

Made with 💖 Mihail Butnaru
