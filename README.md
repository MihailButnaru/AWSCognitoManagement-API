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
