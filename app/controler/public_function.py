# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
import time
from app.controler.power_API import get_business_json
import datetime
def get_first_letter(char):
   char=char.encode('GBK')
   
   if char<b"\xb0\xa1" or char>b"\xd7\xf9":
       return char.decode('GBK')[0:1].lower()
   if char<b"\xb0\xc4":
       return "a"
   if char<b"\xb2\xc0":
       return "b"
   if char<b"\xb4\xed":
       return "c"
   if char<b"\xb6\xe9":
       return "d"
   if char<b"\xb7\xa1":
       return "e"
   if char<b"\xb8\xc0":
       return "f"
   if char<b"\xb9\xfd":
       return "g"
   if char<b"\xbb\xf6":
       return "h"
   if char<b"\xbf\xa5":
       return "j"
   if char<b"\xc0\xab":
       return "k"
   if char<b"\xc2\xe7":
       return "l"
   if char<b"\xc4\xc2":
       return "m"
   if char<b"\xc5\xb5":
       return "n"
   if char<b"\xc5\xbd":
       return "o"
   if char<b"\xc6\xd9":
       return "p"
   if char<b"\xc8\xba":
       return "q"
   if char<b"\xc8\xf5":
       return "r"
   if char<b"\xcb\xf9":
       return "s"
   if char<b"\xcd\xd9":
       return "t"
   if char<b"\xce\xf3":
       return "w"
   if char<b"\xd1\x88":
       return "x"
   if char<b"\xd4\xd0":
       return "y"
   if char<b"\xd7\xf9":
       return "z"

def p_analyzeTJ(username,filternode):

    game_id=[]
    platform=[]
    channel_name=[]
    staff=[]
    agent=[]
    tj=""
    tjtype=""
    args = filternode

    jsons = json.loads(get_business_json("media_TJ.json", username))["body"]

    jsons = json.dumps(jsons,ensure_ascii=False)
    jsons = jsons.replace(" ","")

    resultjson=[]
    word=r'({[^}]*[^}]*})'
    jsons=",".join(re.findall(word,jsons))

    for x in xrange(0,len(args)):
      if args[x][0]=="tjtype":
        tjtype=args[x][1]
      if args[x][0]=="channel_name"   or args[x][0]=="agent" or args[x][0]=="staff" :
        if args[x][1]!="":
          word=r'({[^}]*"'+args[x][0]+'":"'+args[x][1].replace(',','"[^}]+}|{[^}]+"'+args[x][0]+'":"')+'"[^}]*})'
  
          jsons=",".join(re.findall(word,jsons))
       
        else:
          word=r'({[^}]*[^}]*})'
          jsons=",".join(re.findall(word,jsons))

    jsons=json.loads("["+jsons+"]")


    for x in xrange(0,len(jsons)):
      #game_id.append(jsons[x]["game_id"])
      #platform.append(jsons[x]["platform"])
      channel_name.append(jsons[x]['channel_name'])
      agent.append(jsons[x]['agent'])
      staff.append(jsons[x]['staff'])
    #game_id=list(set(game_id))
    #platform=list(set(platform))
    channel_name=list(set(channel_name))
    agent=list(set(agent))
    staff=list(set(staff))
    tj="["

    if tjtype=="channel_name":
      for x in xrange(0,len(channel_name)):

        tj+='{"channel_name":"'+str(channel_name[x])+'","initial":"'+str(get_first_letter(channel_name[x]))+'"},'
      tj=tj[0:-1]
    if tjtype=="agent":
      for x in xrange(0,len(agent)):
        tj+='{"agent":"'+str(agent[x])+'","initial":"'+str(get_first_letter(agent[x]))+'"},'
      tj=tj[0:-1]
    if tjtype=="staff":
      for x in xrange(0,len(staff)):
        tj+='{"staff":"'+str(staff[x])+'","initial":"'+str(get_first_letter(staff[x]))+'"},'
      tj=tj[0:-1]
    # if tjtype=="platform":
    #   for x in xrange(0,len(platform)):
    #     tj+='{"platform":"'+str(platform[x])+'","initial":"'+str(get_first_letter(platform[x]))+'"},'
    #   tj=tj[0:-1]
    tj=tj+']'
    

    return tj
