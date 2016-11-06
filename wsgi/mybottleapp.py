# -*- coding: utf-8 -*-

from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
import MySQLdb

@route('/')
def redirect_to_login():
	redirect('/index')

@route('/index', method=["GET"])
def login():
	return template('index.tpl')