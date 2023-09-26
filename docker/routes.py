from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'parking'
app.config['MYSQL_DB'] = 'parking'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)