# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random

from app.controler.power_API import get_business_json


analyzeBp = Blueprint('analyze', __name__, url_prefix="/analyze")


# 媒体概览相关
@analyzeBp.route('/mediaOverview')
def mediaOverview():
    return render_template("putAnalyze/mediaAnalyze/mediaOverview.html", title=U"媒体概览", sjs=random.random())



@analyzeBp.route('/mediaOverviewJsonTJ')
def mediaOverviewJsonTJ():
    jsons = json.loads(get_business_json("media_1.json", session["username"]))  # 字符串传化为json 对象
    return json.dumps(jsons["body"])


@analyzeBp.route('/mediaOverviewJson')
def mediaOverviewJson():
    jsons = json.loads(get_business_json("media_1.json", session["username"]))["body"]  # 字符串传化为json 对象 dict

    # 处理channel请求
    channel_name = request.args.get('channel_name')
    jsons_filter_channel_names = []
    if channel_name != "":
        channel_names = channel_name.split(",")
        for i in range(len(jsons)):
            if jsons[i]["channel_name"] in channel_names:
                jsons_filter_channel_names.append(jsons[i])
    else:
        jsons_filter_channel_names = jsons

    # 处理agent请求
    agent = request.args.get('agent')
    jsons_filter_agents = []
    if agent != "":
        agents = agent.split(",")
        for i in range(len(jsons_filter_channel_names)):
            if jsons_filter_channel_names[i]["agent"] in agents:
                jsons_filter_agents.append(jsons_filter_channel_names[i])
    else:
        jsons_filter_agents = jsons_filter_channel_names

    # 处理staff请求
    staff = request.args.get('staff')
    jsons_filter_staffs = []
    if staff != "":
        staffs = staff.split(",")
        for i in range(len(jsons_filter_agents)):
            if jsons_filter_agents[i]["staff"] in staffs:
                jsons_filter_staffs.append(jsons_filter_agents[i])
    else:
        jsons_filter_staffs = jsons_filter_agents

    # 按照日期 group by 筛选出有的日期
    newjson = []
    for ii in range(len(jsons_filter_staffs)):
        flag = 1
        for jj in range(len(newjson)):
            if newjson != []:
                if jsons_filter_staffs[ii]["date_time"] == newjson[jj]["date_time"]:
                    flag = 0
                    break
            else:
                flag = 1
        if flag:
            newjson.append({"date_time": jsons_filter_staffs[ii]["date_time"]})

    # 拼凑json串
    for ii in range(len(newjson)):
        newjson[ii]["channel_name"] = "groupby"   # 渠道
        newjson[ii]["agent"] = "groupby"          # 代理
        newjson[ii]["staff"] = "groupby"          # 负责人
        newjson[ii]["ad_click"] = 0.0               # 点击设备
        newjson[ii]["ad_action"] = 0.0              # 激活设备
        newjson[ii]["ad_action_new"] = 0.0          # 新增设备
        newjson[ii]["ad_account_new"] = 0.0         # 新增总账号
        newjson[ii]["double_new"] = 0.0             # 纯新增账号
        newjson[ii]["back_user"] = 0.0              # 回流账号
        newjson[ii]["paid_account"] = 0.0           # 付费账号
        newjson[ii]["spend"] = 0.0                  # 折后花费
        newjson[ii]["cumulative_flow"] = 0.0        # 累计流水
        newjson[ii]["dis"] = 0.0                    # 分成比例
        newjson[ii]["cumulative_moeny"] = 0.0       # 累计净收入

    # 讲数据累加带对应日期
    for jj in jsons_filter_staffs:
        for ii in range(len(newjson)):
            if jj["date_time"] == newjson[ii]["date_time"]:
                newjson[ii]["ad_click"] = newjson[ii]["ad_click"] + int(jj["ad_click"])                   # 点击设备
                newjson[ii]["ad_action"] = newjson[ii]["ad_action"] + int(jj["ad_action"])                  # 激活设备
                newjson[ii]["ad_action_new"] = newjson[ii]["ad_action_new"] + int(jj["ad_action_new"])        # 新增设备
                newjson[ii]["ad_account_new"] = newjson[ii]["ad_account_new"] + int(jj["ad_account_new"])     # 新增总账号
                newjson[ii]["double_new"] = newjson[ii]["double_new"] + int(jj["double_new"])                 # 纯新增账号
                newjson[ii]["back_user"] = newjson[ii]["back_user"] + int(jj["back_user"])                    # 回流账号
                newjson[ii]["paid_account"] = newjson[ii]["paid_account"] + int(jj["paid_account"])           # 付费账号
                newjson[ii]["spend"] = newjson[ii]["spend"] + float(jj["spend"])                                # 折后花费
                newjson[ii]["cumulative_flow"] = newjson[ii]["cumulative_flow"] + float(jj["cumulative_flow"])  # 累计流水
                newjson[ii]["dis"] = newjson[ii]["dis"] + float(jj["dis"])                                      # 分成比例
                newjson[ii]["cumulative_moeny"] = newjson[ii]["cumulative_moeny"] + float(jj["cumulative_moeny"])       # 累计净收入

    # 计算 fufeilv CPA ROI
    for ii in range(len(newjson)):
        if float(newjson[ii]["ad_account_new"]) != 0:
            newjson[ii]["fufeilv"] = newjson[ii]["paid_account"] / float(newjson[ii]["ad_account_new"])  # fufeilv
            newjson[ii]["CPA"] = newjson[ii]["spend"] / float(newjson[ii]["ad_account_new"])  # CPA

            newjson[ii]["fufeilv"] = round(newjson[ii]["fufeilv"], 2)
            newjson[ii]["CPA"] = round(newjson[ii]["CPA"], 2)

        else:
            newjson[ii]["fufeilv"] = '0'
            newjson[ii]["CPA"] = '0'

        if float(newjson[ii]["spend"]) != 0:
            newjson[ii]["ROI"] = newjson[ii]["cumulative_moeny"] / float(newjson[ii]["spend"])  # ROI
            newjson[ii]["ROI"] = round(newjson[ii]["ROI"]*100, 2)
        else:
            newjson[ii]["ROI"] = '0'

        # 将float 保留2位小数
        newjson[ii]["spend"] = round(newjson[ii]["spend"], 2)
        newjson[ii]["cumulative_flow"] = round(newjson[ii]["cumulative_flow"], 2)
        newjson[ii]["dis"] = round(newjson[ii]["dis"], 2)
        newjson[ii]["cumulative_moeny"] = round(newjson[ii]["cumulative_moeny"], 2)

    return json.dumps(newjson)  # 将dict 转化成 字符串


# 新增转化相关
@analyzeBp.route('/newTransfer')
def newTransfer():
    return render_template("putAnalyze/mediaAnalyze/newTransfer.html", title=U"新增转化", sjs=random.random())
#留存活跃相关
@analyzeBp.route('/mediaRetention')
def mediaRetention():
    return render_template("putAnalyze/mediaAnalyze/mediaRetention.html", title=U"留存活跃", sjs=random.random())

@analyzeBp.route('/mediaRetentionJson')
def mediaRetentionJson():
    jsons = json.loads(get_business_json("media_3.json", session["username"]))["body"]  # 字符串传化为json 对象 dict