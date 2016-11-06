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
	resultados = cursor.fetchall()
	cursor.close()
	numero_tablas=len(resultados)
	return template('acceso.tpl', db=db, tablas=resultados, numero_tablas=numero_tablas)

run(host='127.0.0.1', port=8080, debug=True)