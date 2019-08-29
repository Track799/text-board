# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:39:24 2019

@author: Dell
"""

from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500