from flask import Flask, request
#allow us to query our mysql database
from flask_mysqldb import MySQL

#create a server(flask object),configure our server, request to specific route can interface to our code
server = Flask(__name__)
#instance of mysql, pass the server, so that our app can connect to mysql database, to query the db
mysql = MYSQL(server)

#config, server object has a config attribute, essentially a dictionary to store configuration variable
#those variables are used to connect to mysql db
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

#create a route, route to function login
@server.route("/login", methods=["POST"])
def login():
    #basic authentication header
    auth = request.authorization
    #auth.username
    #auth.password
    if not auth:
        return "missing credentials", 401

    #check db for username and password