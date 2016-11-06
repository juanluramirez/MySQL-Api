# -*- coding: utf-8 -*-

from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
import MySQLdb

@route('/')
def redirect_to_login():
	redirect('/index')

@route('/index', method=["GET"])
def index():
	return template('index.tpl')

@route('/acceso', method='POST')
def acceso():
	host  = request.forms.get("host")
	user  = request.forms.get("user")
	passwd = request.forms.get("passwd")
	db= request.forms.get("db")
	basedatos = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
	cursor = basedatos.cursor()
	tablas = cursor.execute("show tables")
	return template('acceso.tpl', db=db, tablas=tablas)