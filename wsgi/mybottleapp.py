# -*- coding: utf-8 -*-

from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect


@route('/')
def redirect_to_login():
	redirect('/login')