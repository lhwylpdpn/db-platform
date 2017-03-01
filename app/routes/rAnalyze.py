# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
from app.controler.cUser import CUser
from app.controler.power_API import login_in, passwd_update

analyzeBp = Blueprint('analyze', __name__, url_prefix="/analyze")


@analyzeBp.route('/mediaOverview')
def mediaOverview():
    return render_template("putAnalyze/mediaAnalyze/mediaOverview.html", title=U"媒体概览")



