from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ChatRoomAnnouncementContents, OpType, MediaType, ContentType, ApplicationType, TalkException, ErrorCode
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#==============================================================================#
# Login line
nn1 = LINE('')
waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#==============================================================================#
nn1MID = nn1.profile.mid
nn1Profile = nn1.getProfile()
nn1Settings = nn1.getSettings()
#==============================================================================#
nn1Poll = OEPoll(nn1)
nn1MID = nn1.getProfile().mid
admin = [nn1MID]
RfuBot=[nn1MID]
Bot = RfuBot
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','IOSIPAD']
mc = {"wr":{}}
sai = {'wc':{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
msg_dict = {}
temp_flood = {}
DDATE = {}
protectcancel =[]
protectJoin = []
protectInvite = []
protectKick = []
protectQr = []
protectkick = []
protectqr = []
protectjoin = []
protectinvite = []
autocancel = {}
#================================================#
autorejit = {
    "autoJoin":False,
    'autoCancel':{"on":True,"members":3},
}    
spamc = {
    "spamcall": False, 
}
commant = {
     "com":False,
}     
set = {"spamcall": False,"wc":{}}
autobl = {
    "autoblock":True,
    "autoaddf":True, 
}    
welcomes = {
    "Welcome":True, 
    "Wc":False, 
    "lv":False,
    "Leave":True, 
    "wcsti2":False, 
}    
sets = {
    "pictsa":False, 
    "sendpict": {},
    "gpict": False,
    "gilstpict": {},
    "pict": False,
    "ilstpict": {},
    "inv":{},
    "wc":{},
    "leave":{},
    "spamGroup":True, 
    "tagsticker": False,
    "Sticker": False,
    "autoJoinTicket": False,
    "tagkick":False,
    "Api": False,
    "autoLeave":True,
    "changeGroupPicture": [],
    "changePictureProfile": False,
    "autoRead": False,
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "readerSticker": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
}
autolike = {
  "autolike":True
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "วิธีตั้งแทค \n ตั้งแทค ข้อความที่ต้องการ",
    "comment": "ออโต้ไลค์  by   ™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯ ",
    "add": "ยินดีที่ได้รู้จักนะครับ 😃\nรับแอดละน้า. >_<",
    "wctext": "ยินดีต้อนรับเข้ากลุ่มนะครับ 😃",
    "lv": "บ๊ายบาย >< ขอให้เธอโชคดีงับ >_<",
    "b": "🐱 บัญชีนี้ถูกป้องกันด้วย ™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯ ระบบได้บล็อคบัญชีคุณอัตโนมัติ 🐱",
    "m": "🐱 สวัสดี เรามุดลิ้งมานะ 🐱",
}
apalo = {
    "bc":{},
    "bc1":{},
    "bc2":{},
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#66FFFF","t": "#000000"}
sets1 = {'autoCancel':{"on":True,"members":10}}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hnn2o = {
    "savefile": False,
    "namefile": "",
}

user1 = nn1MID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = nn1.getProfile() 
backup = nn1.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = nn1Profile.displayName
settings["myProfile"]["statusMessage"] = nn1Profile.statusMessage
settings["myProfile"]["pictureStatus"] = nn1Profile.pictureStatus
cont = nn1.getContact(nn1MID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = nn1.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = nn1Profile.statusMessage
ProfileMe["pictureStatus"] = nn1Profile.pictureStatus
coverId = nn1.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("max.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Max2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        nn1.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    nn1.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    nn1.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = nn1.getContact(mid)
    if contact.videoProfile == None:
        nn1.cloneContactProfile(mid)
    else:
        profile = nn1.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        nn1.updateProfile(profile)
        pict = nn1.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = nn1.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = nn1.getProfileDetail(mid)['result']['objectId']
    nn1.updateProfileCoverById(coverId)
def backupProfile():
    profile = nn1.getContact(nn1MID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = nn1.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = nn1.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        nn1.updateProfileAttribute(8, profile.pictureStatus)
        nn1.updateProfile(profile)
    else:
        nn1.updateProfile(profile)
        pict = nn1.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = nn1.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    nn1.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        nn1.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = nn1.getGroup(msg.to).name
    sd = nn1.waktunjir()
    nn1.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = nn1.getContact(to)
        profile = nn1.profile
        profileName = nn1.profile
        profileStatus = nn1.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        nn1.updateProfile(profileName)
        nn1.updateProfile(profileStatus)
        profile.pictureStatus = nn1.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if nn1.getProfileCoverId(to) is not None:
            nn1.updateProfileCoverById(nn1.getProfileCoverId(to))
        nn1.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return nn1.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        nn1.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
#----------------------------------------------------------------------------#        
def nn4(to, text):
    s = temp["te"]
    a = temp["t"]
    cover = nn1.getProfileCoverURL(nn1MID)
    warna1 = ("#000000")
    warna2 = ("#FF6600")
    warnanya1 = warna1
    warnanya2 = warna2
    data = {
    "type": "flex",
    "altText": "™TANBOTNEVERDIE✯",
    "contents": {
    "type": "bubble",
    "styles": {
    "body": {
    "backgroundColor":warnanya1
    }
    },    
    "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
    {
    "type": "box",
    "layout": "horizontal",
    "contents": [
    {
    "type": "image",
    "url":  "https://www.img.live/images/2019/09/12/images13.jpg",
    "size":"full",
    "aspectRatio":"20:13",
    "aspectMode":"cover"
    },
    ]
    },
    {
    "type": "separator",
    "color": "#CC0000"
    },
    {
    "type": "text",
    "text": text,
    "color":"#66FFFF",
    "gravity": "center",
    "align":"center",
    "wrap": True,
    "size": "xl"
    },
    {
    "type": "separator",
    "color": "#FF6600"
    },
    {
    "type":"button",
    "style": "primary",
    "height": "sm",
    "color": "#FF6600",
    "action": {
    "type": "uri",
    "label": "สนใจบอทติดต่อ",
    "uri": "line://ti/p/~"+nn1.getProfile().userid,
    }
    },
    ]
    }
    }
    }
    sendTemplate(to,data)        
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(nn1.getContact(nn1MID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus)
        ticket = "https://line.me/ti/p/~steveneverdie002"
        nn1.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nn1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def messageTime():
    global DDATE
    while True:
        date = subprocess.getoutput('date +"%H:%M:%S"')
        for x in DDATE:
            if x == date:
                groups = nn1.getGroupIdsJoined()
                for group in groups:
                    nn1.sendMessage(group, DDATE[x])
       
threads = threading.Thread(target=messageTime)
threads.daemon = True
threads.start()
def nn2(to, text):
    s = temp["te"]
    a = temp["t"]
    cover = nn1.getProfileCoverURL(nn1MID)
    data = {
    "type": "flex",
    "altText": "™TANBOTMEVERDIE✯͜͡❂➣",
    "contents": {
    "type": "bubble",
    "styles": {
    "body": {
    "backgroundColor":a
    }
    },    
    "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
    {
    "type": "box",
    "layout": "horizontal",
    "contents": [
    {
    "type": "image",
    "url":  "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
    "size": "sm",
    },
    {
    "type": "separator",
    "color": "#66FFFF"
    },
    {
    "type": "image",
    "url":  "https://www.img.live/images/2019/09/12/images13.jpg",
    "size": "sm",
    },
    ]
    },
    {
    "type": "separator",
    "color": "#66FFFF"
    },
    {
    "type": "text",
    "text": "™TANBOTNEVERDIE✯͜͡❂➣",
    "color": s,
    "weight": "bold",
    "align":"center",
    "size": "xl"
    },
    {
    "type": "separator",
    "color": "#66FFFF"
    },
    {
    "type":"text",
    "text": " ",
    },
    {
    "type": "text",
    "text": text,
    "color":s,
    "gravity": "center",
    "align":"center",
    "wrap": True,
    "size": "lg"
    },
    {
    "type":"text",
    "text": " ",
    },
    {
    "type":"button",
    "style": "primary",
    "height": "sm",
    "color": "#FF6600",
    "action": {
    "type": "uri",
    "label": "™TANBOTNEVERDIE✯",
    "uri": "line://ti/p/~"+nn1.getProfile().userid,
    }
    },
    ]
    }
    }
    }
    sendTemplate(to,data)        
def nn5(to, text):
    s = temp["te"]
    a = temp["t"]
    warna1 = ("#00FFcc","#FF9999","#009999","#666666","#FF1493","#FFFF00","#50B1493","#66600CC","#00FF00","FF0033")
    warna2 = ("#FF0033","#00FF00","#6600CC","#50B4F5","#FFFF00","#FF1493","#666666","#009999","#FF9999","#00FFcc")
    warnanya1 = random.choice(warna1)
    warnanya2 = random.choice(warna2)
    data = {
    "type": "flex",
    "altText": text,
    "contents": {
    "type": "bubble",
    "styles": {
    "body": {
    "backgroundColor":a
    }
    },
    "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
    {
    "type": "text",
    "text": text,
    "color":s,
    "gravity": "center",
    "wrap": True,
    "size": "sm"
    }
    ]
    }
    }
    }
    sendTemplate(to,data)
def nn3(to, nn3):
    data={
"type": "flex",
"altText": nn3,
"contents": {
"type": "bubble",
"styles": {
"footer": {"backgroundColor": "#000000"},
},
"footer": {
"type": "box",
"layout": "vertical",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
"size": "md"
},
{
"type": "text",
"text": nn3,
"color":"#66FFFF",
"gravity": "center",
"align":"center",
"wrap": True,
"size": "md"
},
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
"size": "md"
},
]
}
]
}
}
}
    sendTemplate(to, data)
#----------------------------------------------------------------------------#    
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "「{}」\nต่ะเอ๋ ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(nn1.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        nn1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        nn1.sendMessage(to, "[ INFO ] Error :\n" + str(error))		
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@nn1  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    nn1.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(nn1.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + nn1.getContact("u8b4c22de6d4a1e18190ae14f76465d66").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = nn1.genOBSParams({'oid': nn1MID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = nn1.server.postContent('{}/talk/vp/upload.nhn'.format(str(nn1.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        nn1.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = nn1.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = nn1.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    nn1.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nn1.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nn1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = nn1.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        nn1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nn1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d สัปดาห์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def restartBot():
    print ("RESETBOT..")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global stickers
    with open("sticker1.json","r") as fp:
        stickers = json.load(fp)
    with open("sticker2.json","r") as fp:
        stickerz = json.load(fp)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    nn1.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': nn1.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + nn1.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    nn1.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            nn1.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]
def commandMidContact(to, mid, cmd):
    if cmd in ["ชื่อเรา","mid","คทเรา","ตัสเรา","ปกเรา","รูปเรา","วีดีโอเรา"]:
        if cmd == "mid":
            return nn1.sendMessage(to, mid)
        if cmd == "คทเรา":
            return nn1.sendContact(to, mid)
        if cmd == "ชื่อเรา":
            return nn1.sendMessage(to, nn1.getContact(mid).displayName)
        if cmd == "ตัสเรา":
            return nn1.sendMessage(to, nn1.getContact(mid).statusMessage)
        if cmd == "รูปเรา":
            return nn1.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + nn1.getContact(mid).pictureStatus)
        if cmd == "ปกเรา":
            return nn1.sendImageWithURL(to, nn1.getProfileCoverURL(mid))
        if cmd == "วีดีโอเรา":
        	return nn1.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + nn1.getContact(mid).pictureStatus + "/vp")
    return
#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('max.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('Max2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
async def nn1Bot(op):
    try:
        if settings["restartPoint"] != None:
            nn1.sendMessage(settings["restartPoint"], 'ล็อคอินแล้วเรียบร้อย ><')
            settings["restartPoint"] = None
        if op.type == 0:
            return            
        if op.type == 5:
            if autobl["autoaddf"] == True:
                nn1.blockContact(op.param1)
            if autobl["autoblock"] == True:
                chivaree = "https://www.img.live/images/2019/09/12/images13.jpg"
                time.sleep(0.004)
                nn1.blockContact(op.param1)
                nn1.sendImageWithURL(op.param1, chivaree)
                nn1.sendMessage(op.param1, "🐷ระบบออโต้บล็อคทำงาน🐷\nบัญชีไลนนี้ถูกป้องกันด้วย\n™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯͜͡❂➣\nระบบได้บล็อคคุณ อัตโนมัติ\n\n😐หากสนใจติดบอทรอสักครู่😐")       
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if nn1.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bot:
                            nn1.reissueGroupTicket(op.param1)
                            X = nn1.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            nn1.updateGroup(X)
                            nn1.kickoutFromGroup(op.param1,[op.param2])
                            nn1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass                  
        if op.type == 11:    
        	if nn1.getGroup(op.param1).preventedJoinByTicket == False:
        	   nn2(op.param1,"👉พบการเปิดลิ้ง👈")
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bot:
                    try:
                        group = nn1.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            nn1.cancelGroupInvitation(op.param1,[_mid])
                            nn1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass  
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bot:
                    apalo["Talkwblacklist"][op.param2] = True
                    try:
                        if op.param3 not in apalo["Talkwblacklist"]:
                            nn1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return   
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bot:
                    apalo["Talkwblacklist"][op.param2] = True
                    nn1.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass     
#==========[ระบบกินห้อง เอจัง2019]================================================================
        if op.type == 13:
            if nn1MID in op.param3:
                chivaree2019 = nn1.getGroup(op.param1)
                if autorejit["autoJoin"] == True:
                    if autorejit["autoCancel"]["on"] == True:
                        if len(chivaree2019.members) <= autorejit["autoCancel"]["members"]:
                            nn1.rejectGroupInvitation(op.param1)
                        else:
                            nn1.acceptGroupInvitation(op.param1)
                    else:
                        nn1.acceptGroupInvitation(op.param1)
                elif autorejit["autoCancel"]["on"] == True:
                    if len(chivaree2019.members) <= autorejit["autoCancel"]["members"]:
                        time.sleep(random.uniform(4.5,5.0))
                        nn1.rejectGroupInvitation(op.param1)
                        print ("• ระบบกินห้องรันทำงานคับ •")
                    else:
                    	pass
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in apalo["Talkwblacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    nn1.cancelGroupInvitation(op.param1, matched_list)
#----------------------------------------------------------------------------#                                       
        if op.type == 15:
          if welcomes["Leave"] == True:
            if op.param2 in admin:
                return
            ginfo = nn1.getGroup(op.param1)
            contact = nn1.getContact(op.param2)
            name = contact.displayName
            pp = contact.pictureStatus
            s = name + " " + tagadd["lv"]
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#6600CC'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#FFFFFF",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line.me/ti/p/~steveneverdie002"
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 15:
          if welcomes["lv"] == True:
              ginfo = nn1.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["lv"]
              if msg != None:
                  contact = nn1.getContact(nn1MID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
        if op.type == 17:
          if welcomes["Welcome"] == True:
            if op.param2 in admin:
                return
            g = nn1.getGroup(op.param1)
            contact = nn1.getContact(op.param2)
            gname = g.name
            name = contact.displayName
            pp = contact.pictureStatus
            s = "ยินดีต้อนรับ:)\n"
            s += "\n• ชื่อกลุ่ม : {}".format(gname)
            s += "\n• ชื่อคนเข้ากลุ่ม : {}\n\n".format(name)
            s += tagadd["wctext"]
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#6600CC'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#FFFFFF",
                                "align": "center",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line.me/ti/p/~steveneverdie002"
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if welcomes["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = nn1.getGroup(op.param1)
            contact = nn1.getContact(op.param2)
            cover = nn1.getProfileCoverURL(op.param2)
            names = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    'styles': {
                        "body": {
                            "backgroundColor": '#6600CC'
                        },
                     },
                     "hero": {
                         "type":"image",
                         "url": cover,
                         "size":"full",
                         "aspectRatio":"20:13",
                         "aspectMode":"cover"
                     },
                     "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                             {
                                 "type": "image",
                                 "url": "https://profile.line-scdn.net/" + str(pp),
                                 "size": "lg"
                             },
                             {
                                 "type":"text",
                                 "text":" "
                             },
                             {
                                 "type":"text",
                                 "text":"{}".format(names),
                                 "size":"xl",
                                 "weight":"bold",
                                 "color":"#FFFFFF",
                                 "align":"center"
                             },
                             {
                                 "type": "text",
                                 "text": status,
                                 "wrap": True,
                                 "align": "center",
                                 "gravity": "center",
                                 "color": "#FFFFFF",
                                 "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if welcomes["wcsti2"] == True:
              ginfo = nn1.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["wc"]
              if msg != None:
                  contact = nn1.getContact(nn1MID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)  
#=====================================================================
        if op.type == 22:
            if sets["autoLeave"] == True:
                nn1.leaveRoom(op.param1)
        
        if op.type == 25:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.to not in unsendchat:
                unsendchat[msg.to] = {}
            if msg_id not in unsendchat[msg.to]:
                unsendchat[msg.to][msg_id] = msg_id
            msgdikirim[msg_id] = {"text":text}
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [nn1MID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass

        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != nn1MID: to = sender
                else: to = receiver
                if msg._from not in nn1MID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        nn1.sendMention(to, "คุณติดดำผมอยู่นะครับ @! :)","",[msg._from])
                        nn1.kickoutFromGroup(msg.to, [msg._from])

                if msg.contentType == 13:
                  if sets["inv"] == True:
                    mid = msg.contentMetadata['mid']
                    nn1.inviteIntoGroup(to, [mid])
                if msg.contentType == 13:
                  if apalo["Talkwblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          nn1.sendMessage(msg.to,"Sudah Ada")
                          apalo["Talkwblacklist"] = False
                      else:
                          apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
                          apalo["Talkwblacklist"] = False
                          nn1.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")
                  if apalo["Talkdblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
                          nn1.sendMessage(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว")
                          apalo["Talkdblacklist"] = False
                      else:
                          apalo["Talkdblacklist"] = False
                          nn1.sendMessage(msg.to,"Tidak Ada Dalam Da ftar Blacklist")                          
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        print ("AutoLikeCommat")
                        try:
                            if autolike["autolike"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                nn2(to,"🐱 ไม่ไลค์คับเจ็บนิ้ว 🐱")
                                if purl[1] not in wait['postId']:
                                    nn1.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                if commant["com"] == True:
                                    nn1.createComment(purl[0], purl[1], tagadd["commet"])
                                    wait['postId'].append(purl[1])
                                else:
                                    pass
                        except Exception as e:
                                if autolike["autolike"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    nn2(to,"🐱 ไม่ไลค์คับเจ็บนิ้ว 🐱")
                                    if purl[1] not in wait['postId']:
                                        nn1.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
                                    if commant["com"] == True:
                                        nn1.createComment(msg._from, purl[1], tagadd["commet"])
                                        wait['postId'].append(purl[1])
                                    else:pass                
        if op.type in [26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            if isValid != False:
                if msg.toType == 0 and sender != nn1MID: to = sender
                else: to = receiver
                if msg.contentType == 6:
                      if spamc["spamcall"] == True:
                           nn1.sendMessage(msg._from, "ระบบได้ทำการบล็อคคนรัวคอลเรียบร้อย\nจะทำการปลดบล็อคเองอัตโนมัติ ภายใน 1 นาที")
                           nn1.blockContact(msg._from)
                           time.sleep(60)
                           nn1.unblockContact(msg._from)

#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] ™TANBOTNEVERDIE✯͜͡❂➣")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nn1.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "help":
                    cover = nn1.getProfileCoverURL(nn1.profile.mid)
                    pp = nn1.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = nn1.getProfile().displayName
                    status = nn1.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={
					'type':'flex',
					'altText':"help message",
					'contents':{
					"type":"carousel",
					"contents":[
					{
					"hero":{
					"type":"image",
					"action":{
					"type":"uri","uri":"line://app/1643557392-pe8AQomG?type=profile"
					},
					"url":profile,"size":"full",
					"aspectMode":"cover",
					"aspectRatio":"1:1"},
					"styles":{
					"body":{"backgroundColor":"#000000"
					},
					"header":{"backgroundColor":"#000000"
					}
					},
					"type":"bubble","body":{
					"type":"box","layout":"vertical",
					"spacing":"xs",
					"contents":[
					{"type":"box",
					"margin":"md",
					"layout":"baseline",
					"contents":[
					{
					"type":"text",
					"size":"xl",
					"align":"end",
					"color":"#CC0000",
					"text":"™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯"
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xxs",
					"action":{
					"type":"uri",
					"uri":"https://line.me/ti/p/~"+nn1.getProfile().userid,
					},
					"url":"https://www.img.live/images/2019/09/12/deep-web-dark-web-internet-spam-hack-cyber-security.jpg"
					},
					{
					"type":"image",
					"size":"xxs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=คำสั่ง"
					},
					"url":"https://www.img.live/images/2019/09/12/sytech-dr-1.png",
					},
					{
					"type":"image",
					"size":"xxs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ข้อมูล"
					},
					"url":"https://www.img.live/images/2019/09/12/sytech-dr-1.png",
					},
					{
					"type":"image",
					"size":"xxs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เชคค่า"
					},
					"url":"https://www.img.live/images/2019/09/12/sytech-dr-1.png",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ติดต่อคนสร้างบอท"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"คำสั่ง"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ข้อมูล"
					},
					{
					"type":"text",
					"size":"xs",
					"color":"#66FFFF",
					"text":"เชคค่า"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ออน"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=รีบอท"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=me"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ออน"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"รีบอท"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"me"
					}
					]
					}
					]
					}
					]
					}
					},
					{
					"type":"bubble",
					"styles":{
					"body":{"backgroundColor":"#000000"
					},
					"header":{"backgroundColor":"#000000"
					}
					},
					"body":{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"baseline",
					"contents":[
					{
					"type":"icon",
					"size":"md",
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					},
					{
					"type":"icon",
					"size":"md",
					"url":"https://i.ibb.co/Scv2SyN/battery-Phones.png"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"flex":0,
					"text":"  ᴬᴵˢ 4G"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"align":"end",
					"text":"⏰ 22/10/19 ™"
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ข้อมูล"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=รูปเรา"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=คทเรา"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ข้อมูล"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"รูปเรา"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"คทเรา"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ไอดีเรา"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ชื่อเรา"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตัสเรา"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ไอดีเรา"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ชื่อเรา"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตัสเรา"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=รูปเรา"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=วีดีโอเรา"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ปกเรา"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"รูปเรา"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"วีดีโอเรา"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ปกเรา"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=รีบอท"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ออน1"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=/ลบรัน"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"รีบอท"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ออน1"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"/ลบรัน"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เชค"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ยกเชิญ"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ทัก"
					},
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เชค"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ยกเชิญ"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ทัก"
					}
					]
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"md",
					"contents":[
					{
					"type":"text",
					"text":"❀❀❀",
					"align":"center",
					"size":"xs",
					"weight":"bold",
					"color":"#F8F8FF",
					"wrap":True
					}
					]
					}
					]
					}
					]
					}
					},
					{
					"type":"bubble",
					"styles":{
					"body":{"backgroundColor":"#000000"
					},
					"header":{"backgroundColor":"#000000"
					}
					},
					"body":{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"baseline",
					"contents":[
					{
					"type":"icon",
					"size":"md",
					"url":"https://www.img.live/images/2019/09/12/343321.jpg",
					},
					{
					"type":"icon",
					"size":"md",
					"url":"https://i.ibb.co/Scv2SyN/battery-Phones.png"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"flex":0,
					"text":"  ᴬᴵˢ 4G"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"align":"end",
					"text":"⏰ 22/10/19 ™"
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=แทค"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ก๊อป"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=กลับร่าง"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"แทค"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ก๊อป"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"กลับร่าง"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งapi"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ล้างapi"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เชคapi"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งapi"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ล้างapi"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เชคapi"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=stag"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=แปรงคท"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ยูทูป"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"stag"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"แปรงคท"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ยูทูป"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=รูป"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เพลสโต"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=image"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"รูป"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เพลสโต"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"image"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งรูปโปรไฟล์"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ประกาศ"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ยกเลิก"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งโปรไฟล์"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ประกาศ"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ยกเลิก"
					}
					]
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"md",
					"contents":[
					{
					"type":"text",
					"text":"❀❀❀",
					"align":"center",
					"size":"xs",
					"weight":"bold",
					"color":"#F8F8FF",
					"wrap":True
					}
					]
					}
					]
					}
					]
					}
					},
					{
					"type":"bubble",
					"styles":{
					"body":{"backgroundColor":"#000000"
					},
					"header":{"backgroundColor":"#000000"
					}
					},
					"body":{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"baseline",
					"contents":[
					{
					"type":"icon",
					"size":"md",
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					},
					{
					"type":"icon",
					"size":"md",
					"url":"https://i.ibb.co/Scv2SyN/battery-Phones.png"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"flex":0,
					"text":"  ᴬᴵˢ 4G"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"align":"end",
					"text":"⏰ 22/10/19 ™"
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ดำ"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ขาว"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เชคดำ"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ดำ"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ขาว"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เชคดำ"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ดำ"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ล้าง"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=คทดำ"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ดำ"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ล้าง"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"คทดำ"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งต้อนรับ"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งคนออก"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งแอด"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งต้อนรับ"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งคนออก"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งแอด"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งแทค"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งคอมเม้น"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งค้างเชิญ"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งแทค"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งคอมเม้น"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งค้างเชิญ"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งมุดลิ้ง"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งคนบล็อค"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ล้างดำ"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งมุดลิ้ง"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งคนบล็อค"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ล้างดำ"
					}
					]
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"md",
					"contents":[
					{
					"type":"text",
					"text":"❀❀❀",
					"align":"center",
					"size":"xs",
					"weight":"bold",
					"color":"#F8F8FF",
					"wrap":True
					}
					]
					}
					]
					}
					]
					}
					},
					{
					"type":"bubble",
					"styles":{
					"body":{"backgroundColor":"#000000"
					},
					"header":{"backgroundColor":"#000000"
					}
					},
					"body":{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"baseline",
					"contents":[
					{
					"type":"icon",
					"size":"md",
					"url":"https://www.img.live/images/2019/09/12/343321.jpg"
					},
					{
					"type":"icon",
					"size":"md",
					"url":"https://i.ibb.co/Scv2SyN/battery-Phones.png"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"flex":0,
					"text":"  ᴬᴵˢ 4G"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"align":"end",
					"text":"⏰ 22/10/19 ™"
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดแทค"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดแทค2"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดแทค3"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดแทค"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดแทค2"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดแทค3"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดไลค์"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดคอมเม้น"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดบล็อค"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดไลค์"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดคอมเม้น"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดบล็อค"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดแอด"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดกันรัน"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดยกเลิก"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดแอด"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดกันรัน"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดยกเลิก"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดต้อนรับ"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดต้อนรับ2"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดคนออก"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดต้อนรับ"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดต้อนรับ2"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดคนออก"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดติ๊คนเข้า"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดติ๊กคนออก"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดติ๊กใหญ่"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดติ๊กคนเข้า"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดติ๊กคนออก"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดติ๊กใหญ่"
					}
					]
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"md",
					"contents":[
					{
					"type":"text",
					"text":"❀❀❀",
					"align":"center",
					"size":"xs",
					"weight":"bold",
					"color":"#F8F8FF",
					"wrap":True
					}
					]
					}
					]
					}
					]
					}
					},
					{
					"type":"bubble",
					"styles":{
					"body":{"backgroundColor":"#000000"
					},
					"header":{"backgroundColor":"#000000"
					}
					},
					"body":{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"baseline",
					"contents":[
					{
					"type":"icon",
					"size":"md",
					"url":"https://www.img.live/images/2019/09/16/343321.jpg"
					},
					{
					"type":"icon",
					"size":"md",
					"url":"https://i.ibb.co/Scv2SyN/battery-Phones.png"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"flex":0,
					"text":"  ᴬᴵˢ 4G"
					},
					{
					"type":"text",
					"size":"xxs",
					"color":"#66FF66",
					"align":"end",
					"text":"⏰ 22/10/19 ™"
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เปิดมุดลิ้ง"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งติ๊กคนแอด"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ลบติ๊กคนแอด"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เปิดมุดลิ้ง"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งติ๊กคนแอด"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ลบติ๊กคนแอด"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งติ๊กคนแทค"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ลบติ๊กคนแทค"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งติ๊กคนเข้า"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งติกคนแทค"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ลบติ๊กคนแทค"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งติ๊กคนเข้า"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ตั้งติ๊คนออก"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ลบติ๊กคนออก"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ลบติ๊กคนเข้า"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ตั้งติ๊กคนออก"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ลบติ๊กคนออก"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ลบติ๊กคนเข้า"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เขียน1"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ไอดีไลน์"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ดึง"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เขียน1"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ไอดีไลน์"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ดึง"
					}
					]
					}
					]
					},
					{
					"type":"box",
					"layout":"vertical",
					"spacing":"xs",
					"contents":[
					{
					"type":"box",
					"layout":"horizontal",
					"contents":[
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=บล็อค"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=เพิ่มเพื่อน"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					},
					{
					"type":"image",
					"size":"xs",
					"action":{
					"type":"uri",
					"uri":"line://app/1643727178-0XPGAaRX?type=text&text=ลบเพื่อน"
					},
					"url":"https://www.img.live/images/2019/09/12/343316.jpg",
					}
					],
					"flex":1
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"xxl",
					"contents":[
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"บล็อค"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"เพิ่มเพื่อน"
					},
					{
					"type":"text",
					"size":"xs",
					"align":"center",
					"color":"#66FFFF",
					"text":"ลบเพื่อน"
					}
					]
					},
					{
					"type":"box",
					"layout":"horizontal",
					"spacing":"md",
					"contents":[
					{
					"type":"text",
					"text":"❀❀❀",
					"align":"center",
					"size":"xs",
					"weight":"bold",
					"color":"#F8F8FF",
					"wrap":True
					}
					]
					}
					]
					}
					]
					}
					}
					]
					}
					}
                    sendTemplate(to, data)
                if text == "ตั้งโอน":
                   sets["pictsa"]=True
                   nn2(to, "กรุณาส่งรูปมา")
                if text == "บช" or text == "บัญชี":
                   if sets["sendpict"] == {}:
                       nn1.sendMessage(to, "คุณยังไม่ได้ตั้งรูป กรุณาพิม 'ตั้งโอน'ด้วย")
                   else:
                       nn1.sendImage(to, str(sets["sendpict"]))
                if text.lower().startswith('sh'):
                    text = msg.text.split(' ')
                    keyword = msg.text.replace(text[0] + ' ','')
                    nn1.sendMessage(to, subprocess.getoutput(keyword))
                elif text.lower().startswith('ทัก '):
                            ayudha = text.split(' ')
                            byudha = text.replace(ayudha[0] + ' ','')
                            cyudha = int(ayudha[1])
                            for var in range(cyudha):
                                RhyN_(to,to)
#--------------------------------------------------------------------------------------------------------------------#                                        
                elif msg.text.lower().startswith('ยกเลิก '):
                            nn1.unsendMessage(msg.id)
                            j = int(msg.text.split(' ')[1])
                            a = [nn1.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                            if len(msg.text.split(' ')) == 2:
                                h = wait['Unsend'][msg.to]['B']
                                n = len(wait['Unsend'][msg.to]['B'])
                                for b in h[:j]:
                                    try:
                                        nn1.unsendMessage(b)
                                        wait['Unsend'][msg.to]['B'].remove(b)
                                    except:pass
                                t = len(wait['Unsend'][msg.to]['B'])
                            if len(msg.text.split(' ')) >= 3:h = [nn1.unsendMessage(nn1.sendMessage(to,nn1.adityasplittext(msg.text,'s')).id) for b in a]
#--------------------------------------------------------------------------------------------------------#                            
                if text.lower() == "ประกาศ4":
                    ret = "วิธีการใช้ประกาศกำหนดเวลา :\n"
                    ret += "ประกาศ เวลา:นาที:วินาที;;ข้อความประกาศ\n"
                    ret += "ดูตัวอย่าง เช่น :\n"
                    ret += "ประกาศ4 08:30:00;;มอนิ่งครับ\n"
                    ret += "แบบนี้ก็จะประกาศตอนที่ 08:30:00\n"
                    nn1.sendMessage(to, str(ret))
#----------------------------------------------------------------------------#                    
                if text.lower() == "เปิดกันคอล":
                    spamc["spamcall"] = True
                    nn2(to, "🐱เปิดกันสแปมโทรเรียบร้อย🐱")
                if text.lower() == "ปิดกันคอล":
                    spamc["spamcall"] = False
                    nn2(to, "🐱ปิดกันสแปมโทรเรียบร้อย🐱")
#----------------------------------------------------------------------------#                    
                if  text.lower().startswith("อัพชื่อไว "):
                     keyword = msg.text.replace(msg.text.split(" ")[0] + " ", "")
                     keyword1 = "􀰂􀰂"
                     keyword2 = "�"
                     unname = "{}{}{}".format(keyword1,keyword,keyword2)
                     profile_A = nn1.getProfile()
                     profile_A.displayName = unname
                     nn1.updateProfile(profile_A)
                     nn1.sendMessage(to, "อัพชื่อเป็น {n} ชื่อพิเศษเรียบร้อย".format(n=unname))
#----------------------------------------------------------------------------#                     
                elif text.lower() == "ลบรัน" or text.lower() == "/ลบรัน":
                      ag = nn1.getGroupIdsInvited()
                      k = len(ag)//30
                      nn1.sendMessage(msg.to,"กำลังดำเนินการรอสักครู่...")
                      num=1
                      for i in range(k+1):
                         for j in ag[i*30 : (i+1)*30]:
                            nn1.acceptGroupInvitation(j)
                            time.sleep(random.uniform(0.4,0.5))
                            nn1.leaveGroup(j)
                            print ("[Command] "+str(num)+" => "+str(len(ag))+" cancel members")
                            num = num+1
                         time.sleep(random.uniform(0.30,0.30))
                         print ("[ ยกเลิกจำนวน {} กลุ่มเรียบร้อยแล้ว ]".format(str(len(ag))))
                      nn1.sendMessage(to,"ยกเลิกจำนวน {} กลุ่มเรียบร้อยแล้ว".format(str(len(ag))))
#----------------------------------------------------------------------------#                      
                if text.lower() == "ลบแชท":
                    nn1.removeAllMessages(op.param2)
                    time.sleep(0.30)
                    nn2(to, "ลบแชทสำเร็จแล้ว")
#----------------------------------------------------------------------------#                    
                if text.lower() == "ประกาศ":
                    sa="วิธีใช้ ประกาศกลุ่ม >\\<"
                    sa+="\n- ประกาศ ข้อความ/ไอดีไลน์"
                    sa+="\nตัวอย่าง >\\<"
                    sa+="\n- ประกาศ มอนิ่ง/nn33.h"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "™TANBOTNEVERDIE✯", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}
                    sendTemplate(to,data)
#----------------------------------------------------------------------------#                    
                if text.lower() == "ตั้งapi":
                    sa = "วีธีใช้ api >\\<"
                    sa += "\n- ตั้งapi คีย์เวิร์ด;;ตอบกลับ"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- ตั้งapi เทส;;เทสทำไม"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "™TANBOTNEVERDIE✯", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}
                    sendTemplate(to,data)
#----------------------------------------------------------------------------#                    
                if text.lower() == "stag":
                    sa = "วิธีใช้ stag >\\<"
                    sa += "\n- stag [เลขที่ต้องการ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- stag 1 @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "™TANBOTNEVERDIE✯", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}
                    sendTemplate(to,data)
#----------------------------------------------------------------------------#                    
                if text.lower() == "สะกดจิต":
                    sa = "วิธีใช้ สะกดจิต >\\<"
                    sa += "\n- สะกดจิต [ข้อความ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- สะกดจิต Fc NN @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "™TANBOTNEVERDIE✯", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}
                    sendTemplate(to,data)
#----------------------------------------------------------------------------#                    
                if text.lower() == "เชคค่า" or text.lower() == "set":
                    sas = "🐱 Settings 🐱"
                    if autobl["autoaddf"] == True: sa = "\n🔊 ออโต้บล็อค1 ( เปิด )"
                    else:sa = "\n🚫 ออโต้บล็อค1 ( ปิด )"
                    if autobl["autoblock"] == True: sa += "\n🔊 ออโต้บล็อค2 ( เปิด )"
                    else:sa += "\n🚫 ออโต้บล็อค2 ( ปิด )"
                    if autorejit["autoCancel"]["on"] == True: sa +="\n🔊 ยกเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"])
                    else:sa += "\n🚫 ปฏิเสธกลุ่มเชิญ ( ปิด )"
                    if tagadd["tags"] == True: sa += "\n🔊 ตอบกลับคนแทค ( เปิด )"
                    else:sa += "\n🚫 ตอบกลับคนแทค ( ปิด )"
                    if tagadd["tagss"] == True: sa += "\n🔊 ตอบกลับคนแทค2 ( เปิด )"
                    else:sa += "\n🚫 ตอบกลับคนแทค2 ( ปิด )"
                    if sets["autoLeave"] == True: sa += "\n🔊 กันดึงแชทรวม ( เปิด )"
                    else:sa += "\n🚫 กันดึงแชทรวม ( ปิด )"
                    if sets["tagsticker"] == True: sa += "\n🔊 แทคสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n🚫 แทคสติ๊กเกอร์ ( ปิด )"
                    if autolike["autolike"] == True: sa += "\n🔊 ออโต้ไลค์ ( เปิด )"
                    else:sa += "\n🚫 ออโต้ไลค์ ( ปิด )"
                    if commant["com"] == True: sa += "\n🔊 คอมเม้นโพส ( เปิด )"
                    else:sa += "\n🚫 คอมเม้นโพส ( ปิด )"
                    if welcomes["Welcome"] == True: sa += "\n🔊 ต้อนรับคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n🚫 ต้อนรับคนเข้ากลุ่ม ( ปิด )"
                    if welcomes["Wc"] == True: sa += "\n🔊 ต้อนรับคนเข้ากลุ่ม2 ( เปิด )"
                    else:sa += "\n🚫 ต้อนรับคนเข้ากลุ่ม2 ( ปิด )"
                    if welcomes["wcsti2"] == True: sa += "\n🔊 ติ๊กคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n🚫 ติ๊กคนเข้ากลุ่ม ( ปิด )"
                    if welcomes["Leave"] == True: sa += "\n🔊 คนออกกลุ่ม ( เปิด )"
                    else:sa += "\n🚫 คนออกกลุ่ม ( ปิด )"
                    if welcomes["lv"] == True: sa += "\n🔊 ติ๊กคนออกกลุ่ม ( เปิด )"
                    else:sa += "\n🚫 ติ๊กคนออกกลุ่ม ( ปิด )"
                    if settings["unsendMessage"] == True: sa += "\n🔊 ตรวจจับยกเลิก ( เปิด )"
                    else:sa += "\n🚫 ตรวจจับยกเลิก ( ปิด )"
                    if settings["Sticker"] == True: sa += "\n🔊 ติ๊กใหญ่ ( เปิด )"
                    else:sa += "\n🚫 ติ๊กใหญ่ ( ปิด )"
                    if sets["Sticker"] == True: sa += "\n🔊 เชคโค๊ดสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n🚫 เชคโค๊ดสติ๊กเกอร์ ( ปิด )"
                    if sets["Api"] == True: sa += "\n🔊 ระบบApi ( เปิด )"
                    else:sa += "\n🚫 ระบบApi ( ปิด )"
                    if spamc["spamcall"] == True: sa += "\n🔊 ระบบป้องกันรัวคอล ( เปิด )"
                    else:sa += "\n🚫 ระบบป้องกันรัวคอล ( ปิด )"
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "hero": {
                                 "type":"image",
                                 "url": "https://www.img.live/images/2019/09/17/343285aaddd.jpg",
                                 "size":"full",
                                 "aspectRatio":"1:1",
                                 "aspectMode":"cover"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": sas,
                                        "color": "#CC0000",
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#66FFFF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
#--------------------------------------------------------------------------------------------------#                    
                elif text.lower() == 'clearban' or text.lower() == "ล้างดำ":
                      apalo["Talkblacklist"] = {}
                      nn2(to, "🐱ล้างดำ สำเร็จ🐱")
#--------------------------------------------------------------------------------------------------#                      
                if text.lower() == 'ยกเชิญ':
                                try:
                                    if msg.toType == 2:
                                        group = nn1.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//30
                                        nn1.sendMessage(msg.to,"[ ยกค้างเชิญ จำนวน {} คน] \nรอสักครู่...".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*30 : (i+1)*30]:
                                                time.sleep(random.uniform(0.7,0.6))
                                                nn1.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            nn1.sendMessage(receiver,"พัก 10-15 วินาที แล้ว จะทำการ ยกต่อ 30 คน")
                                            time.sleep(random.uniform(15,10))
                                        nn1.sendMessage(receiver,"[ ยกค้างเชิญ จำนวน {} คน เรียบร้อยแล้ว]".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        #nn1.sendMessage(receiver, None, contentMetadata={"STKID": "119","STKPKGID": "1","STKVER": "100" }, contentType=7)
                                        gname = nn1.getGroup(receiver).name
                                        nn1.sendMessage(Notify,"[ ยกค้างเชิญ >> "+gname+"  <<] \n จำนวน {} คน เรียบร้อยแล้ว".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                except:        
                                    nn1.sendMessage(msg.to, "สำเร็จแล้ว")
#--------------------------------------------------------------------------------------------------#                                    
                elif text.lower() == "คทดำ":
                    if msg._from in nn1MID:
                        if apalo["Talkblacklist"] == []:
                            nn2(to, "🐱 ไม่มีคท.คนติดดำ  🐱")
                        else:
                            for bl in apalo["Talkblacklist"]:
                                 nn1.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
#--------------------------------------------------------------------------------------------------#                                 
                elif msg.text.lower().startswith("ตั้งสีme "):
                            text_ = removeCmd("ตั้งสีme", text)
                            try:
                                temp["t"] = text_
                                nn2(to,"🐱 โค๊ดสี 🐱\nคือ : " + text_)
                            except:
                                nn2(to,"สำเเร็จแล้ว")
                elif msg.text.lower().startswith("สีอักษร "):
                            text_ = removeCmd("สีอักษร", text)
                            try:
                                temp["te"] = text_
                                nn2(to,"🐱 โค๊ดสี 🐱\nคือ : " + text_)
                            except:
                                nn2(to,"สำเเร็จแล้ว")
                                
                elif msg.text.lower() == "รหัสสี":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="**ตัวอย่างที่1**\nคำสั่งเปลี่ยนสี me\nพิม'ตั้งสีme #333333'\n**ตัวอย่างที่2**\nคำสั่งเปลี่ยนสี tag\nพิม'ตั้งสีแทค #333333'"
                            nn1.sendImageWithURL(to,c)
                            nn1.sendImageWithURL(to,p)
                            nn2(to,m)
                            
                elif msg.text.lower().startswith("ตั้งบล็อค "):
                            text_ = removeCmd("ตั้งบล็อค", text)
                            try:
                                tagadd["b"] = text_
                                nn2(to,"🐱 ตั้งบล็อคอัตโนมัติ 🐱\nคือ : " + text_)
                            except:
                                nn2(to,"สำเเร็จแล้ว")
                                
                elif text.lower().startswith("ตั้งค้างเชิญ "):
                            text_ = removeCmd("ตั้งค้างเชิญ", text)
                            try:
                                settings["autoCancel"]["members"] = text_
                                nn2(to,"🐱 ตั้งยกค้างเชิญ 🐱\nจำนวน : " + text_)
                            except:
                                nn2(to,"สำเเร็จแล้ว")
#-----------------------------[modiflie by: nn]--------------------------------------#                  
                if text.lower() == "คำสั่ง":
                    sender_profile = nn1.getContact(sender)
                    COOZ = ("#66FFFF")
                    COOZ2 = ("#000000")                    
                    COOZ3 = ("#000000")                    
                    COOZ4 = ("#000000")                    
                    dataProfile = [
                        {
                            "type": "bubble",
                            "styles": {
                                "header": {"backgroundColor": COOZ2},
                                "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#000000"},
                                "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                            },
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "type": "image",
                                        "url": "https://www.img.live/images/2019/09/17/343316.jpg",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        },  
                                        {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                            {
                                            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                                            "type": "image"
                                        },
                                    ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                            {
                                            "text": "🐱 คำสั่งบอทจ้าา 🐱",
                                            "size": "xl",
                                            "align": "center",
                                            "color": "#FF0000",
                                            'flex': 1,
                                            "weight": "bold",
                                            "type": "text"
                                            }
                                        ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                        {
                                            "url": "https://sv1.picz.in.th/images/2019/09/05/Znpb5u.jpunpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " me",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {    
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " /me",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " คท",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ไอดีเรา",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ชื่อเรา",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตัสเรา",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " รูปเรา",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                                                                                                                                                                                                                                                                                                  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " รูปวีดีโอเรา",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ปกเรา",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ข้อมูล",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " รีบอท",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ออน",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " /ลบรัน",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เชค",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                         
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " แทค",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"                                   
                                     }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                        "type": "icon",
                                        "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                        "size": "md"
                                            },
                                            {
                                        "type": "text",
                                        "text": "™TANBOTNEVERDIE✯͜͡❂➣",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                            },
                                            {
                                        "type": "spacer",
                                        "size": "md",
                                            }
                                        ]
                                    }
                                ]
                            }
                        },
                        {
                            "type": "bubble",
                            "styles": {
                                "header": {"backgroundColor": COOZ4},
                                "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#000000"},
                                "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                            },
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "type": "image",
                                        "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        },  
                                        {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                            {
                                            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                                            "type": "image"
                                        },
                                    ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                     
                                        "contents": [
                                            {
                                            "text": "🐱 คำสั่งบอทจ้าา 🐱",
                                            "size": "xl",
                                            "align": "center",
                                            "color": "#FF0000",
                                            'flex': 1,
                                            "weight": "bold",
                                            "type": "text"
                                            }
                                        ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {    
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ยกเชิญ",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ก็อป @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " กลับร่าง",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งapi [พิมเพื่อดูวิธี]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ล้างapi [คำที่จะลบ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เชคapi",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " stag [พิม'stag'เพื่อดูวิธี]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                                                                                                                                                                                                                                                                
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "แปรงคท [MID]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ยูทูป [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"                                        
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " image [text(ภาษาอังกฤษ)]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " รูป [ข้อความ(ภาษาไทย)]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " playstore [ชื่อแอพ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ยกเลิก [ใส่จำนวนที่จะยกเลิก]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"                                            
                                     }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                        "type": "icon",
                                        "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                        "size": "md"
                                            },
                                            {
                                        "type": "text",
                                        "text": "™TANBOTNEVERDIE✯͜͡❂➣",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                            },
                                            {
                                        "type": "spacer",
                                        "size": "md",
                                            }
                                        ]
                                    }
                                ]
                            }
                        },
                        {
                            "type": "bubble",
                            "styles": {
                                "header": {"backgroundColor": COOZ4},
                                "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#000000"},
                                "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                            },
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "type": "image",
                                        "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        },  
                                        {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                            {
                                            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                                            "type": "image"
                                        },
                                    ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                     
                                        "contents": [
                                            {
                                            "text": "🐱 คำสั่งบอทจ้าา 🐱",
                                            "size": "xl",
                                            "align": "center",
                                            "color": "#FF0000",
                                            'flex': 1,
                                            "weight": "bold",
                                            "type": "text"
                                            }
                                        ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {    
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ดำ ส่งคท.",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ขาว ส่งคท.",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ดำ @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ล้าง @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เชคดำ",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " คทดำ",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ล้างดำ",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                                                                                                                                                                                                                                                                
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งต้อนรับ [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งคนออก [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"                                        
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งแอด [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งแทค [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งคอมเม้น [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งค้างเชิญ [จำนวน]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งมุดลิ้ง [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งคนบล็อค [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"                                            
                                     }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                        "type": "icon",
                                        "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                        "size": "md"
                                            },
                                            {
                                        "type": "text",
                                        "text": "™TANBOTNEVERDIE✯͜͡❂➣",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                            },
                                            {
                                        "type": "spacer",
                                        "size": "md",
                                            }
                                        ]
                                    }
                                ]
                            }
                        },
                        { 
                            "type": "bubble",
                            "styles": {
                                "header": {"backgroundColor": COOZ4},
                                "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#000000"},
                                "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                            },
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "type": "image",
                                        "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        },  
                                        {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                            {
                                            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                                            "type": "image"
                                        },
                                    ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                     
                                        "contents": [
                                            {
                                            "text": "🐱 คำสั่งบอทจ้าา 🐱",
                                            "size": "xl",
                                            "align": "center",
                                            "color": "#FF0000",
                                            'flex': 1,
                                            "weight": "bold",
                                            "type": "text"
                                            }
                                        ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {    
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดมุดลิ้ง/ปิดมุดลิ้ง",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งติ๊กคนแอด",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "ลบติ๊กคนแอด",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "ตั้งติ๊กคนแทค",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ลบติ๊กคนแทค",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งติ๊กคนเข้า",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ลบติ๊กคนเข้า",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                                                                                                                                                                                                                                                                
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตั้งติ๊กคนออก",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ลบติ๊กคนออก",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"                                        
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เขียน [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ไอดีไลน์ [idline]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ดึง @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " บล็อค @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เพิ่มเพื่อน @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ลบเพื่อน @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"                                            
                                     }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                        "type": "icon",
                                        "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                        "size": "md"
                                            },
                                            {
                                        "type": "text",
                                        "text": "™TANBOTNEVERDIE✯͜͡❂➣",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                            },
                                            {
                                        "type": "spacer",
                                        "size": "md",
                                            }
                                        ]
                                    }
                                ]
                            }
                        },
                        {   
                            "type": "bubble",
                            "styles": {
                                "header": {"backgroundColor": COOZ4},
                                "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#000000"},
                                "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                            },
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "type": "image",
                                        "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        },  
                                        {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                            {
                                            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                                            "type": "image"
                                        },
                                    ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                     
                                        "contents": [
                                            {
                                            "text": "🐱 คำสั่งบอทจ้าา 🐱",
                                            "size": "xl",
                                            "align": "center",
                                            "color": "#FF0000",
                                            'flex': 1,
                                            "weight": "bold",
                                            "type": "text"
                                            }
                                        ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {    
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " แอด",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "ไอดีกลุ่ม",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "ชื่อกลุ่ม",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "รูปกลุ่ม",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ข้อมูลกลุ่ม",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " คนในห้อง",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " กลุ่มทั้งหมด",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                                                                                                                                                                                                                                                                
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "ลิ้ง",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "เปิดลิ้ง",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"                                        
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "ปิดลิ้ง",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "เพื่อน",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " อัพชื่อ [ข้อความ]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " อัพตัส [จำนวน]",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " อัพรูปโปร",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                            
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": "อัพรูปกลุ่ม",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"                                            
                                     }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                        "type": "icon",
                                        "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                        "size": "md"
                                            },
                                            {
                                        "type": "text",
                                        "text": "™TAMBOTNEVERDIE✯͜͡❂➣",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                            },
                                            {
                                        "type": "spacer",
                                        "size": "md",
                                            }
                                        ]
                                    }
                                ]
                            }
                        },
                        {   
                            "type": "bubble",
                            "styles": {
                                "header": {"backgroundColor": COOZ3},
                                "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#000000"},
                                "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                            },
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "type": "image",
                                        "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        },  
                                        {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                            {
                                            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                                            "type": "image"
                                        },
                                    ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                   
                                        "contents": [
                                            {
                                            "text": "🐱 คำสั่งบอทจ้าา 🐱",
                                            "size": "xl",
                                            "align": "center",
                                            "color": "#FF0000",
                                            'flex': 1,
                                            "weight": "bold",
                                            "type": "text"
                                            }
                                        ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดแทค/ปิดแทค",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดแทค2/ปิดแทค2",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดแทค3/ปิดแทค3",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดไลค์/ปิดไลค์",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดคอมเม้น/ปิดคอมเม้น",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดบล็อค/ปิดบล็อค",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดแอด/ปิดแอด",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                                                                                                                                                                                                                                                                 
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดกันรัน/ปิดกันรัน",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดต้อนรับ/ปิดต้อนรับ",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดต้อนรับ2/ปิดต้อนรับ2",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดคนออก/ปิดคนออก",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดยกเลิก/ปิดยกเลิก",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดติ๊กคนเข้า/ปิดติ๊กคนเข้า",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดติ๊กคนออก/ปิดติ๊กคนออก",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดติ๊กใหญ่/ปิดติ๊กใหญ่",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"                                            
                                     }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                        "type": "icon",
                                        "url": "https://www.img.live/images/2019/09/17/343432.jpg",
                                        "size": "md"
                                            },
                                            {
                                        "type": "text",
                                        "text": "™TANBOTNEVERDIE✯͜͡❂➣",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                            },
                                            {
                                        "type": "spacer",
                                        "size": "md"
                                            }
                                        ]
                                    }
                                ]
                            }
                        },
                        {   
                            "type": "bubble",
                            "styles": {
                                "header": {"backgroundColor": COOZ3},
                                "hero": {"backgroundColor": "#FFFFFF", "separator": True, "separatorColor": "#000000"},
                                "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                            },
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "type": "image",
                                        "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        },  
                                        {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                            {
                                            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                                            "type": "image"
                                        },
                                    ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                   
                                        "contents": [
                                            {
                                            "text": "🐱 คำสั่งบอทจ้าา 🐱",
                                            "size": "xl",
                                            "align": "center",
                                            "color": "#FF0000",
                                            'flex': 1,
                                            "weight": "bold",
                                            "type": "text"
                                            }
                                        ],
                                        "type": "box",
                                        "spacing": "sm",
                                        "layout": "vertical"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " mid @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " คท @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ปก @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " รูป @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ตัส @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ชื่อ @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {  
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เชค",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                                                                                                                                                                                                                                                                 
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " คอล (จำนวน) @user",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เตะดำ",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เชคคอล",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ประกาศ3 (ข้อความ)",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                           "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เชคบัค",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " ประกาศมุด ( ข้อความ )",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เขียน3 (ข้อความ)",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"
                                    },
                                    {                                        
                                        "contents": [
                                        {
                                            "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                            "type": "icon",
                                            "size": "md"
                                        },
                                        {
                                            "text": " เปิดแทคเตะ/ปิดแทคเตะ",
                                            "size": "md",
                                            "margin": "none",
                                            "color": COOZ,
                                            'flex': 1,
                                            "weight": "regular",
                                            "type": "text"
                                            }
                                        ],
                                            "type": "box",
                                            "layout": "baseline"
                                     },
                                    {
                                        "type": "separator",
                                        "color": "#DC143C"                                            
                                     }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                        "type": "icon",
                                        "url": "https://www.img.live/images/2019/09/12/343316.jpg",
                                        "size": "md"
                                            },
                                            {
                                        "type": "text",
                                        "text": "™TANBOTNEVERDIE✯͜͡❂➣",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                            },
                                            {
                                        "type": "spacer",
                                        "size": "md"
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                    data = {
                        "type": "flex",
                        "altText": "Help Message",
                        "contents": {
                            "type": "carousel",
                            "contents": dataProfile
                        }
                    }
                    sendTemplate(to, data)
 #------------------------------ขายของ---------------------------------------------#                            
                elif msg.text.lower().startswith("ขายของ"):
                            contact = nn1.getContact(sender) 
                            groups = nn1.getGroupIdsJoined()
                            for group in groups:
                                dataProfile = [ 
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FF00'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "NEVERDIE BOT",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FF00"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://www.img.live/images/2019/09/17/20190917_163605.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/~steveneverdie002"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://www.img.live/images/2019/09/17/343313.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "botneverdie"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://sv1.picz.in.th/images/2019/06/04/10UTMJ.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "self bot flex python3",
                                                  "color": "#00FF00",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 100B ต่อเดือน",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ดูแลตลอดการไช้งาน",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ไม่หนีไม่หาย มาไวทันใจ",
                                                  "color": "#00FF00",
                                                  "gravity": "botneverdie",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "อัพเดตฟังชั่นเรื่อยๆ",
                                                  "color": "#00FF00",
                                                  "gravity": "botneverdie",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจกดที่นี่คับ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line.me/ti/p/~steveneverdie002",
                                                        "type": "uri",
                                                        "label": "Add Hacker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                       }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FF00'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "NEVERDIE BOT",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FF00"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://www.img.live/images/2019/09/17/20190917_163605.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/~steveneverdie002"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://www.img.live/images/2019/09/17/343285aaddd.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "botneverdie"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://www.img.live/images/2019/09/17/343344.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "รับติดบอทV10",
                                                  "color": "#00FF00",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ลงสด/ห้อง สนใจทักมา",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "บอทม่ตอบ เดี๋ยวเปลี่ยนให้",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "มาสอบถามได้คับ",
                                                  "color": "#00FF00",
                                                  "gravity": "botneverdie",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ดูแลตลอดการไช้งาน",
                                                  "color": "#00FF00",
                                                  "gravity": "botneverdie",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจกดที่นี่คับ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line.me/ti/p/~steveneverdie002",
                                                        "type": "uri",
                                                        "label": "Add Hacker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FF00'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "NEVERDIE BOT",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FF00"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://www.img.live/images/2019/09/17/Hack_1920x1200_px_anarchy_Anonymous_Binary_Code_computer_Dark-1490679.jpgd.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/~steveneverdie002"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://www.img.live/images/2019/09/17/Hack_1920x1200_px_anarchy_Anonymous_Binary_Code_computer_Dark-1490679.jpgd.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "botneverdie"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://www.img.live/images/2019/09/17/343344.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "รับทำบอทเพจ/บอทคำสั่งv10",
                                                  "color": "#00FF00",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "บอทApiอื่นๆ",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ดูแลตลอดมาใส่คำสั่งเพิ่มได้",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคากันเอง",
                                                  "color": "#00FF00",
                                                  "gravity": "botneverdie",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "รับทำดิส/วีดีโอโปรไฟล",
                                                  "color": "#00FF00",
                                                  "gravity": "botneverdie",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจกดที่นี่คับ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line.me/ti/p/~steveneverdie002",
                                                        "type": "uri",
                                                        "label": "Add Hacker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                ]
                                data = {
                                    "type": "flex",
                                    "altText": "มีของมาขาย",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(1)
                            nn1.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))     
#------------------------------ขายของ---------------------------------------------#                            
                elif msg.text.lower().startswith("กลุ่มลับ"):
                            contact = nn1.getContact(sender) 
                            groups = nn1.getGroupIdsJoined()
                            for group in groups:
                                dataProfile = [ 
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FF00'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "VIP 18+ XXX",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#66FFFF"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://sv1.picz.in.th/images/2019/09/02/ZsMySV.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/~steveneverdie002"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://www.img.live/images/2019/09/16/343321.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "botneverdie"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://sv1.picz.in.th/images/2019/09/02/ZsMFiQ.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "เข้ากลุ่มลับVIP",
                                                  "color": "#00FF00",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 100B ตลอดชีพ",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "มีหลากหลายบริการ",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "งานดี100%",
                                                  "color": "#00FF00",
                                                  "gravity": "botneverdie",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "สนใจติดต่อมา",
                                                  "color": "#00FF00",
                                                  "gravity": "botneverdie",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "เข้ากลุ่มลับVIP กด",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line.me/ti/p/~steveneverdie002",
                                                        "type": "uri",
                                                        "label": "Add Hacker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                       }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FF00'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "VIP 18+ XXX",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#66FFFF"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://sv1.picz.in.th/images/2019/09/02/ZsMySV.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/~steveneverdie002"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://sv1.picz.in.th/images/2019/09/02/ZsMFiQ.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "botneverdie"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://sv1.picz.in.th/images/2019/09/02/ZsMFiQ.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "เข้ากลุ่มลับVIP",
                                                  "color": "#00FF00",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 100B ตลอดชีพ",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "มีหลากหลายบริการ",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "สนใจติดต่อมา",
                                                  "color": "#00FF00",
                                                  "gravity": "botneverdie",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "งานดี100%",
                                                  "color": "#00FF00",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "เข้ากลุ่มลับVIP กด",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line.me/ti/p/~steveneverdie002",
                                                        "type": "uri",
                                                        "label": "Add Hacker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FF00'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "VIP 18+ XXX",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#66FFFF"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://sv1.picz.in.th/images/2019/09/02/ZsMySV.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~steveneverdie002"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://sv1.picz.in.th/images/2019/09/02/ZsMFiQ.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "botneverdie"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://sv1.picz.in.th/images/2019/09/02/ZsMFiQ.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "เข้ากลุ่มลับVIP",
                                                  "color": "#00FF00",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 100B ตลอดชีพ",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "สนใจติดต่อมา",
                                                  "color": "#00FF00",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "มีหลากหลายบริการ",
                                                  "color": "#00FF00",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "งานดี100%",
                                                  "color": "#00FF00",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "เข้ากลุ่มลับVIP กด",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line.me/ti/p/~steveneverdie002",
                                                        "type": "uri",
                                                        "label": "Add Hacker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                ]
                                data = {
                                    "type": "flex",
                                    "altText": "มีของมาขาย",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(1)
                            nn1.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))                                                                                                                                                                               
#--------------------------------------------------------------------------------------------------#                                
                if text.lower() == "ดำ":
                  if msg._from in admin:
                      apalo["Talkwblacklist"] = True
                      nn2(to,"🐱 ส่งคท.มา 🐱")
                if text.lower() == "ขาว":
                  if msg._from in admin:
                      apalo["Talkdblacklist"] = True
                      nn2(to,"🐱 ส่งคท.มา  🐱")
#--------------------------------------------------------------------------------------------------#                      
                elif msg.text in ["เปิดแอบ"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    nn2(to,"เปิดระบบตรวจคนอ่าน")
                    
                elif msg.text in ["ปิดแอบ"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        nn2(to, RfuCctv['sidermem'][msg.to])
                    else:
                        nn2(to, "ปิดระบบแอบคนอ่านแล้ว")
                        
                elif 'ตั้งคนแอบ ' in msg.text:
                   if msg._from in admin:
                      spl = msg.text.replace('ตั้งคนแอบ ','')
                      if spl in [""," ","\n",None]:
                          nn2(msg.to, "เกิดข้อผิดพลาด")
                      else:
                          settings["mention"] = spl
                          nn2(msg.to, "「ข้อความเช็คคนแอบ」\nเปลี่ยนข้อความเป็น :\n「{}」".format(str(spl)))	
#--------------------------------------------------------------------------------------------------#                          
                elif msg.text.lower().startswith("ตั้งแทค "):
                      text_ = removeCmd("ตั้งแทค", text)
                      try:
                          tagadd["tag"] = text_
                          sa = "🐱 ตั้งคำแทค 🐱\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "™TANBOTNEVERDIE✯͜͡❂➣", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}
                          sendTemplate(to,data)
                      except:
                          nn2(to,"Done. >_<")
#----------------------------------------------------------------------------#                          
                elif msg.text.lower().startswith("ตั้งแทคแชท "):
                      text_ = removeCmd("ตั้งแทคแชท", text)
                      try:
                          settings["reply"] = text_
                          sa = "「 ตั้งคำแทค 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "™TANBOTNEVERDIE✯͜͡❂➣", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}
                          sendTemplate(to,data)
                      except:
                          nn2(to,"Done. >_<")
#----------------------------------------------------------------------------#                          
                elif msg.text.lower().startswith("ตั้งต้อนรับ "):
                      text_ = removeCmd("ตั้งต้อนรับ", text)
                      try:
                          set["wc"][msg.to] = text_
                          sa = "「 ตั้งต้อนรับ 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "™TANBOTNEVERDIE✯͜͡❂➣", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}
                          sendTemplate(msg.to,data)
                      except:
                          nn2(msg.to,"Done. >_<")
                          
                elif msg.text.lower().startswith("ตั้งคนออก "):
                            text_ = removeCmd("ตั้งคนออก", text)
                            try:
                                tagadd["lv"] = text_
                                nn2(to,"「 ตั้งคนออก 」\nคือ : " + text_)
                            except:
                                nn2(to,"สำเเร็จแล้ว")
                                
                elif msg.text.lower().startswith("ตั้งแอด "):
                      text_ = removeCmd("ตั้งแอด", text)
                      try:
                          tagadd["add"] = text_
                          sa = "「 ตั้งแอด 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "™TANBOTNEVERDIE✯͜͡❂➣", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}
                          sendTemplate(to,data)
                      except:
                          nn2(to,"Done. >_<")
                          
                elif msg.text.lower().startswith("ตั้งคอมเม้น "):
                      text_ = removeCmd("ตั้งคอมเม้น", text)
                      try:
                          tagadd["comment"] = text_
                          sa = "🌠 ตั้งคอมเม้น 🌠\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "™TANBOTNEVERDIE✯͜͡❂➣", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}
                          sendTemplate(to,data)
                      except:
                          nn2(to,"Done. >_<")
#--------------------------------------------------------------------------------------------------#                          
                if text.lower() == "เชค":
                    add = tagadd["add"]
                    tag = tagadd["tag"]
                    like = settings["comment"]
                    wc = tagadd["wctext"]
                    lv = tagadd["lv"]
                    c = settings["autoCancel"]["members"]
                    b = tagadd["b"]
                    Re = settings["reply"]
                    nn1.generateReplyMessage(msg.id)
                    nn1.sendReplyMessage(msg.id, to, "ข้อความแอด :\n"+str(add)+"\n\nข้อความแทค :\n"+str(tag)+"\n\nข้อความเม้น :\n"+str(like)+"\n\nข้อความต้อนรับ :\n"+str(wc)+"\n\nข้อความคนออก :\n"+str(lv)+"\n\nจำนวนค้างเชิญ :\n"+str(c)+" จำนวน\n\nข้อความบล็อค :\n"+str(b)+"\n\nข้อความแทคแชท :\n"+str(Re))

#=====================================================================
                if text.lower().startswith("ลบเวลา "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del DDATE[getx]
                        nn1.sendMessage(msg.to, "ประกาศเวลา " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('time.json','w','utf-8')
                        json.dump(DDATE, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
#----------------------------------------------------------------------------#                        
                if text.lower().startswith("ประกาศ4 "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        DDATE[kw] = ans
                        f=codecs.open('time.json','w','utf-8')
                        json.dump(DDATE, f, sort_keys=True, indent=4, ensure_ascii=False)
                        nn1.sendMessage(msg.to,"เวลา: " + str(kw) + "\nประกาศ: "+ str(ans))
                    except Exception as Error:
                        print(Error)
#----------------------------------------------------------------------------#                        
                if text.lower() == "เช็คเวลา":
                    lisk = "เช็คดูประกาศเวลา"
                    for i in DDATE:
                        lisk+="\nเวลา: "+str(i)+"\nประกาศ: "+str(DDATE[i])
                    nn1.sendMessage(to, str(lisk))
#----------------------------------------------------------------------------#                    
                if text.lower() == 'เชคคอล':
                            a = nn1.getGroupCall(to)
                            print(a)
                            k = len(a.memberMids)//20
                            for i in range(k+1):
                                try:
                                    if i == 0:aa = '╭「 การสนทนาแบบกลุ่ม 」─\n│ชื่อกลุ่ม: {}\n│เริ่มการโทร ใน: {}'.format(nn1.getGroup(to).name,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                                    else:aa = '├「 การสนทนาแบบกลุ่ม 」─\n│ชื่อกลุ่ม: {}\n│เริ่มการสนทนาใน: {}'.format(nn1.getGroup(to).name,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                                    ret = aa
                                    for b in a.memberMids[i*20 : (i+1)*20]:
                                        ds = nn1.getContact(b).displayName
                                        no += 1
                                        c = a.hostMids
                                        s = nn1.getContact(c).displayName
                                        if a.mediaType == 1:typenya = 'การใช้สายแบบฟรีไทม์'
                                        if a.mediaType == 2:typenya = 'การใช้สายวิดีโอคอลกลุ่ม'
                                        if no == len(a.memberMids):ret+='\n│{}. {}\n│ชนิด: {}\n│ผู้เริ่มการสนทนา: {}\n╰────────────'.format(no,ds,typenya,s)
                                        else:ret+='\n│{}. {}'.format(no,ds)
                                    nn1.sendMessage(to, ret)
                                except:
                                    if a.mediaType == 3:typenya = 'การรับชมไลฟ์สด'
                                    if i == 0:aa = '╭「 กำลังรับชมไลฟ์สด」─\n│ชื่อกลุ่ม: {}\n│เริ่มการไลฟ์ ใน : {}\n│   • ผู้รับชมไลฟ์สด:'.format(nn1.getGroup(to).name,humanize.naturaltime(datetime.fromtimestamp(int(a.started)//1000)));no = i
                                    else:aa = '├「 กำลังไลฟ์สดกลุ่ม 」─\n│ชื่อกลุ่ม: {}\n│เริ่มการไลฟ์ ใน: {}\n|• ผู้รับชม ไลฟ์สด:'.format(nn1.getGroup(to).name,humanize.naturaltime(datetime.fromtimestamp(int(a.starter)//1000)));no=i*20
                                    ret = aa
                                    for b in a.memberMids[i*20 : (i+1)*20]:
                                        ds = nn1.getContact(b).displayName
                                        no += 1
                                        c = a.hostMids
                                        s = nn1.getContact(c).displayName
                                        if no == len(a.memberMids):ret+='\n│{}. {}\n│ชนิด: {}\n│ผู้เริ่มการไลฟ์สด: {}\n╰─────────────'.format(no,ds,typenya,s)
                                        else:ret+='\n│{}. {}'.format(no,ds)
                                    nn1.sendMessage(to, ret)
#----------------------------------------------------------------------------#                                    
                elif msg.text.lower().startswith("ประกาศ "):
                            txt = removeCmd("ประกาศ", text)
                            s = "#000000"
                            a = "#ffffff"
                            groups = nn1.getGroupIdsJoined()
                            contact = nn1.getContact(nn1MID)
                            pp = nn1.getProfile().pictureStatus
                            profile = "https://profile.line-scdn.net/" + str(pp)
                            for group in groups:
                                sa = "「 ข้อความประกาศ 」\n\n{}".format(str(txt))
                                data = {"type": "flex","altText": str(sa),"contents": {"type": "bubble",'styles': {"body": {"backgroundColor":str(a)}},"hero": {"type":"image","url":"https://sv1.picz.in.th/images/2019/09/05/ZrDaKJ.png","size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": str(sa),"wrap": True,"color":str(s),"align": "center","gravity": "center","size": "md"},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#FF0066","action": {"type": "uri","label": "• แอดมา •","uri": "line://ti/p/~"+str(nn1.getProfile().userid)}}]}}}
                                sendTemplate(group, data)
                                time.sleep(1)
                            nn2(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))                
#----------------------------------------------------------------------------#                
                elif msg.text.lower().startswith("ประกาศ3 "):
                            txt = removeCmd("ประกาศ3", text)
                            s = temp["te"]
                            a = temp["t"]
                            contact = nn1.getContact(sender)
                            pp = nn1.getProfile().pictureStatus
                            cover = nn1.getProfileCoverURL(nn1.profile.mid)
                            profile = "https://profile.line-scdn.net/" + str(pp)
                            vido = "https://os.line.naver.jp/os/p/" + nn1MID + "/vp"
                            name = nn1.getProfile().displayName
                            status = nn1.getProfile().statusMessage
                            groups = nn1.getGroupIdsJoined()
                            contact = nn1.getContact(nn1MID)
                            cover = nn1.getProfileCoverURL(nn1MID)
                            for group in groups:
                                sa = "{}".format(str(txt))
                                data={"type":"flex","altText": "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯","contents":{"type":"carousel","contents":[{"type":"bubble","body":{"type":"box","contents":[{"type":"text","wrap":True,"size":"xl","text":"ประกาศๆ","weight":"bold"},{"type":"box","contents":[{"weight":"bold","text":"Picture ","size":"xl","type":"text","wrap":True,"flex":0},{"weight":"bold","text":"Status","size":"xs","type":"text","wrap":True,"flex":0}],"layout":"baseline"},{"margin":"md","text":"ประกาศๆ","size":"xxl","type":"text","wrap":True,"color":"#ff0000","flex":0}],"spacing":"xs","layout":"vertical"},"footer":{"type":"box","contents":[{"type":"icon","url":"https://sv1.picz.in.th/images/2019/09/05/ZrbkBy.jpg","size":"xl"},{"size":"md","action":{"type":"uri","uri":"https://line.me/ti/p/~" + nn1.profile.userid},"text":"ติดต่อคนสร้าง","weight":"bold","type":"text","wrap":True,"align":"center","color":"#ff0000"}],"layout":"baseline"},"hero":{"margin":"xl","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"aspectMode":"cover","aspectRatio":"1:1","type":"image","size":"full"},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#333333"}}},{"type":"bubble","body":{"type":"box","contents":[{"type":"text","wrap":True,"size":"xl","text":"ประกาศๆ","weight":"bold"},{"type":"box","contents":[{"weight":"bold","text":"Cover","size":"xl","type":"text","wrap":True,"flex":0},{"weight":"bold","text":" Status","size":"xs","type":"text","wrap":True,"flex":0}],"flex":1,"layout":"baseline"},{"margin":"md","text":"ประกาศๆ","size":"xxl","type":"text","wrap":True,"color":"#ff0000","flex":0}],"spacing":"xs","layout":"vertical"},"footer":{"type":"box","contents":[{"type":"icon","url":"https://sv1.picz.in.th/images/2019/09/05/ZrbkBy.jpg","size":"xl"},{"size":"md","action":{"type":"uri","uri":"line://ti/p/~"+nn1.getProfile().userid,},"text":"ติดต่อคนสร้าง","weight":"bold","type":"text","wrap":True,"align":"center","color":"#ff0000"}],"layout":"baseline"},"hero":{"margin":"xxl","url":nn1.getProfileCoverURL(sender),"aspectMode":"cover","aspectRatio":"1:1","type":"image","size":"full"},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#333333"}}},{"type":"bubble","footer":{"type":"box","contents":[{"type":"icon","url":"https://sv1.picz.in.th/images/2019/09/05/ZrbkBy.jpg","size":"xl"},{"size":"md","action":{"type":"uri","uri":"line://ti/p/~"+nn1.getProfile().userid,},"text":"ติดต่อคนสร้าง","weight":"bold","type":"text","wrap":True,"align":"center","color":"#ff0000"}],"layout":"baseline"},"body":{"type":"box","contents":[{"size":"lg","text":"      ประกาศกลุ่ม","weight":"bold","type":"text","wrap":True,"color":"#ff0000"},{"type":"box","contents":[{"weight":"bold","text":str(sa),"size":"md","type":"text","wrap":True,"color":"#ff0000"}],"flex":1,"layout":"baseline"},{"margin":"md","text":"SelfBot_ By:™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯ ","size":"md","type":"text","wrap":True,"color":"#ff0000","flex":0}],"spacing":"xs","layout":"vertical"},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#333333"}}}]}}
                                sendTemplate(group, data)
                                time.sleep(1)
                            nn2(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))   
#----------------------------------------------------------------------------#                
                elif text.lower() == "เตะดำ":
                    if msg.toType == 2:
                        groupMemberMids = [contact.mid for contact in nn1.getGroup(to).members]
                        matched_list = []
                        for mid in apalo["Talkblacklist"]:
                            matched_list += [x for x in groupMemberMids if x == mid]
                        if matched_list == []:
                            nn4(to, "👉 ไม่พบควายเผือก 👈")
                        else:
                            for mids in matched_list:
                                try:
                                    nn1.kickoutFromGroup(to, [mids])
                                except:pass
#----------------------------------------------------------------------------#                
                elif text.lower() == "เตะควาย":
                    if msg.toType == 2:
                        groupMemberMids = [contact.mid for contact in nn1.getGroup(to).members]
                        matched_list = []
                        for mid in apalo["Talkblacklist"]:
                            matched_list += [x for x in groupMemberMids if x == mid]
                        if matched_list == []:
                            nn4(to, "👉 ไม่พบควายเผือก 👈")
                        else:
                            for mids in matched_list:
                                try:
                                    nn1.kickoutFromGroup(to, [mids])
                                except:pass   
#----------------------------------------------------------------------------#                
                elif text.lower() == "ประหารชีวิต":
                    if msg.toType == 2:
                        groupMemberMids = [contact.mid for contact in nn1.getGroup(to).members]
                        matched_list = []
                        for mid in apalo["Talkblacklist"]:
                            matched_list += [x for x in groupMemberMids if x == mid]
                        if matched_list == []:
                            nn4(to, "👉 ไม่พบควายเผือก 👈")
                        else:
                            for mids in matched_list:
                                try:
                                    nn1.kickoutFromGroup(to, [mids])
                                except:pass                                     
#----------------------------------------------------------------------------#                                
                elif text.lower() == 'บ้าน' or text.lower() == "!list group":
                        s = temp["te"]
                        a = temp["t"]
                        contact = nn1.getContact(nn1MID)
                        groups = nn1.groups
                        g = "\n"
                        no = 0 + 1
                        for gid in groups:
                            group = nn1.getGroup(gid)
                            g += "{}. {} | {}\n".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        gg = "จำนวน {} กลุ่ม".format(str(len(groups)))
                        data={'type':'flex','altText':"กลุ่มเรา",'contents':{"type":"bubble","header":{"type":"box","layout":"baseline","contents":[{"type":"icon","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"size":"lg"},{"type":"text","text":"☆ ™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯ ☆","margin":"xl","weight":"bold","color":"#FFFFFF","align":"center","size":"lg"}]},"hero":{"type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"size":"full"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"•กลุ่มทั้งหมดของเรา•","weight":"bold","align":"center","size":"lg","color":s,"flex":1},{"type":"text","text":"{}".format(str(g)),"size":"sm","wrap":True,"flex":1}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"{}".format(str(gg)),"color":s,"weight":"bold","size":"sm","align":"center"}]},"styles":{"header":{"backgroundColor":"#FF69B4"},"hero":{"separator":True,"separatorColor":"#FF69B4","backgroundColor":"#FF69B4"},"footer":{"backgroundColor":"#FF69B4","separator":True,"separatorColor":"#CCFFCC"},"body":{"backgroundColor":a}}}}
                        sendTemplate(to, data)
#----------------------------------------------------------------------------# 
#คำสั่งชุดป้องกันแบบแยกกลุ่มได้  🐱🐱🐱🐱    
#----------------------------------------------------------------------------#  
#------------------[เปิด-ปิดป้องกัน]--------------------------------------------------------#                   
                elif 'กันลิ้ง ' in msg.text:
                      spl = msg.text.replace('กันลิ้ง ','')
                      if spl == 'เปิด':
                          if msg.to in protectqr:
                              msgs = "เปิดระบบกันลิ้ง"
                          else:
                              protectqr.append(msg.to)
                              ginfo = nn1.getGroup(msg.to)
                              msgs = "เปิดระบบกันลิ้ง\n ประจำกลุ่ม : " +str(ginfo.name)
                          nn2(msg.to, "「พร้อมใช้งานแล้ว」\n" + msgs)                          
                      elif spl == 'ปิด':
                           if msg.to in protectqr:
                               protectqr.remove(msg.to)
                               ginfo = nn1.getGroup(msg.to)
                               msgs = "ปิดระบบกันลิ้ง\n ประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบกันลิ้ง"
                           nn2(msg.to, "「ปิดใช้งาน」\n" + msgs)
                      
                elif 'กันเชิญ ' in msg.text:
                      spl = msg.text.replace('กันเชิญ ','')
                      if spl == 'เปิด':
                          if msg.to in protectinvite:
                              msgs = "เปิดระบบกันคนเชิญ"
                          else:
                              protectinvite.append(msg.to)
                              ginfo = nn1.getGroup(msg.to)
                              msgs = "เปิดระบบกันคนเชิญ\n ประจำกลุ่ม : " +str(ginfo.name)
                          nn2(msg.to, "「พร้อมใช้งานแล้ว」\n" + msgs)                          
                      elif spl == 'ปิด':
                           if msg.to in protectinvite:
                               protectinvite.remove(msg.to)
                               ginfo = nn1.getGroup(msg.to)
                               msgs = "ปิดระบบกันคนเชิญ\n ประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบกันคนเชิญ"
                           nn2(msg.to, "「ปิดใช้งาน」\n" + msgs)
                          
                elif 'กันคนเข้า ' in msg.text:
                      spl = msg.text.replace('กันคนเข้า ','')
                      if spl == 'เปิด':
                          if msg.to in protectjoin:
                              msgs = "เปิดระบบกันคนเข้า"
                          else:
                              protectjoin.append(msg.to)
                              ginfo = nn1.getGroup(msg.to)
                              msgs = "เปิดระบบกันคนเข้า\n ประจำกลุ่ม : " +str(ginfo.name)
                          nn2(msg.to, "「พร้อมใช้งานแล้ว」\n" + msgs)                          
                      elif spl == 'ปิด':
                           if msg.to in protectjoin:
                               protectjoin.remove(msg.to)
                               ginfo = nn1.getGroup(msg.to)
                               msgs = "ปิดระบบกันคนเข้า\n ประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบกันคนเข้า"
                           nn2(msg.to, "「ปิดใช้งาน」\n" + msgs)    
                           
                elif 'กันเตะ ' in msg.text:
                      spl = msg.text.replace('กันเตะ ','')
                      if spl == 'เปิด':
                          if msg.to in protectkick:
                              msgs = "เปิดระบบกันคนเตะ"
                          else:
                              protectkick.append(msg.to)
                              ginfo = nn1.getGroup(msg.to)
                              msgs = "เปิดระบบกันคนเตะ\n ประจำกลุ่ม : " +str(ginfo.name)
                          nn2(msg.to, "「พร้อมใช้งานแล้ว」\n" + msgs)                          
                      elif spl == 'ปิด':
                           if msg.to in protectkick:
                               protectkick.remove(msg.to)
                               ginfo = nn1.getGroup(msg.to)
                               msgs = "ปิดระบบกันคนเตะ\n ประจำกลุ่ม : " +str(ginfo.name)
                           else:
                               msgs = "ปิดระบบกันคนเตะ"
                           nn2(msg.to, "「ปิดใช้งาน」\n" + msgs)
#----------------------------------------------------------------------------#             
                elif text.lower().startswith("เขียน "):
                            s = "#66FF00"
                            a = "#ffffff"
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            contact = nn1.getContact(nn1MID)
                            cover = nn1.getProfileCoverURL(nn1MID)
                            data = {
                                "type": "flex",
                                "altText": "flex",
                                "contents": {
                                      "type": "bubble",
                            'styles': {
                                "body": {
                                    "backgroundColor":a
                                },
                             },
                             "hero": {
                                 "type":"image",
                                 "url": "https://sv1.picz.in.th/images/2019/09/04/Z6LeuS.jpg",
                                 "size":"full",
                                 "aspectRatio":"20:13",
                                 "aspectMode":"cover"
                            },
                            "body": {
                               "type": "box",
                                "layout": "vertical",
                                "contents": [            
                                            {
                                                "type": "text",
                                                "text": "{}".format(text),
                                                "wrap": True,
                                                "align": "start",
                                                "gravity": "center",
                                                "color": s,
                                                "size": "xxl"
                                            },
                                        ]
                                    }
                                }
                            }
                            sendTemplate(to, data)
#----------------------------------------------------------------------------#                            
                elif text.lower().startswith('คอล '):
                            j = int(msg.text.split(' ')[1])
                            a = [nn1.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                nama = [key1]
                                b = [nn1.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a];nn2(to, '「 เชิญโทร」\nกำลังเชิญ แล้ว {} ครั้ง สำเร็จแล้ว มาคุยกันเถอะ♪'.format(j))
                            else:
                                group = nn1.getGroup(to);nama = [contact.mid for contact in group.members];b = [nn1.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a]
                                nn2(to, ' 「 เชิญโทรกลุ่ม」\nกำลังเชิญสมาชิก {} ครั้ง สำเร็จแล้ว♪'.format(j))
#----------------------------------------------------------------------------#                                
                elif cmd == "เชคบัค":
                    if msg._from in admin or msg._from in owner:
                       try:nn1.inviteIntoGroup(to, [nn1MID]);has = "OK"
                       except:has = "NOT"
                       try:nn1.kickoutFromGroup(to, [nn1MID]);has1 = "OK"
                       except:has1 = "NOT"
                       if has == "OK":sil = "สถานะ ไม่บัค ✔"
                       else:sil = "สถานะ บัค 🚫"
                       if has1 == "OK":sil1 = "สถานะ ไม่บัค ✔"
                       else:sil1 = "สถานะ บัค 🚫"
                       nn2(to, "╭═™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ═╮\n👉ระบบเตะ : {} \n👉ระบบเชิญ : {}\n👉ระบบแชท : สถานะ ไม่ลาง✔\n╰═™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ═╯".format(sil1,sil))
#-----------------------------------------------------------------------------------------#                            
                elif msg.text.lower().startswith("poto "):
                                query = removeCmd("poto", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
#-----------------------------------------------------------------------------------------------------#                           
                elif cmd == "ติดต่อ":
                        	_session = requests.session()
                        	n1 = LiffChatContext(to)
                        	n2 = LiffContext(chat=n1)
                        	view = LiffViewRequest('1602687308-GXq4Vvk9', n2)
                        	token = nn1.liff.issueLiffView(view)
                        	url = 'https://api.line.me/message/v3/share'
                        	headers = {
                        		'Content-Type': 'application/json',
                        		'Authorization': 'Bearer %s' % token.accessToken
                        	}
                        	jsonData = {
                        		"to": to,
                        		"messages": [
                        			{
                        				"type": "template",
                        				"altText": "LINE",
                        				"template": {
                        					"type": "carousel",
                        					"actions": [],
                        					"columns": [
                                                {
                                                	"title": "ติดต่อผู้สร้าง",
                                                	"text": "AddMe",
                                                	"actions": [
                                                		{
                                                			"type": "uri",
                                                			"label": "ADD ME",
                                                			"uri": "line.me/ti/p/~steveneverdie002"
                                                		}
                                                	]
                                                },
                                                {
                                                	"title": "Youtube",
                                                	"text": "Youtube",
                                                	"actions": [
                                                		{
                                                			"type": "uri",
                                                			"label": "Youtube",
                                                			"uri": "line.me/ti/p/~steveneverdie002"
                                                		}
                                                	]                                                		
                                                },
                                                {
                                                	"title": "Game",
                                                	"text": "Game",
                                                	"actions": [
                                                		{
                                                			"type": "uri",
                                                			"label": "Game",
                                                			"uri": "line.me/ti/p/~steveneverdie002"
                                                		}
                                                	]                                                		
                                                },
                                                {                                                    
                                                	"title": " Group Event",
                                                	"text": " Group Event",
                                                	"actions": [
                                                		{
                                                			"type": "uri",
                                                			"label": " Group Event",
                                                			"uri": "line.me/ti/p/~steveneverdie002"
                                                		}
                                                	]                                                		
                                                },
                                                {                                                    
                                                	"title": "กดสิ",
                                                	"text": "กดสิ",
                                                	"actions": [
                                                		{
                                                			"type": "uri",
                                                			"label": "กดสิ",
                                                			"uri": "line://app/1487085176-lP805wzy?text=รักนะจุ๊บๆ"                                                            
                                                		}                                                		
                                                	]
                                                }
                        					]
                        				}
                        			}
                        		]
                        	}
                        	data = json.dumps(jsonData)
                        	sendPost = _session.post(url, data=data, headers=headers)
#--------------------------------------------------------------------------------------------------------------------#                           
                elif cmd == "เชคบล็อค":
                            if msg._from in nn1MID:
                                blockedlist = nn1.getBlockedContactIds()
                                if blockedlist == []:
                                    nn2(to, "👉ไม่พบ👈 ‼️")
                                else:
                                    for kontak in blockedlist:
                                        nn1.sendMessage(to, text=None, contentMetadata={'mid': kontak}, contentType=13)
                                        time.sleep(1)
                                        nn3(to,"🚫รายการบล็อค🚫")
#-----------------------------------------------------------------------------------------------------------------#                           
                elif cmd == 'gift':
                            nn1.generateReplyMessage(msg.id)
                            nn1.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)   
                            nn2(to, "💞💝🎃 ส่งของขวัญละจ้า🎃💖🖤")
                elif cmd == 'แจก':
                            nn1.generateReplyMessage(msg.id)
                            nn1.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)   
                            nn2(to, "🎀🎁ส่งของขวัญละจ้า🎁🎀")    
#--------------------------------------------------------------------------------------#                           
                elif cmd.startswith("flex "):
                            sep = text.split(" ")
                            pesan = text.replace(sep[0] + " ","")
                            data = {
                                "type": "flex",
                                "altText": "flex",
                                "contents": {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(pesan),
                                                "wrap": True,
                                                "align": "start",
                                                "gravity": "center",
                                                "size": "sm"
                                            },
                                        ]
                                    }
                                }
                            }
                            sendTemplate(to, data)
#------------------------------------------------------------------------------------------------------------------#              
                elif msg.text.lower().startswith("เขียนเฟก "):
                    sep = text.split(" ")
                    textnya = text.replace(sep[0] + " ", "")
                    text = "{}".format(textnya)
                    contact = nn1.getContact(nn1MID)
                    data = {
                        "type": "flex",
                        "altText": "AvengresBot",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                    },
                                 },
                            "hero": {
                                "type": "image",
                                "url": "https://www.img.live/images/2019/09/17/Hack_1920x1200_px_anarchy_Anonymous_Binary_Code_computer_Dark-1490679.jpgd.jpg",
                                "size": "full",
                                "aspectRatio":"1:1",
                                "aspectMode":"cover"
                            },
                            "body": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(text),
                                        "color":"#66FFFF",
                                        "wrap": True,
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "xl"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)  

#---------------------------------ลูกเล่น--------------------------------------------------------------------------------------#                                   
#---------------------------------ลูกเล่น--------------------------------------------------------------------------------------#                            
                elif text.lower() == "เทสบอท":
                    nn2(to,"「 NEVERDIE BOT」")
                    time.sleep(1)
                    nn3(to, "█▒... 10.0%")
                    time.sleep(1)
                    nn3(to, "███▒... 25.0%")
                    time.sleep(1)
                    nn3(to, "█████▒... 50.0%")
                    time.sleep(1)
                    nn3(to, "███████▒... 75.0%")
                    time.sleep(1)
                    nn3(to, "███████████..100.0%")
                    time.sleep(1)
                    nn4(to,"「👉บอทยังทำงานจ้าา👈」")               
         
                elif msg.text in ["เทส2","เทส"]:
                    Chivaree1={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "กำลังโหลด:▒...0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree2={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "█▒... 10.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree3={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "██▒... 20.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree4={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "███▒... 30.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}  
                       
                    Chivaree5={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "████▒... 40.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree6={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "█████▒... 50.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree7={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "█████▒... 60.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree8={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "██████▒... 70.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree9={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "████████▒... 80.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree10={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "█████████▒... 90.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree11={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "███████████..100.0%","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
  
                    Chivaree12={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "บอทยังทำงานคับท่าน😁","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree13={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "••AVENGRES BOT","color": "#00FF00","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}

                    sendTemplate(to, Chivaree1)
                    time.sleep(1)
                    sendTemplate(to, Chivaree2)
                    time.sleep(1)
                    sendTemplate(to, Chivaree3)
                    time.sleep(1)
                    sendTemplate(to, Chivaree4)
                    time.sleep(1)
                    sendTemplate(to, Chivaree5)
                    time.sleep(1)
                    sendTemplate(to, Chivaree6)
                    time.sleep(1)
                    sendTemplate(to, Chivaree7)
                    time.sleep(1)
                    sendTemplate(to, Chivaree8)
                    time.sleep(1)
                    sendTemplate(to, Chivaree9)
                    time.sleep(1)
                    sendTemplate(to, Chivaree10)
                    time.sleep(1)
                    sendTemplate(to, Chivaree11)
                    time.sleep(1)
                    sendTemplate(to, Chivaree12)
                    time.sleep(1)
                    sendTemplate(to, Chivaree13) 
#-----------------------------------------------------------------------------------------------------------------------------------------#                   
                elif msg.text in ["ด่า","ด่ามาน"]:
                    Chivaree1={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "กำลังด่า [รอสักครู่]..","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree2={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "ไอ้เย็บแม่!! เดะกุตบหัวหลุด","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree3={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "ก็มาดิไอ่เวร เหมือนเก่งอะ","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree4={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "มัดมือป่าว มีดคนละเล่มจะได้จบๆ","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}  
                       
                    Chivaree5={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "เหมือนหล่ออะไอ้เวร","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree6={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "ระวังตัวใว้ มึงเข้าไปเดี๋ยวเจอเลย","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree7={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "มองครวยไรละไอสัส","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree8={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "ไม่เคยเห็นบอทด่าเหรอ","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree9={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "ก็ม่ได้เสียวาไรอยู่แล้ว","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree10={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "เหมือนหล่ออะคับ","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       
                    Chivaree11={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "จอบอ จบ.....","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}  
                    
                    Chivaree12={
                       "type": "flex","altText": "◤₦Ɇ⩔ɆɌƉƗɆ ɃØ₮◢","contents": { "type": "bubble",     
                       "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "••🌟 ₦Ɇ⩔ɆɌƉƗɆ ɃØ₮🌟••","color": "#ffffff","align": "center","size": "xs"}]},
                       "styles": {"body": {"backgroundColor": "#0033FF"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}

                    sendTemplate(to, Chivaree1)
                    time.sleep(1)
                    sendTemplate(to, Chivaree2)
                    time.sleep(1)
                    sendTemplate(to, Chivaree3)
                    time.sleep(1)
                    sendTemplate(to, Chivaree4)
                    time.sleep(1)
                    sendTemplate(to, Chivaree5)
                    time.sleep(1)
                    sendTemplate(to, Chivaree6)
                    time.sleep(1)
                    sendTemplate(to, Chivaree7)
                    time.sleep(1)
                    sendTemplate(to, Chivaree8)
                    time.sleep(1)
                    sendTemplate(to, Chivaree9)
                    time.sleep(1)
                    sendTemplate(to, Chivaree10)
                    time.sleep(1)
                    sendTemplate(to, Chivaree11)
                    time.sleep(1)
                    sendTemplate(to, Chivaree12)          
#----------------------------------------------------------------------------#                 
                elif msg.text in ["นับ"]:
                    nn2(to,"「 NEVERDIE BOT」")
                    time.sleep(1)
                    nn3(to,"💓💙 1 💛💖")
                    time.sleep(1)
                    nn3(to,"💞💜 2 💖💞")
                    time.sleep(1)
                    nn3(to,"💝🖤 3🧡💛")
                    time.sleep(1)
                    nn3(to,"💝🖤 4🧡💛")
                    time.sleep(1)
                    nn3(to,"💞💜 5 💖💞")
                    time.sleep(1)
                    nn3(to,"💝🖤 6 ??💛")
                    time.sleep(1)
                    nn3(to,"💝🖤 7 🧡💛")
                    time.sleep(1)
                    nn3(to,"💓💙 8 💛💖")
                    time.sleep(1)
                    nn3(to,"💞💜 9 💖💞")
                    time.sleep(1)
                    nn3(to,"??🖤 10 ??💛")
                    time.sleep(1)
                    nn2(to,"👉เสร็จละจ้าา" +datetime.today().strftime('%H:%M:%S')+ "👈")
                   
                elif msg.text in ["นับไทย"]:
                    nn2(to,"「 NEVERDIE BOT」")
                    time.sleep(1)
                    nn3(to,"🖤🧡 ๑ 💝💓")
                    time.sleep(1)
                    nn3(to,"💖💙 ๒ 💞🧡")
                    time.sleep(1)
                    nn3(to,"💛❤ ๓ 💝💞")
                    time.sleep(1)
                    nn3(to,"💝🖤 ๔ 🧡💛")
                    time.sleep(1)
                    nn3(to,"💛❤ ๕ 💝💞")
                    time.sleep(1)
                    nn3(to,"💞💜 ๖ 💖💞")
                    time.sleep(1)
                    nn3(to,"💓💙 ๗ 💛💖")
                    time.sleep(1)
                    nn3(to,"💝🖤 ๘ 🧡💛")
                    time.sleep(1)
                    nn3(to,"💞💜 ๙ 💖💞")
                    time.sleep(1)
                    nn3(to,"💛❤ ๑๐ 💝💞")
                    time.sleep(1)
                    nn2(to,"👉เสร็จละจ้า" +datetime.today().strftime('%H:%M:%S')+ "👈")
                                  
                elif msg.text in ["นับสเปน"]:
                    nn2(to,"「NEVERDIE BOT」")
                    time.sleep(1)                   
                    nn3(to,"1✴•••  รีลมาดริด•••✴")
                    time.sleep(1)
                    nn3(to,"2✴••• บาเซโลน่า•••✴")
                    time.sleep(1)
                    nn3(to,"3✴••• บาเลนเซีย•••✴")
                    time.sleep(1)
                    nn3(to,"4✴••• แอตมาดริด•••✴")
                    time.sleep(1)
                    nn3(to,"5✴••• ลาคอรุนญ่า•••✴")
                    time.sleep(1)
                    nn3(to,"6✴•••เอสปันญ่อล•••✴")
                    time.sleep(1)
                    nn3(to,"7✴•••  โอซาซูน่า•••✴")
                    time.sleep(1)
                    nn3(to,"8✴••• ซาราโกซ่า•••✴")
                    time.sleep(1)
                    nn3(to,"9✴•••• บียาร์รีลล์•••✴")
                    time.sleep(1)
                    nn3(to,"0✴••• เรอัลเบติส•••✴")
                    time.sleep(1)
                    nn2(to,"👉เสร็จละจ้า" +datetime.today().strftime('%H:%M:%S')+ "👈")    
                                 
                elif msg.text in ["นับอังกฤษ"]:
                    nn2(to,"「NEVERDIE BOT」")
                    time.sleep(1)                  
                    nn3(to,"✴ •••One••• ✴")
                    time.sleep(1)
                    nn3(to,"✴ •••Two••• ✴")
                    time.sleep(1)
                    nn3(to,"✴ •••Three••• ✴")
                    time.sleep(1)
                    nn3(to,"✴ •••Four•••• ✴")
                    time.sleep(1)
                    nn3(to,"✴ •••Five••• ✴")
                    time.sleep(1)
                    nn3(to,"✴ •••Six••• ✴")
                    time.sleep(1)
                    nn3(to,"✴ •••Seven••• ✴")
                    time.sleep(1)
                    nn3(to,"✴  •••Eight•••  ✴")
                    time.sleep(1)
                    nn3(to,"✴ •••Nine••• ✴")
                    time.sleep(1)
                    nn3(to,"✴ •••Zero••• ✴")
                    time.sleep(1)
                    nn2(to,"👉เสร็จละจ้า" +datetime.today().strftime('%H:%M:%S')+ "👈")

                elif msg.text in ["นับอินโด"]:
                    nn2(to,"「NEVERDIE BOT」")
                    time.sleep(1)
                    nn3(to,"🎀1 •••Satu••• 💖")
                    time.sleep(1)
                    nn3(to,"🎀2••••Dua•••• 💖")
                    time.sleep(1)
                    nn3(to,"🎀3 •••Tiga••• 💖")
                    time.sleep(1)
                    nn3(to,"🎀4 ••Empat••• 💖")
                    time.sleep(1)
                    nn3(to,"🎀5  ••Lima••• 💖")
                    time.sleep(1)
                    nn3(to,"🎀6•••Enam••• 💖")
                    time.sleep(1)
                    nn3(to,"🎀7  ••Tujuh••• 💖")
                    time.sleep(1)
                    nn3(to,"🎀8 •Delapan••• 💖")
                    time.sleep(1)
                    nn3(to,"🎀9 Sembilan 9 ••• 💖")
                    time.sleep(1)
                    nn3(to,"🎀0 ••••Nol•••• 💖")
                    time.sleep(1)
                    nn2(to,"👉เสร็จละจ้า" +datetime.today().strftime('%H:%M:%S')+ "👈")   
                  
                elif msg.text in ["นับ1"]:
                    nn2(to,"「NEVERDIE BOT」\n✪••••••✪ℕℕ❂••••••✪")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n🧡🧡[[[[[ 1 ]]]]]🧡🧡\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n🖤🖤[[[[[ 2 ]]]]]🖤🖤\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n💙💙[[[[[ 3 ]]]]]💙💙\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n❤❤[[[[[ 4 ]]]]]❤❤\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n💛💛[[[[[ 5 ]]]]]💛💛\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n💜💜[[[[[ 6 ]]]]]💜💜\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n💗💗[[[[[ 7 ]]]]]💗💗\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n❣️❣️[[[[[ 8 ]]]]]❣️❣️\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n💖ั💖[[[[[ 9 ]]]]]💖💖\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn3(to,"✪••••••✪𝕊𝕋❂••••••✪\n💟💟[[[[[ 0 ]]]]]💟💟\n ••••• " +datetime.today().strftime('%H:%M:%S')+ " •••••")
                    time.sleep(1)
                    nn2(to,"👉เสร็จละจ้า" +datetime.today().strftime('%H:%M:%S')+ "👈")   
#----------------------------------------------------------------------------#
                elif "แฟลช" == msg.text.lower():
                    nn2(to,"👉🎀「ความเร็ว...」🎀👈")
                    time.sleep(1)
                    nn3(to,"███▒39%")
                    time.sleep(1)
                    nn3(to,"██████▒69%")
                    time.sleep(1)
                    nn3(to,"██████████▒99%")
                    time.sleep(1)
                    nn3(to,"0.0000000000000000 second")
                    time.sleep(1)
                    nn3(to,"👉🎃"+datetime.today().strftime('%H:%M:%S')+ "🎃👈")      

                elif "n" == msg.text.lower():
                    nn3(to,"꧁͜͡꧂🍁𝕊𝕋🍁꧁͜͡꧂")
                    time.sleep(0.7)
                    nn3(to,"CREATOR ST SELFBOT\nNLOGIN")
                    time.sleep(0.7)
                    nn3(to,"🔥🎃NEVERDIE BOT LINE🎃🔥\n✪••••••✪𝕊𝕋❂••••••✪") 

                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    nn3(msg.to, A)

                elif text.lower() == 'ปฏิทิน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "🔥NEVERDIE BOT🎃\n\n🔥💖💜❤💛🧡💖💓🖤💜💜💖" + "\n\n🍁" + hasil + "\n🍁 ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\n🍁 เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]" + "\n🔥💖💜❤💛🧡💖💓🖤💜💜💖" + "\n\nBY: 💖𝕊𝕋 ₦Ɇ⩔ɆɌƉƗɆɃØ₮"
                    nn2(msg.to, readTime)   

                elif msg.text in ["การบล็อค"]: 
                    blockedlist = nn1.getBlockedContactIds()
                    kontak = nn1.getContacts(blockedlist)
                    num=1
                    msgs="🚫รายการบัญชีที่ถูกบล็อค🚫"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🚫รายการบัญชีที่ถูกบล็อค🚫\n\nTotal Blocked : %i" % len(kontak)
                    nn2.sendMessage(receiver, msgs)

                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    nn1.sendAudio(msg.to,"hasil.mp3")  
#============= โหมดกิฟสติ้กเกอร์ ==============================================================================================    
                elif msg.text in ["นักฆ่า"]:
                   chivaree1={"type":"template","altText":"✯ ST Sticker ✯","template":{
                     "type":"image_carousel","columns":[{"imageUrl":"https://img.live/images/2019/01/03/a019.gif","size":"xxxl","aspectRatio":"1:2","action":{
                             "type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=••✯%20NEVERDIE%20✯••",}}]}}
                   chivaree2={"type":"template","altText":"✯ ST ✯","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VL3pa.gif",
                                       "size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=••✯%20™NEVERDIE%20✯••",}}]}}
                   sendTemplate(to, chivaree1)
                   sendTemplate(to, chivaree2)                
                elif msg.text in ["บึ้ม","บ้านบึ้ม"]:
                   chivaree={"type":"template","altText":"✯ ST Sticker ✯","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/02/07/TQsIAy.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=••✯%20NEVERDIE%20✯••",}}]}}
                   sendTemplate(to, chivaree)
                elif text.lower() == "เค้าสั่น":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VmsQW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้างง":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VmeZR.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                  
                elif msg.text in ["เค้าดีใจ","เย้ๆ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9Vmms0.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าเขิล":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://img.live/images/2019/01/02/chivaree3.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif msg.text in ["เค้าอาย"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VmI9Z.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif text.lower() == "เค้าเชื่อ":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VySrl.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าโอเค":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://img.live/images/2019/01/02/chivaree78.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าไม่เถียง":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9Vvzdu.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                  
                elif msg.text in ["เค้าเผ่น","วิ่งๆ","เผ่นสิ"]:
                   data={"type":"template","altText":"🌟?? ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/12/9Hj89n.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าเครียด":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9X4Vjl.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif msg.text in ["เค้าหิว"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VvMFQ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif text.lower() == "เค้าพร้อม":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://img.live/images/2019/01/03/a011.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าชอบ":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9X4Wxu.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                  
                elif msg.text in ["อาบน้ำ","เค้าอาบน้ำ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9Vvoyb.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)         
                elif text.lower() == "เค้าจะเอา":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9X4dnZ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif text.lower() == "จัดไป":
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSGn2t.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif msg.text in ["โยก","โยกๆ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSGHTl.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)              
                elif msg.text in ["ว้าว","ว้าวว"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSGItW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                     
                elif msg.text in ["ขอบคุณ","ขอบคุน"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSJt50.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                      
                elif msg.text in ["เห้อ","เห้ออ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSJsJ2.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["เศร้า","เบื่อ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSJvLz.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["โอเค","โอเคร"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSJIuI.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                    
                elif msg.text in ["กัปตัน","แคป"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSewZI.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)   
                elif msg.text in ["วานด้า","วันด้า"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSe1sP.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif msg.text in ["แนท","นาตาชา"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSec9e.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                    
                elif msg.text in ["ฟรุ้งฟริ้ง","มุ้งมิ้ง"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSeQUE.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["ยิง","เหอะ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSebyn.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                    
                elif msg.text in ["บาย","ไปละ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSesUy.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["หึหึ","ธานอส"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSeGH0.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)             
                elif msg.text in ["เย่","ธอร์"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSmgIb.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["เบิดเดย์","วันเกิด"]:
                   data={"type":"template","altText":"🌟?? ST Sticker 🌟??","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSmqhz.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                    
                elif msg.text in ["ชอบ","ถูกใจ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSm6Vv.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                  
                elif msg.text in ["น่ารัก","น่ารักก"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSmrYE.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["รัก","รักนะ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSyqPS.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["เหรอ","ใช่เหรอ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSybbW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["ร้อน","ร้อนน"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSyja2.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["จุฟ","จุฟๆ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSFHtS.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                  
                elif msg.text in ["สวัสดี","หวัดดี"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSFvq2.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["โหล","ฮาโหล"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSFMof.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif msg.text in ["ฝันดี","ฝรรดี"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSI4i0.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif msg.text in ["เผ่น","เผ่นๆ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSIZiE.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif msg.text in ["เพลีย","เพลียย"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSMjae.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["เร็ว","ไวๆ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSMo4l.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)               
                elif msg.text in ["ล้อเล่นๆ","ล้อเล่นๆๆ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSMDQk.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                     
                elif msg.text in ["พิม่อน"]:
                   chivaree1={"type":"template","altText":"✯ ST Sticker ✯","template":{
                     "type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/17/Z9G3G9.gif","size":"xxxl","aspectRatio":"1:2","action":{
                             "type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=••✯%20AVENGERS%20✯••",}}]}}
                   chivaree2={"type":"template","altText":"✯ ST ✯","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/17/Z9GK7a.gif",
                                       "size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=••✯%20™AVENGERS%20✯••",}}]}}   
                   chivaree3={"type":"template","altText":"✯ ST ✯","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/17/Z9GgF8.gif",
                                       "size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=••✯%20™AVENGERS%20✯••",}}]}}     
                   sendTemplate(to, chivaree1)
                   sendTemplate(to, chivaree2)
                   sendTemplate(to, chivaree3)           
                elif msg.text in ["เหอะๆ","ต่าย"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/17/ZThcTy.png","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)              
                elif msg.text in ["ยิง2","ยิง!"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/Zg0Nxf.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["มา","มานี่"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/Zg0t30.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["อ้อน","อ้อนๆ"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/Zg01aZ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)              
                elif msg.text in ["สติช","สแตช"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/ZgSBwz.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)           
                elif msg.text in ["สติช2","สแตช2"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/ZgSORS.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["สติช3","สแตช3"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/ZgSo1W.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)               
                elif msg.text in ["นาซ่า","ทีมบิน"]:
                   data={"type":"template","altText":"🌟🌟 ST Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/ZgSAL1.png","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
#----------------------------------------------------------------------------------------------------------------------- 
                elif msg.text.lower().startswith("ส่งหัวใจ "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                nn1.sendMessage(receiver,"💖•💗•รั.ก.น่.ะ.ค่.ะ.จุ้.ฟ.ๆ•💗•💖\n💖•💗•รั.ก.น่.ะ.ค่.ะ.จุ้.ฟ.ๆ•💗•💖\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                nn1.sendMessage(receiver,"💖•💗•รั.ก.น่.ะ.ค่.ะ.จุ้.ฟ.ๆ•💗•💖\n💖•💗•รั.ก.น่.ะ.ค่.ะ.จุ้.ฟ.ๆ•💗•💖\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                nn1.sendMessage(to, "💗•ส่งในแชทสต.แล้วคับ•💗".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith("ส่งคลิป "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                nn1.sendMessage(receiver, "🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                nn1.sendMessage(receiver, "🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                nn1.sendMessage(to, "🌀ดูคลิปเด็ดในแชท สต.น่ะคับ🌀".format(str(jml)))
#                                
                elif msg.text.lower().startswith("แจกของขวัญ "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                nn1.sendGift(receiver, '1002077','sticker')
                                nn1.sendMessage(to, "🎁•รับทางแชทสต.นะคับ•🎁".format(str(jml)))
                            else:
                                pass
                
                elif msg.text.lower().startswith("ส่งนอน "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                nn1.sendMessage(receiver,"🌙•หลับฝันดีน่ะคับที่รัก จุ๊ฟป้อก•🌙\n🌙•หลับฝันดีน่ะคับที่รัก จุ๊ฟป้อก•🌙\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                nn1.sendMessage(receiver, "🌙•หลับฝันดีน่ะคับที่รัก จุ๊ฟป้อก•🌙\n🌙•หลับฝันดีน่ะคับที่รัก จุ๊ฟป้อก•🌙\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                nn1.sendMessage(to, "🌙•ส่งในแชทสต.แล้วคับ•🌙".format(str(jml)))
                            else:
                                pass
                                
                elif msg.text.lower().startswith("ส่งความรัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                nn1.sendMessage(receiver, "💖.ฉั.น.รั.ก.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.ฉั.น.รั.ก.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                nn1.sendMessage(receiver, "💖.ฉั.น.รั.ก.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.ฉั.น.รั.ก.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                nn1.sendMessage(to, "💗•ส่งในแชทสต.แล้วคับ•💗".format(str(jml)))
                            else:
                                pass 
                    
                elif msg.text.lower().startswith("ส่งความคิดถึง "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                nn1.sendMessage(receiver, "💖.คิ.ด.ถึ.ง.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.คิ.ด.ถึ.ง.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\nไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                                nn1.sendMessage(receiver, "💖.คิ.ด.ถึ.ง.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💖.คิ.ด.ถึ.ง.เ.ธ.อ.ที่.สุ.ด.เ.ล.ย.💖\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.??.🤗.💚")
                                nn1.sendMessage(to, "💗•ส่งในแชทสต.แล้วคับ•💗".format(str(jml)))
                            else:
                                pass                       

                elif msg.text.lower().startswith("ส่งของขวัญ "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                nn1.sendMessage(receiver,"คุ.ณ.ไ.ด้.รั.บ.ข.อ.ง.ข.วั.ญ.ค่.ะ.🎁\nคุ.ณ.ไ.ด้.รั.บ.ข.อ.ง.ข.วั.ญ.ค่.ะ.🎁\n💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                nn1.sendMessage(receiver,"คุ.ณ.ไ.ด้.รั.บ.ข.อ.ง.ข.วั.ญ.ค่.ะ.🎁\nคุ.ณ.ไ.ด้.รั.บ.ข.อ.ง.ข.วั.ญ.ค่.ะ.🎁\n💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                nn1.sendMessage(to, "🎁•รับทางแชทสต.นะคับ•🎁".format(str(jml)))
                            else:
                                pass                   
#---------------------[คำสั่งเรียกกิฟ]-------------------------------------------------------------------------------#
                elif text.lower() == "กิฟ" or text.lower() == "n6":
                    sas = "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯͜͡❂➣\n"
                    sa = "• นักฆ่า \n"
                    sa += "• บึ้ม\n"
                    sa += "• เค้าสั่น\n"
                    sa += "• เค้างง\n"
                    sa += "• เค้าดีใจ\n"
                    sa += "• เค้าเขิล\n"
                    sa += "• เค้าอาย\n"
                    sa += "• เค้าเชื่อ\n"
                    sa += "• เค้าโอเค\n"
                    sa += "• เค้าไม่เถียง\n"
                    sa += "• เค้าเผ่น\n"
                    sa += "• เค้าเครียด\n"
                    sa += "• เค้าหิว\n"
                    sa += "• เค้าพร้อม\n"
                    sa += "• เค้าชอบ\n"
                    sa += "• อาบน้ำ\n"
                    sa += "• เค้าจะเอา\n"
                    sa += "• จัดไป\n"
                    sa += "• โยก\n"
                    sa += "• ว้าว\n"                  
                    sa += "• ขอบคุณ\n"
                    sa += "• เห้อ\n"
                    sa += "• เศร้า\n"
                    sa += "• โอเคร\n"
                    sa += "• กัปตัน\n"
                    sa += "• วันด้า\n"
                    sa += "• แนท\n"
                    sa += "• ฟรุ้งฟริ้ง\n"
                    sa += "• ยิง\n"
                    sa += "• บาย\n"
                    sa += "• หึหึ\n"
                    sa += "• เย่\n"
                    sa += "• เบิดเดย์\n"
                    sa += "• ถูกใจ\n"
                    sa += "• น่ารัก\n"
                    sa += "• รัก\n"
                    sa += "• เหรอ \n"
                    sa += "• ร้อน\n"
                    sa += "• จุฟ\n"
                    sa += "• สวัสดี\n"
                    sa += "• ฮาโหล\n"
                    sa += "• ฝันดี\n"
                    sa += "• เผ่น\n"
                    sa += "• เพลีย\n"
                    sa += "• เร็ว\n"
                    sa += "• ล้อเล่น\n"
                    helps = "{}".format(str(sa))
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": sas,
                                        "size":"xl",
                                        "weight":"bold",
                                        "color":"#CC0000",
                                        "align":"center"
                                    },
                                    {
                                        "type":"text",
                                        "text": " "
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#66FFFF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type":"button",
                                        "style":"primary",
                                        "color":"#CC0000",
                                        "action": {
                                            "type":"uri",
                                            "label":"NEVERDIE BOT",
                                            "uri":"line.me/ti/p/~steveneverdie002"
                                        },
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)  
#----------------------------------------------------------------------------------------------------#
                elif text.lower() == "คำสั่ง2" or text.lower() == "ลูกเล่น":
                    sas = "🔥NEVERDIE BOT🔥\n"
                    sa = "• เทสบอท \n"
                    sa += "• เทส/เทส2\n"
                    sa += "• นับอังกฤษ\n"
                    sa += "• นับสเปน\n"
                    sa += "• นับอินโด\n"
                    sa += "• นับ1\n"
                    sa += "• ปักหมุด\n"
                    sa += "• ลบหมุด\n"
                    sa += "• บอกหมุด: [ข้อความ]\n"
                    sa += "• บอกหมุด2: [ข้อความ]\n"
                    sa += "• บอกหมุด3: [ข้อความ]\n"
                    sa += "• บอกหมุด4: [ข้อความ]\n"
                    sa += "• ลิสหมุด\n"
                    sa += "• ด่า\n"
                    sa += "• นับ\n"
                    sa += "• ส่งหัวใจ จำนวน @\n"
                    sa += "• ส่งคลิป จำนวน @\n"
                    sa += "• แจกของขวัญ จำนวน @\n"
                    sa += "• ส่งนอน จำนวน @\n"
                    sa += "• ส่งความรัก จำนวน @\n"
                    sa += "• ส่งความคิดถึง จำนวน @\n"
                    sa += "• ส่งของขวัญ จำวน @\n"                  
                    sa += "• กิฟ\n"
                    sa += "• เตะควาย\n"
                    sa += "• ประหารชีวิต\n"
                    sa += "• เชคบัค\n"
                    sa += "• แฟลช\n"
                    sa += "• ขอรูป\n"
                    sa += "• Poto [ อังกฤษ]\n"
                    sa += "• ตั้งรูปโปรไฟล์ \n"
                    sa += "• วีดีโอเรา\n"
                    sa += "• เปิดapi/ปิดapi\n"
                    sa += "• นับไทย\n"      
                    sa += "• พูด [ข้อความ]\n"
                    sa += "• เวลา\n"
                    sa += "• ปฏิทิน\n"                    
                    sa += "• Gift/แจก\n"
                    sa += "• Tr-th ข้อความ[แปลภาษา]\n"
                    sa += "──────────────\n"
                    sa += "• NEVERDIE BOTLINE•\n"
                    sa += "──────────────\n"
                    helps = "{}".format(str(sa))
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": sas,
                                        "size":"xl",
                                        "weight":"bold",
                                        "color":"#FF6600",
                                        "align":"center"
                                    },
                                    {
                                        "type":"text",
                                        "text": " "
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#66FFFF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type":"button",
                                        "style":"primary",
                                        "color":"#FF6600",
                                        "action": {
                                            "type":"uri",
                                            "label":"NEVERDIE BOT",
                                            "uri":"line.me/ti/p/~steveneverdie002"
                                        },
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)                     
#-----------------------------------------------------------------------------------------#  
#                # สกิล ตัวแปล Chivaree5 Help โดย  nn
                elif msg.text in ["โค้ดลับ"]:
                            sender_profile = nn1.getContact(sender)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                                     },
                         "header": {
                         "type": "box",
                          "layout": "vertical",   
                          "contents": [
                                          {     
                                             "type": "text",
                                             "text": "🌟™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯͜͡❂➣🌟",
                                             "color": "#66FFFF",
                                              "weight": "bold",
                                              "align": "center"
                                            }
                                         ]
                                      },
                         "hero": {
                         "type": "image",
                         "url": "https://www.img.live/images/2019/09/17/343498.jpg",
                         "size": "lg",
                         "action": {
                                 "type":"uri","uri":"line://app/1602687308-GXq4Vvk9?type=image&img=https://www.img.live/images/2019/09/17/20190917_163605.jpg"
                                 }
                       },
                       "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัส「Virus Code Cr.เอจัง」",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสปีโป้",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสคิทตี้",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสสีชมพู",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                 "text": "•♡• ไวรัสชิวารี",
                                                 "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสแมนยู",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสฟรุตตี้",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสรวมมิตร",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสผลไม้",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสฟรุ้งฟริ้ง",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสมุ้งมิ้ง",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสเจเล่",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสป๊อกกี้",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสเยลลี่",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสแอ๊บแบ๊ว",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": 'https://www.img.live/images/2019/09/17/343432.jpg',
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯͜͡❂➣",
                                                        "align": "center",
                                                        "color": "#66FFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                                     },
                         "header": {
                         "type": "box",
                          "layout": "vertical",   
                          "contents": [
                                          {     
                                             "type": "text",
                                             "text": "🌟™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯͜͡❂➣🌟",
                                             "color": "#66FFFF",
                                              "weight": "bold",
                                              "align": "center"
                                            }
                                         ]
                                      },
                         "hero": {
                         "type": "image",
                         "url": "https://sv1.picz.in.th/images/2019/08/09/ZWrSvW.jpg",
                         "size": "lg",
                         "action": {
                                 "type":"uri","uri":"line://app/1602687308-GXq4Vvk9?type=image&img=https://www.img.live/images/2019/09/17/20190917_163605.jpg"
                                 }
                       },
                       "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสเอจัง",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                             {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสเอจัง2",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสเอจัง3",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสแห่งความมืด",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสแห่งความรัก",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสชนบท",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ไวรัสอวตาร",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไวรัสดาวอังคาร",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• เอจังวางระเบิด",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ระเบิดเวลาเอจัง",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• Hello Kitty",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ปีโป้อร่อยจัง",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• รันไวรัส 「@ชื่อ」",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• รันปีโป้ 「@ชื่อ」",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ผู้สร้างไวรัส",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": 'https://www.img.live/images/2019/09/17/343432.jpg',
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯͜͡❂➣",
                                                        "align": "center",
                                                        "color": "#66FFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                                     },
                         "header": {
                         "type": "box",
                          "layout": "vertical",   
                          "contents": [
                                          {     
                                             "type": "text",
                                             "text": "🌟™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯͜͡❂➣🌟",
                                             "color": "#66FFFF",
                                              "weight": "bold",
                                              "align": "center"
                                            }
                                         ]
                                      },
                         "hero": {
                         "type": "image",
                         "url": "https://www.img.live/images/2019/09/17/343486.jpg",
                         "size": "lg",
                         "action": {
                                 "type":"uri","uri":"line://app/1602687308-GXq4Vvk9?type=image&img=https://www.img.live/images/2019/09/17/20190917_163605.jpg"
                                 }
                       },
                       "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                 "type": "text",
                                                "text": "•♡• ไฮโล 「สุ่มเปิดไฮโล」",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• เต้าปูปลา 「สุ่มเต้าปูปลา」",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                             {
                                                 "type": "text",
                                                "text": "•♡• เศษตังแม่, พ่อกูรวย",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• เราจังด่า",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• ใครเกรียนสุด",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• ใครสวยสุด",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• เอจังนับ, นับ",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "•♡• นับจีน",
                                                "size": "sm",
                                                "color": "#66FFFF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "•♡• นับไทย",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• นับอินโด",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• นับไฮโซ",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• นับสเปน",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• นับอังกฤษ",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• Nnopen",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "•♡• Nnclose",
                                                "size": "sm",
                                                 "color": "#66FFFF",
                                                 'flex': 1,
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": 'https://www.img.live/images/2019/09/17/343432.jpg',
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯͜͡❂➣",
                                                        "align": "center",
                                                        "color": "#66FFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "✯• Chivaree Help5 •✯",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)                          
#---------------------------------------------------------------------------------------------------------------------------#
#📌📌  ปักหมุด modifile by: nn # ปักครั้งเดียว บอกหมุด4รูปแบบ
#---------------------------------------------------------------------------------------------------------------------------#
#----------------------------ปักหมุดเฟก BY: NN-------------------------------------------------------------------#                                      
                elif msg.text in ["ลิสหมุด"]:
                    a = nn1.getGroupIdsJoined()
                    ret_ = " 📌รายชื่อกลุ่มที่ปักหมุด📌"
                    num = 1
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            group = nn1.getGroup(manusia)
                            ret_ += "\n {}. {} | {}".format(str(num), str(group.name), str(len(group.members)))
                            num=(num+1)					
                    nn2(to, str(ret_))
#----------------------------------------------------------------------------#
                elif msg.text in ["ปักหมุด"]:
                    apalo["bc"][receiver] = True
                    nn3(receiver,"「📌 ปักหมุดกลุ่มนี้เรียบร้อย 」")
                   
                elif msg.text in ["ลบหมุด"]:
                    try:
                        del apalo["bc"][receiver]
                        nn3(receiver,"「📌 ลบหมุดออกเรียบร้อย 」")
                    except:
                        nn3(receiver,"「📌 ลบหมุดออกเรียบร้อย 」")
#----------------------[บอกหมุด 4 รูปแบบ]------------------------------------------------------#                 
                elif "บอกหมุด: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด: ", "")
                    a = nn1.getGroupIdsJoined()
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            nn1.sendMessage(manusia,(bctxt))
                            time.sleep(1)
                    nn3(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")  
               
                elif "บอกหมุด2: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด2: ", "")
                    a = nn1.getGroupIdsJoined()
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            nn2(manusia,(bctxt))
                            time.sleep(1)
                    nn3(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")
             
                elif "บอกหมุด3: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด3: ", "")
                    a = nn1.getGroupIdsJoined()
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            nn3(manusia,(bctxt))
                            time.sleep(1)
                    nn3(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")
             
                elif "บอกหมุด4: " in msg.text.lower():
                    bctxt = msg.text.replace("บอกหมุด4: ", "")
                    a = nn1.getGroupIdsJoined()
                    for manusia in apalo["bc"]:
                        if manusia in a:
                            nn4(manusia,(bctxt))
                            time.sleep(1)
                    nn3(receiver,"「📌 ส่งกลุ่มที่ปักหมุดแล้ว 」")                   
#-----------------------------ลบรัน1---------------------------------------------------#                                
                elif text.lower() == 'ลบรัน1':
                         gid = nn1.getGroupIdsInvited()  
                         k = len(gid)//10     
                         num = 1                     
                         for i in range(k+1):
                            for j in gid[i*20 : (i+1)*20]: 
                               time.sleep(random.uniform(4.5,5.0))                                  	
                               nn1.acceptGroupInvitation(j)
                               nn1.leaveGroup(j)
                               print(j)
                         nn2(msg.to,"「 ลบรันเรียบร้อย 」")                                                      
#----------------------------------------------------------------------------#                       
                elif msg.text.lower().startswith("ก็อป "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = nn1.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = nn1.getContact(she);ClonerV2(she)
                                    nn2(to, "=͟͟͞͞➳ คุณกำลังก็อปปี้สำเร็จแล้ว >_<");nn1.sendContact(to, str(BackupProfile.mid));nn1.sendContact(to, str(contact.mid))
                
                elif text.lower() == "กลับร่าง":
                            try:
                                nn1status = nn1.getProfile()
                                nn1Name = nn1.getProfile()
                                nn1Name.statusMessage = ProfileMe["statusMessage"]
                                nn1Name.pictureStatus = str(ProfileMe["pictureStatus"])
                                nn1.updateProfile(nn1status)
                                nn1Name.displayName = ProfileMe["NameMe"]
                                nn1.updateProfile(nn1Name)
                                path = nn1.downloadFileURL(ProfileMe["PictureMe"])
                                nn1.updateProfilePicture(path)
                                coverId = ProfileMe["coverId"]
                                nn1.updateProfileCoverById(coverId)
                                BackupProfile = nn1.getContact(sender)
                                sendMention(to, BackupProfile.mid, "🐱 กลับบัญชีเดิมเรียบร้อย 🐱", "™T̶e̶a̶m̶b̶o̶t̶ ̶a̶v̶e̶n̶g̶e̶r̶s̶✯");nn1.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
                                nn2(to,"🐱 คุณยังไม่ได้ก็อปปี้ 🐱")
#----------------------------------------------------------------------------#                                
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               nn1.sendMessage(msg.to, teks)
                        else:
                           nn1.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            nn1.sendMessage(msg.to, tulisan)
                        else:
                            nn1.sendMessage(msg.to, "Out Of Range!")
#----------------------------------------------------------------------------#                            
                if cmd in ["ชื่อเรา","ตัสเรา","mid","รูปเรา","ปกเรา","คทเรา","วีดีโอเรา"]:
                    commandMidContact(to, sender, cmd)
#----------------------------------------------------------------------------#                    
                elif msg.text.lower().startswith("ทัก "):
                  text = msg.text.split(' ')
                  search = msg.text.replace(text[0] + ' ','')
                  for x in range(search):
                     RhyN_(to, to)
#----------------------------------------------------------------------------#                     
                elif msg.text.lower().startswith("เขียน3 "):
                  text = msg.text.split(' ')
                  search = msg.text.replace(text[0] + ' ','')
                  r = requests.get('http://api.zicor.ooo/graffiti.php?text={}'.format(str(search)))
                  data = json.loads(r.text)
                  sendTemplate(to,{'type':'template','altText':'Graffiti','template':{'type':'image_carousel','columns':[{'imageUrl':str(data['image']),'action':{'type':'uri','uri':'line://app/1644992891-KOnapywG?type=image&img='+str(data['image'])}}]}})
#----------------------------------------------------------------------------#                  
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nn1.getContact(ls)
                            mi_d = contact.mid
                            nn1.sendContact(msg.to, mi_d)
#----------------------------------------------------------------------------#                            
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nn1.getContact(ls)
                            mi_d = contact.statusMessage
                            nn1.sendMessage(msg.to, mi_d)
#----------------------------------------------------------------------------#                            
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nn1.getContact(ls)
                            mi_d = contact.displayName
                            nn1.sendMessage(msg.to, mi_d)
#----------------------------------------------------------------------------#                            
                elif msg.text.lower().startswith("mid "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = "「 Mid User 」"
                                for ls in lists:
                                    ret_ += "\n{}".format(str(ls))
                                nn1.generateReplyMessage(msg.id)
                                nn1.sendReplyMessage(msg.id, to, str(ret_))
#----------------------------------------------------------------------------#                                
                elif msg.text.lower().startswith("รูป "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                	gg = 'http://dl.profile.line-cdn.net/' + nn1.getContact(ls).pictureStatus
                                nn1.generateReplyMessage(msg.id)
                                nn1.sendReplyImageWithURL(msg.id, to, str(gg))
#----------------------------------------------------------------------------#                                
                elif msg.text.lower().startswith("ปก "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                	gg = nn1.getProfileCoverURL(ls)
                                nn1.generateReplyMessage(msg.id)
                                nn1.sendReplyImageWithURL(msg.id, to, str(gg))
#----------------------------------------------------------------------------#                        
                elif text.lower() == "!me":
                            s = temp["te"]
                            a = temp["t"]
                            contact = nn1.getContact(nn1MID)
                            cover = nn1.getProfileCoverURL(nn1MID)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                    },
                                    "body": {
                                       "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "weight": "bold",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐱 รูปโปรไฟล์ 🐱",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                       ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+nn1MID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "line.me/ti/p/~steveneverdie002"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(cover),
                                        "size": "full",
                                        "aspectRatio":"20:13",
                                        "aspectMode":"cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.mid),
                                                "align": "center",
                                                "color": s,
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐱 รูปปกพื้นหลัง 🐱",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+nn1MID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~steveneverdie002"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "🐱 ชื่อของคุณ 🐱",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "color": s,
                                                "size": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "align": "center",
                                                "color": a,
                                                "size": "sm",
                                            },
                                            {
                                                "type": "text",
                                                "text": "🐱 สเตตัสของคุณ 🐱",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.statusMessage),
                                                "align": "center",
                                                "color": s,
                                                "wrap": True,
                                                "size": "md"
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+nn1MID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~steveneverdie002"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(contact.displayName),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
#----------------------------------------------------------------------------#                            
                if text.lower() == "ออน" or text.lower() == "runtime":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "⇨ เวลาออน ⇦\n"
                    run += runtime
                    data = {
                        "type": "flex",
                        "altText": "{}".format(run),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [                        
                                    {
                                        "type": "text",
                                        "text": "{}".format(run),
                                        "wrap": True,
                                        "color": "#99FFFF",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
#--------------------------------------------------------------------------------------------------#                   
                if text.lower() == "ออน2" or text.lower() == "online":
                    contact = nn1.getContact(sender)
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)   
                    a = "วันที่"+ datetime.strftime(timeNow,'%d-%m-%Y')+"🇹??เวลา"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n"
                    run = "「 เวลาออนบอท 」\n"
                    run += runtime
                    data = {
                            "type": "flex",
                            "altText": "{}".format(run),
                            "contents": {
                            "styles": {
                              "body": {
                                "backgroundColor": "#000000"
                              },
                              "footer": {
                                "backgroundColor": "#000000"
                              }
                            },
                            "type": "bubble",
                            "body": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                                      "type": "image"
                                    },
                                    {
                                      "type": "separator",
                                      "color": "#CC0000"
                                    },
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                                      "type": "image"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "horizontal"
                                },
                                {
                                  "type": "separator",
                                  "color": "#CC0000"
                                },
                                {
                                  "contents": [
                                    {
                                      "text": "🔥เวลาออนไลน์ของบอท🔥",
                                      "size": "lg",
                                      "align": "center",
                                      "color": "#CC0000",
                                      "wrap": True,
                                      "weight": "bold",
                                      "type": "text"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "vertical"
                                },
                                {
                                  "type": "separator",
                                  "color": "#CC0000"
                                },
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "{}".format(run),
                                          "size": "lg",
                                          "align": "center",
                                          "margin": "none",
                                          "color": "#CC0000",
                                          "wrap": True,
                                          "weight": "regular",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    },
                                  ],
                                  "type": "box",
                                  "layout": "vertical"
                                }
                              ],
                              "type": "box",
                              "spacing": "md",
                              "layout": "vertical"
                            },
                            "footer": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "NEVERDIE BOT",
                                          "size": "xl",
                                          "action": {
                                            "uri": "line.me/ti/p/~steveneverdie002",
                                            "type": "uri",
                                            "label": "Add Hacker"
                                          },
                                          "margin": "xl",
                                          "align": "center",
                                          "color": "#CC0000",
                                          "weight": "bold",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    }
                                  ],
                                  "type": "box",
                                  "layout": "horizontal"
                                }
                              ],
                              "type": "box",
                              "layout": "vertical"
                            }
                        }
                    }
                    sendTemplate(to, data)   
#--------------------------------------ออน3---------------------------------------------------------#                 
                elif text.lower() == 'ออน3':
                    contact = nn1.getContact(sender)
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    van = " ระยะเวลาการทำงานของบอท\n"  +format(str(runtime))+"\n ◐วันที่ : "+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n ◐เวลา [ "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n『AVENGERS BOT』"
                    data={
                        'type': 'flex',
                        'altText': 'NEVERDIE BOT',
                                'contents': {
                            "type": "bubble",
                            "header": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "NEVERDIE BOT",
                                        "weight": "bold",
                                        "color": "#FFFFFF",
                                        "align": "center"
                                    }
                                ]
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": van,
                                        "size": "sm",
                                         "align": "center",
                                        "weight": "bold",
                                        "color": "#66FF33",
                                        "gravity": "center",
                                        "wrap": True,
                                        "flex": 1
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "NEVERDIE BOT",
                                        "color": "#FFFFFF",
                                        "align": "center"
                                    }
                                ]
                            },
                            "styles": {
                                "header": {
                                    "backgroundColor": "#CC0000"
                                },
                                "footer": {
                                    "backgroundColor": "#CC0000",
                                    "separator": True,
                                    "separatorColor": "#CC0000"
                                },
                                "body": {
                                    "backgroundColor": "#000000"
                                }
                            }
                        }
                    }
                    sendTemplate(to, data) 
#-------------------------------------------------------------------------------------------------------------  
                elif text.lower() == "ออน4":
                    cover = nn1.getProfileCoverURL(nn1.profile.mid)
                    pp = nn1.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = nn1.getProfile().displayName
                    status = nn1.getProfile().statusMessage     
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    van = format(str(runtime))
                    van2 = "\n\n💖วันที่ :"+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n───────────\n◐เวลา:"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n\n"      
                    data={
"type":"flex",
"altText":"Weclome",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#FF6600", "separator": True, "separatorColor": "#FF6600"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "💖 เวลาบอทออนไลน์ 💖",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#66FFFF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#CC0000"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#CC0000"
},
{
"contents": [
{
"text": "💖ระยะเวลาออนของบอท💖",
"size": "md",
"align": "center",
"color": "#66FFFF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#CC0000"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#FFCCFF",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " 🔥 ดัดแปลงโดย : \n 🔥NEVERDIE BOT🔥\n🔥S̷T̷ B̷O̷T̷L̷I̷N̷E̷🔥",
"size": "xs",
"margin": "none",
"color": "#FFCCFF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#FF6600",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อบอท",
"uri": "https://line.me/ti/p/~steveneverdie002",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#FF6600",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "ADD CREATOR",
"uri": "https://line.me/ti/p/~steveneverdie002",
}
}
]
}
},
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#FF6600", "separator": True, "separatorColor": "#FF6600"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "🔥 ปฏิทิน 🔥",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#66FFFF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#CC0000"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#CC0000"
},
{
"contents": [
{
"text": "🔥 วันเดือนปี  เวลา 🔥",
"size": "md",
"align": "center",
"color": "#66FFFF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#CC0000"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van2,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#FFCCFF",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " 🔥ดัดแปลงโดย : \n 🔥NEVERDIE BOT🔥 \n🔥S̷T̷ B̷O̷T̷L̷I̷N̷E̷🔥",
"size": "xs",
"margin": "none",
"color": "#FFCCFF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#FF6600",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อบอท",
"uri": "https://line.me/ti/p/~steveneverdie002",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#FF6600",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "ADD CREATOR",
"uri": "https://line.me/ti/p/~steveneverdie002",
}
}
]
}
}
]
}
}                    
                    sendTemplate(to, data)  
#----------------------------------------------------------------------------------------------#                   
                elif text.lower() == "ออน5" or text.lower() == "runtime5":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "⇨ เวลาออนไลน์บอท ⇦\n"
                    run += runtime
                    data = {
                        "type": "flex",
                        "altText": "{}".format(run),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#CC0000'
                                 },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://sv1.picz.in.th/images/2019/09/05/Znpb5u.jpg",
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [                              
                                    {
                                        "type": "text",
                                        "text": "{}".format(run),
                                        "wrap": True,
                                        "color": "#000000",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)            
#----------------------------------------------------------------------------#                    
                elif cmd.startswith("fx "):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            groups = nn1.getGroupIdsJoined()
                            for gr in groups:                            
                                data = {
                                        "type": "flex",
                                        "altText": "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FF1C"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
            "type": "image"
          },
          {
            "url": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
            "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "contents": [
          {
            "text": "👉ประกาศ👈",
            "size": "lg",
            "align": "center",
            "color": "#CC0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#FF1900"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "{}".format(text),
                "size": "lg",
                "align": "center",
                "margin": "none",
                "color": "#66FFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "สนใจบอทติดต่อ",
                "size": "xl",
                "action": {
                  "uri": "line://ti/p/~"+nn1.getProfile().userid,
                  "type": "uri",
                  "label": "Add Hacker"
                },
                "margin": "xl",
                "align": "center",
                "color": "#FF9900",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                sendTemplate(gr, data)
                                time.sleep(1)     
                            nn1.sendMessage(to, "ส่งคำประกาศจำนวน {} กลุ่ม".format(str(len(groups))))                   
#----------------------------------------------------------------------------#                                
                if text.lower() == "sp" or text.lower() == "speed":
                    s = "#FF6600"
                    a = "#000000"
                    start = time.time()
                   # nn1.sendMessage("u21d04f683a70ee8776c4c58a0358c204","test speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    aa = "ความเร็ว : %.3fms วินาที" % (took)
                    data = {
                        "type": "flex",
                        "altText": "BotSpeed",
                        "contents": {
                            "type": "bubble",
                            'styles': {
                                "body": {
                                    "backgroundColor":a
                                },
                            },
                            "hero": {
                                "type":"image",
                                "url":"https://sv1.picz.in.th/images/2019/09/04/Z6iZ2N.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": aa,
                                        "wrap": True,
                                        "color":s,
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "sm"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                    
                elif text.lower() == "รีบอท" or text.lower() == "reset":
                    nn2(to, "กำลังทำการรีบอทใหม่")
                    nn3(to, "🐱กดลิ้งเพื่อล็อคอินอีกครั้ง🐱")
                    restartBot()
#----------------------------------------------------------------------------------------------------------------------#             
                elif text.lower() == "รีบอท2" or text.lower() == "reset2":
                    gifnya = ["https://sv1.picz.in.th/images/2019/09/05/Zn6vxl.gif"]
                    data = {
                        "type": "template",
                        "altText": "กำลังรีบอท...",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line.me/ti/p/~steveneverdie002"
                                     }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, data)
                    time.sleep(1)
                    ga = "สำเร็จแล้ว (｀・ω・´)"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(ga)),
                        "sentBy": {
                             "label": "รีบอทสำเร็จ...",
                             "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"
                        }
                    }
                    sendTemplate(to, data)
                    restartBot()   
#----------------------------------------------------------------------------#                    
#----------------------------------------------------------------------------#                 
                if text.lower() == "/speed" or text.lower() == "/sp" or text.lower() == "/สปีด":
                    start = time.time()
                    #nn1.sendMessage("u36f6521607e3082d23cb316d185b10bf","speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "ความเร็ว :\n- เชิร์ฟเวอร์ : %.3fms วินาที" % (took)
                    data = {"type": "text","text": "{}".format(a),"sentBy": {"label": "%.10f" % (elapsed_time), "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"}}                  
                    sendTemplate(to,data)
                    
                if text.lower() == "สปีด" or text.lower() == "ความเร็ว":
                    s = temp["te"]
                    a = temp["t"]
                    start = time.time()
                    #nn1.sendMessage("u21d04f683a70ee8776c4c58a0358c204","test speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    aa = "ความเร็ว : %.3fms วินาที" % (took)
                    data = {'type':'flex','altText':"ความเร็วบอท",'contents':{"header":{"contents":[{"text":"เชคความเร็วบอท","type":"text","align":"center","color":s}],"type":"box","layout":"vertical"},"styles":{"header":{"backgroundColor":a,"separator":True,"separatorColor":s},"body":{"backgroundColor":a,"separator":True,"separatorColor":s},"footer":{"backgroundColor":"#000000","separator":True,"separatorColor":s}},"body":{"contents":[{"text":aa,"type":"text","align":"center","color":s}],"type":"box","layout":"vertical"},"hero":{"size":"full","aspectMode":"cover","type":"image","url":"https://sv1.picz.in.th/images/2019/09/04/Z6iXtZ.jpg"},"type":"bubble","footer":{"contents":[{"contents":[{"size":"md","type":"icon","url":"https://sv1.picz.in.th/images/2019/08/08/KIIbGy.jpg"},{"text":"ADD MEE","size":"md","color":"#FF0066","type":"text","action":{"type":"uri","uri":"https://line.me/R/ti/p/~0969245004"},"align":"center"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"sm","layout":"vertical"}}} 
                    sendTemplate(to, data)                
#----------------------------------------------------------------------------#                
                if cmd == "ขายบอท":
                   data = {"type":"flex","altText": "ขายเชลบอทคุณภาพ","contents":{"type":"carousel","contents":[{"type":"bubble","header":{"type":"box","layout":"horizontal","contents":[{"type":"text","action":{"type":"uri","uri":"https://line.me/ti/p/~steveneverdie002"},"text":"™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯","wrap":True,"weight":"bold","align":"center","size":"md","color":"#000000"}]},"hero":{"action":{"uri":"https://line.me/ti/p/~steveneverdie002","type":"uri"},"type":"image","url":"https://i.ibb.co/ns8nR1y/Image-749.jpg","size":"full","aspectMode":"cover"},"styles":{"header":{"backgroundColor":"#CC0000"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#CC0000"}},"body":{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"text","size":"md","text":"🐱Self BOT & Kicker Premium🐱","wrap":True,"weight":"bold","color":"#66FFFF","align":"center"},{"type":"text","text":"บอทป้องกันกลุ่ม","wrap":True,"weight":"bold","align":"center","color":"#66FFFF","size":"lg"},{"type":"text","size":"lg","text":"ระบบเฟกและภาษาไทยทั้งหมด","wrap":True,"weight":"bold","color":"#66FFFF","align":"center"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"ราคาเชลบอทระบบเฟก 100บาท","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"(1เชล/10คิก+1คิกผี)=500บาท","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"(1เชล/20คิก+1คิกผี)=1000บาท","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"เซลบอทกันรันกันแชทร่วมได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"เซลบอทมีระบบลบห้องรันอัติโนมัติ","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","action":{"type":"uri","uri":"https://line.me/ti/p/~steveneverdie002"},"text":"ติดต่อคนขายบอท","wrap":True,"weight":"bold","align":"center","size":"xl","color":"#000000"}]}},{"type":"bubble","header":{"type":"box","layout":"horizontal","contents":[{"type":"text","action":{"type":"uri","uri":"https://line.me/ti/p/~steveneverdie002"},"text":"™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ̶✯","wrap":True,"weight":"bold","align":"center","size":"md","color":"#000000"}]},"hero":{"action":{"uri":"https://line.me/ti/p/~stevenever002","type":"uri"},"type":"image","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png","size":"full","aspectMode":"cover"},"styles":{"header":{"backgroundColor":"#FF0033"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#FF0033"}},"body":{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"text","size":"md","text":"🐱Self BOT & Kicker Premium🐱","wrap":True,"weight":"bold","color":"#CC0000","align":"center"},{"type":"text","text":"บอทป้องกันกลุ่ม","wrap":True,"weight":"bold","align":"center","color":"#FFFFFF","size":"lg"},{"type":"text","size":"lg","text":"ระบบเฟกและภาษาไทยทั้งหมด","wrap":True,"weight":"bold","color":"#66FFFF","align":"center"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"ตั้งข้อความ ต้อนรับ เข้าออกเองได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"ตั้งข้อความเวลาเพื่อนแท็ค เราได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"ตั้งสติกเกอร์ตัวใหญ่ เองได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"ตั้งสีตัวอักษรกับสีใบคำสั่ง เองได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"เช็คดูคนอ่านข้อความได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","action":{"type":"uri","uri":"https://line.me/ti/p/~steveneverdie002"},"text":"ติดต่อคนขายบอท","wrap":True,"weight":"bold","align":"center","size":"xl","color":"#000000"}]}},{"type":"bubble","header":{"type":"box","layout":"horizontal","contents":[{"type":"text","action":{"type":"uri","uri":"https://line.me/ti/p/~steveneverdie002"},"text":"™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ̶✯","wrap":True,"weight":"bold","align":"center","size":"md","color":"#000000"}]},"hero":{"action":{"uri":"https://line.me/ti/p/~steveneverdie002","type":"uri"},"type":"image","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png","size":"full","aspectMode":"cover"},"styles":{"header":{"backgroundColor":"#FF0033"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#FF0033"}},"body":{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"text","size":"md","text":"🐱Self BOT & Kicker Premium🐱","wrap":True,"weight":"bold","color":"#CC0000","align":"center"},{"type":"text","text":"บอทป้องกันกลุ่ม","wrap":True,"weight":"bold","align":"center","color":"#FFFFFF","size":"lg"},{"type":"text","size":"lg","text":" ระบบเฟ็กและภาษาไทยทั้งหมด","wrap":True,"weight":"bold","color":"#66FFFF","align":"center"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"แทคสมาชิกยกห้องได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"ขโมย รูป ดิส ปก ตัส ได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"ดึง คอนแทค จากโพสได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"สามารถCopyบัญชีคนอื่นได้","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","spacing":"xs","layout":"vertical","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"xl","url":"https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png"},{"flex":0,"type":"text","margin":"none","text":"ขายลิ้งบินกลุ่มสามารบินได้500คน","weight":"bold","color":"#66FFFF"}]}]},{"type":"separator","color":"#FFFFFF"}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"text","action":{"type":"uri","uri":"https://line.me/ti/p/~steveneverdie002"},"text":"ติดต่อคนขายบอท","wrap":True,"weight":"bold","align":"center","size":"xl","color":"#000000"}]}}]}}
                   sendTemplate(to, data)
#----------------------------------------------------------------------------#                   
                if text.lower() == "me" or text.lower() == "/me":
                    contact = nn1.getContact(sender)
                    cover = nn1.getProfileCoverURL(nn1.profile.mid)
                    pp = nn1.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = nn1.getProfile().displayName
                    status = nn1.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"carousel","contents":[{"type":"bubble","hero":{"type":"image","url":profile,"margin":"none","align":"center","gravity":"center","size":"full","aspectRatio":"1:1","aspectMode":"cover","backgroundColor":"#FFFFFF","action":{"type":"uri","label":"a","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=apind%20ganteng"}},"body":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"text","text":"รูปโปรไฟล์เรา","margin":"xxl","size":"xl","align":"center","gravity":"center","weight":"bold","color":"#FF0000","action":{"type":"uri","label":"b","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=apind%20ganteng%20banget%20ya"},"wrap":True},{"type":"box","layout":"horizontal","spacing":"xs","flex":2,"contents":[{"type":"image","url":"https://icons.iconarchive.com/icons/pelfusion/long-shadow-media/512/Camera-icon.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/camera/"}},{"type":"image","url":"https://icons.iconarchive.com/icons/blackvariant/button-ui-microsoft-office-apps/1024/Microsoft-Gallery-icon.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/cameraRoll/multi"}},{"type":"image","url":"https://icons.iconarchive.com/icons/designbolts/handstitch-social/256/Share-icon.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/timeline"}},{"type":"image","url":"https://icons.iconarchive.com/icons/simplefly/simple-green-social-media/256/social-media-chat-icon.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/chat"}},{"type":"image","url":"https://icons.iconarchive.com/icons/chrisbanks2/gCons/128/keep-icon.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/keep"}}]}]},"footer":{"type":"box","layout":"vertical","spacing":"none","margin":"none","contents":[{"type":"box","layout":"horizontal","spacing":"none","margin":"none","contents":[{"type":"button","action":{"type":"uri","label":"ข้อมูล1","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=ข้อมูล1"},"color":"#66FF00","margin":"none","height":"sm","style":"primary"},{"type":"button","action":{"type":"uri","label":"คำสั่ง","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=คำสั่ง"},"color":"#66FF00","margin":"none","height":"sm","style":"primary"}]},{"type":"box","layout":"horizontal","spacing":"none","margin":"none","contents":[{"type":"button","action":{"type":"uri","label":"เชคค่า","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=เชคค่า"},"color":"#FF0000","margin":"none","height":"sm","style":"primary","gravity":"top"}]}]},"styles":{"hero":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#000000"}}},{"type":"bubble","hero":{"type":"image","url":cover,"margin":"none","align":"center","gravity":"center","size":"full","aspectRatio":"1:1","aspectMode":"cover","backgroundColor":"#FFFFFF","action":{"type":"uri","label":"KONTOL","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=ปกเรา"}},"body":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"text","text":"รูปปกของเรา","margin":"xxl","size":"xl","align":"center","gravity":"center","weight":"bold","color":"#FF0000","action":{"type":"uri","label":"kotnol","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=apind%20ganteng"},"wrap":True},{"type":"box","layout":"horizontal","spacing":"xs","flex":2,"contents":[{"type":"image","url":"https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/profile-icon.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/profile"}},{"type":"image","url":"https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Actions-contact-new-icon.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/addFriends"}},{"type":"image","url":"https://icon-icons.com/icons2/72/PNG/256/setting_14432.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/settings"}},{"type":"image","url":"https://icons.iconarchive.com/icons/graphicloads/100-flat/256/phone-icon.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://call/contacts"}},{"type":"image","url":"https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/shop-icon.png","aspectMode":"cover","aspectRatio":"1:1","size":"xxs","action":{"type":"uri","uri":"line://nv/stickerShop"}}]}]},"footer":{"type":"box","layout":"vertical","spacing":"none","margin":"none","contents":[{"type":"box","layout":"horizontal","spacing":"none","margin":"none","contents":[{"type":"button","action":{"type":"uri","label":"แทค","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=แทค"},"flex":0,"color":"#66FF00","margin":"none","height":"sm","style":"primary"},{"type":"button","action":{"type":"uri","label":"บ้าน","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=บ้าน"},"flex":2,"color":"#66FF00","margin":"none","height":"sm","style":"primary"}]},{"type":"box","layout":"horizontal","spacing":"none","margin":"none","contents":[{"type":"button","action":{"type":"uri","label":"ข้อมูลกลุ่ม","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=ข้อมูลกลุ่ม"},"color":"#FF0000","margin":"none","height":"sm","style":"primary","gravity":"top"}]}]},"styles":{"hero":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#000000"}}},{"type":"bubble","body":{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"ชื่อเรา","flex":1,"align":"start","gravity":"top","color":"#66FF00","action":{"type":"uri","label":"KONTOL","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=apind%20ganteng"}},{"type":"text","text":name,"flex":3,"align":"start","gravity":"top","color":"#FF0000","action":{"type":"uri","label":"KONTOL","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=apind%20ganteng"},"wrap":False}]},{"type":"box","layout":"baseline","contents":[{"type":"text","text":"สเตตัส","flex":1,"align":"start","gravity":"top","weight":"regular","color":"#66FF00","action":{"type":"uri","label":"kotol","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=apind%20ganteng"},"wrap":True},{"type":"text","text":"{}".format(contact.statusMessage),"flex":3,"weight":"regular","color":"#FF0000","action":{"type":"uri","label":"KONTOL","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=apind%20ganteng"},"wrap":True}]}]},"footer":{"type":"box","layout":"vertical","flex":0,"spacing":"none","margin":"none","contents":[{"type":"box","layout":"horizontal","spacing":"none","margin":"none","contents":[{"type":"button","action":{"type":"uri","label":"เชคกลุ่มค้างเชิญ","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=เชคกลุ่มค้างเชิญ"},"flex":0,"color":"#66FF00","margin":"none","height":"sm","style":"primary"},{"type":"button","action":{"type":"uri","label":"ออน","uri":"line://app/1636367965-3Xqr5zjl?type=text&text=ออน"},"flex":2,"color":"#66FF00","margin":"none","height":"sm","style":"primary"}]},{"type":"box","layout":"vertical","spacing":"none","margin":"none","contents":[{"type":"button","action":{"type":"uri","label":"คนสร้างบอท","uri":"line://ti/p/~0969245004"},"color":"#FF0000","margin":"none","height":"sm","style":"primary","gravity":"center"}]}]},"styles":{"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#000000"}}}]}
                    data = {'type': 'flex','altText': '™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯','contents': data}
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#                    
                if text.lower() == "me1" or text.lower() == "/me":
                    cover = nn1.getProfileCoverURL(nn1.profile.mid)
                    pp = nn1.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = nn1.getProfile().displayName
                    status = nn1.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={'type':'flex','altText':"คนหล่อ",'contents':{"type":"carousel","contents":[{"hero":{"type":"image","action":{"type":"uri","uri":"line://app/1643557392-pe8AQomG?type=profile"},"url":profile,"size":"full","aspectMode":"cover","aspectRatio":"1:1"},"styles":{"body":{"backgroundColor":"#1C1C1C"},"header":{"backgroundColor":"#1C1C1C"}},"type":"bubble","body":{"type":"box","layout":"vertical","spacing":"xs","contents":[{"type":"box","margin":"md","layout":"baseline","contents":[{"type":"icon","size":"sm","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"type":"icon","size":"sm","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"type":"icon","size":"sm","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"type":"icon","size":"sm","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"type":"icon","size":"sm","url":"https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"},{"type":"text","size":"xxs","align":"end","color":"#F8F8FF","text":"™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯"}]},{"type":"box","layout":"vertical","spacing":"xs","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"image","size":"xxs","action":{"type":"uri","uri":"https://line.me/ti/p/~steveneverdie002"},"url":"https://i.ibb.co/Gpd4gYq/CC-20190226-120445.png"},{"type":"image","size":"xxs","action":{"type":"uri","uri":"line://app/1643727178-0XPGAaRX?type=text&text=คำสั่ง"},"url":"https://i.ibb.co/TLMzHYM/CC-20190226-120353.png"},{"type":"image","size":"xxs","action":{"type":"uri","uri":"line://app/1643727178-0XPGAaRX?type=text&text=ข้อมูล1"},"url":"https://i.ibb.co/b1Rgjgf/CC-20190226-120232.png"},{"type":"image","size":"xxs","action":{"type":"uri","uri":"line://app/1643727178-0XPGAaRX?type=text&text=เชคค่า"},"url":"https://i.ibb.co/R3zr1X0/CC-20190226-121428.png"}],"flex":1},{"type":"box","layout":"horizontal","spacing":"xxl","contents":[{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ติดต่อคนสร้างบอท"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"คำสั่ง"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ข้อมูล1"},{"type":"text","size":"xs","color":"#00FF00","text":"เชคค่า"}]}]}]}},{"type":"bubble","styles":{"body":{"backgroundColor":"#1C1C1C"},"header":{"backgroundColor":"#1C1C1C"}},"body":{"type":"box","layout":"vertical","spacing":"xs","contents":[{"type":"box","layout":"baseline","contents":[{"type":"icon","size":"md","url":"https://data.boteater.co/storage-Screenshot_20190228-084051_GalleryHtf5msTA.jpg"},{"type":"icon","size":"md","url":"https://i.ibb.co/Scv2SyN/battery-Phones.png"},{"type":"text","size":"xxs","color":"#66FF66","flex":0,"text":"  ᴬᴵˢ 4G"},{"type":"text","size":"xxs","color":"#66FF66","align":"end","text":"⏰ 22/10/19 ™"}]},{"type":"box","layout":"vertical","spacing":"xs","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1643557392-pe8AQomG?type=text&text=about"},"url":"https://data.boteater.co/storage-Screenshot_20190228-083531_GalleryHtf5msTA.jpg"},{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1609524990-mpvZ5xv5"},"url":"https://data.boteater.co/storage-Screenshot_20190228-084421_GalleryHtf5msTA.jpg"},{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1623679774-lGOq9q3G"},"url":"https://data.boteater.co/storage-Screenshot_20190228-083746_GalleryHtf5msTA.jpg"}],"flex":1},{"type":"box","layout":"horizontal","spacing":"xxl","contents":[{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ᵃᵇᵒᵘᵗ"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ᶠᵃᶜᵉᵇᵒᵒᵏ"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ᵐᵉᵈⁱᵃ"}]}]},{"type":"box","layout":"vertical","spacing":"xs","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1623679774-pXJyQy1D"},"url":"https://data.boteater.co/storage-Screenshot_20190228-084242_GalleryHtf5msTA.jpg"},{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1643557392-pe8AQomG?type=profile"},"url":"https://data.boteater.co/storage-Screenshot_20190228-084313_GalleryHtf5msTA.jpg"},{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1623679774-YvdwxwV3"},"url":"https://data.boteater.co/storage-Screenshot_20190228-083254_GalleryHtf5msTA.jpg"}],"flex":1},{"type":"box","layout":"horizontal","spacing":"xxl","contents":[{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ⁿᵒᵗᵉ\xa0ᵖᵃᵈ"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ˡⁱⁿᵉ"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ᵏᵃˡᵉⁿᵈᵉʳ"}]}]},{"type":"box","layout":"vertical","spacing":"xs","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1623679774-3vDKkKaP"},"url":"https://data.boteater.co/storage-Screenshot_20190228-083057_GalleryHtf5msTA.jpg"},{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1623679774-z6dOvOV9"},"url":"https://data.boteater.co/storage-Screenshot_20190226-093402_Galleryj97NY7GF.jpg"},{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1609524990-ODaJ0Va0"},"url":"https://data.boteater.co/storage-Screenshot_20190228-125713_GalleryNOfnAwaS.jpg"}],"flex":1},{"type":"box","layout":"horizontal","spacing":"xxl","contents":[{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ᵍᵒᵒᵍˡᵉ"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ʲᵒᵒˣ"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ᵍᵃᵐᵉ\xa0ᵒⁿˡⁱⁿᵉ"}]}]},{"type":"box","layout":"vertical","spacing":"xs","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1623679774-qmmXPXJ5"},"url":"https://data.boteater.co/storage-Screenshot_20190228-122858_GallerylK1AJizc.jpg"},{"type":"image","size":"xs","action":{"type":"uri","uri":"line://app/1609524990-pdlOGglG"},"url":"https://data.boteater.co/storage-Screenshot_20190228-083918_GalleryHtf5msTA.jpg"},{"type":"image","size":"xs","action":{"type":"uri","uri":"https://www.youtube.com/user/WorkpointOfficial"},"url":"https://data.boteater.co/storage-Screenshot_20190228-082538_GalleryHtf5msTA.jpg"}],"flex":1},{"type":"box","layout":"horizontal","spacing":"xxl","contents":[{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ᵖˡᵃʸ\xa0ˢᵗᵒʳᵉ"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ᵗᵉˣᵗ\xa0ⁿᵉᵒ"},{"type":"text","size":"xs","align":"center","color":"#00FF00","text":"ʸᵒᵘᵗᵘᵇᵉ"}]},{"type":"box","layout":"horizontal","spacing":"md","contents":[{"type":"text","text":"- - -","align":"center","size":"xs","weight":"bold","color":"#F8F8FF","wrap":True}]}]}]}}]}}
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#                    
                if text.lower() == "me2":
                    contact = nn1.getContact(sender)
                    cover = nn1.getProfileCoverURL(nn1.profile.mid)
                    pp = nn1.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = nn1.getProfile().displayName
                    status = nn1.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText": "คนหน้ารัก","contents":{"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#FF00FF","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://app/1644000112-l90ORBeK"},"type":"text","text":"ลิ้งลบรัน","align":"center","weight":"bold"},{"type":"separator","color":"#ff00ff"},{"color":"#ff00ff","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://app/1636169025-yQ7bGMVA?type=profile"},"type":"text","text":"คนสร้างบอท","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":a}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":s},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://i.pinimg.com/originals/b3/b4/c1/b3b4c14cbd4fe22986ae699c4403695a.gif"},{"type":"separator","color":s},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://i.ibb.co/GdwQtdS/Screenshot-2018-1215-233501.png"},{"type":"separator","color":s},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://media.giphy.com/media/qqWB4u3mrTlrG/giphy.gif"},{"type":"separator","color":s},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://i.pinimg.com/originals/a6/94/ec/a694ec9773292abec803f07befd73e74.gif"},{"type":"separator","color":s}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":s},{"type":"box","contents":[{"type":"separator","color":s},{"color":"#FF0033","size":"md","wrap":True,"type":"text","text":"™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ̶✯","weight":"bold"},{"type":"separator","color":s},{"color":s,"size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":s},{"color":"#FF0033","size":"xs","wrap":True,"type":"text","text":"สเตตัส","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":s}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"full","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}}
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#                    
                if text.lower() == "me3":
                    contact = nn1.getContact(sender)
                    name = nn1.getProfile().displayName
                    status = nn1.getProfile().statusMessage
                    cover = nn1.getProfileCoverURL(nn1.profile.mid)
                    pp = nn1.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText": "™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯","contents":{"contents":[{"hero":{"aspectMode":"cover","url":profile,"action":{"uri":"http://line.me/ti/p/~steveneverdie002","type":"uri"},"type":"image","size":"full"},"styles":{"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#FF0000"},"header":{"backgroundColor":"#FF0000"}},"type":"bubble","footer":{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"button","flex":2,"style":"primary","color":"#0000FF","height":"sm","action":{"type":"uri","label":"คนสร้าง","uri":"line://app/1644000112-l90ORBeK"}},{"flex":3,"type":"button","style":"primary","color":"#0000FF","margin":"sm","height":"sm","action":{"type":"uri","label":"กดสิ","uri":"line://app/1636169025-yQ7bGMVA?type=profile"}}]}]},"header":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"รูปโปรไฟลเรา","size":"xl","wrap":True,"weight":"bold","color":"#66FF00","align":"center"}]}},{"hero":{"aspectMode":"cover","url":cover,"action":{"uri":"http://line.me/ti/p/~0969245004","type":"uri"},"type":"image","size":"full"},"styles":{"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#FF0000"},"header":{"backgroundColor":"#FF0000"}},"type":"bubble","footer":{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"button","flex":2,"style":"primary","color":"#0000FF","height":"sm","action":{"type":"uri","label":"คนสร้าง","uri":"line://app/1644000112-l90ORBeK"}},{"flex":3,"type":"button","style":"primary","color":"#0000FF","margin":"sm","height":"sm","action":{"type":"uri","label":"กดสิ","uri":"line://app/1636169025-yQ7bGMVA?type=profile"}}]}]},"header":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"ปกเรา","size":"xl","wrap":True,"weight":"bold","color":"#66FF00","align":"center"}]}},{"styles":{"body":{"backgroundColor":a},"footer":{"backgroundColor":"#FF0000"},"header":{"backgroundColor":"#FF0000"}},"type":"bubble","body":{"contents":[{"contents":[{"contents":[{"type":"text","text":name,"size":"xl","wrap":True,"weight":"bold","color":s,"align":"center"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"type":"separator","color":"#FF0000"},{"contents":[{"contents":[{"type":"text","text":"{}".format(contact.statusMessage),"size":"md","wrap":True,"weight":"bold","color":s,"align":"center"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"},{"type":"separator","color":"#FF0000"},{"contents":[{"contents":[{"type":"text","text":" ..","size":"xs","wrap":True,"weight":"bold","color":"#F0FFFF","align":"center"}],"type":"box","layout":"baseline"}],"type":"box","spacing":"xs","layout":"vertical"}],"type":"box","spacing":"xs","layout":"vertical"},"footer":{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"button","flex":2,"style":"primary","color":"#0000FF","height":"sm","action":{"type":"uri","label":"คนสร้าง","uri":"line://app/1644000112-l90ORBeK"}},{"flex":3,"type":"button","style":"primary","color":"#0000FF","margin":"sm","height":"sm","action":{"type":"uri","label":"กดสิ","uri":"line://app/1636169025-yQ7bGMVA?type=profile"}}]}]},"header":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"สเตตัสของเรา","size":"xl","wrap":True,"weight":"bold","color":"#66FF00","align":"center"}]}}],"type":"carousel"}}
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#                    
                if text.lower() == "me4":
                    contact = nn1.getContact(sender)
                    cover = nn1.getProfileCoverURL(nn1.profile.mid)
                    pp = nn1.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = nn1.getProfile().displayName
                    status = nn1.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText": "{} เกี่ยวกับ".format(name),"contents":{"type":"carousel","contents":[{"type":"bubble","hero":{"type":"image","url":cover,"size":"full","aspectRatio":"2:1","aspectMode":"cover","backgroundColor":a},"body":{"type":"box","layout":"vertical","contents":[{"type":"image","url":profile,"align":"center","size":"sm","aspectRatio":"1:1"},{"type":"text","text":name,"color":"#66FF00","size":"xxl","margin":"xl","weight":"bold","wrap":True},{"type":"text","text":status,"color":s,"wrap":True}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"separator","color":"#66FF00"},{"type":"button","style":"link","color":s,"action":{"type":"uri","label":"ติดต่อ","uri":"https://line.me/ti/p/~steveneverdie002"}}]}},{"type":"bubble","hero":{"type":"image","url":"https://noxt.cf/files/cyde-facebook.png","size":"full","aspectRatio":"2:1","backgroundColor":a},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"Facebook","color":"#314e97","size":"xxl","weight":"bold","wrap":True}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"separator","color":"#314e97"},{"type":"button","style":"link","color":"#314e97","action":{"type":"uri","label":"โปรไฟล์ของฉัน","uri":"https://www.facebook.com/folk.noxt"}}]}},{"type":"bubble","hero":{"type":"image","url":"https://noxt.cf/files/cyde-youtube.png","size":"full","aspectRatio":"2:1","backgroundColor":"#fe0000"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"YouTube","color":"#fe0000","size":"xxl","weight":"bold","wrap":True}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"separator","color":"#fe0000"},{"type":"button","style":"link","color":"#fe0000","action":{"type":"uri","label":"ช่องของฉัน","uri":"https://www.youtube.com/channel/UCvsje3-C2JqUzgyujUTxcQQ"}},{"type":"button","style":"link","color":"#fe0000","action":{"type":"uri","label":"วีดีโอของฉัน","uri":"https://www.youtube.com/channel/UCvsje3-C2JqUzgyujUTxcQQ/videos"}}]}},{"type":"bubble","hero":{"type":"image","url":"https://noxt.cf/files/cyde-github.png","size":"full","aspectRatio":"2:1","backgroundColor":"#24292e"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"GitHub","color":"#24292e","size":"xxl","weight":"bold","wrap":True}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"separator","color":"#24292e"},{"type":"button","style":"link","color":"#24292e","action":{"type":"uri","label":"โปรไฟล์ของฉัน","uri":"https://github.com/Noxturnix"}},{"type":"button","style":"link","color":"#24292e","action":{"type":"uri","label":"Repo ของฉัน","uri":"https://github.com/Noxturnix?tab=repositories"}}]}},{"type":"bubble","hero":{"type":"image","url":"https://noxt.cf/files/cyde-website.png","size":"full","aspectRatio":"2:1","backgroundColor":"#808080"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"Website","color":"#808080","size":"xxl","weight":"bold","wrap":True}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"separator","color":"#808080"},{"type":"button","style":"link","color":"#808080","action":{"type":"uri","label":"เว็บไซต์ของฉัน","uri":"https://graybox.inth.red/"}}]}}]}}
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#                    
                if text.lower() == "ลิ้งรัน":
                    contact = nn1.getContact(sender)
                    cover = nn1.getProfileCoverURL(nn1.profile.mid)
                    pp = nn1.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = nn1.getProfile().displayName
                    status = nn1.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={'type':'flex','altText':"แจกลิ้งบอท",'contents':{"type":"bubble","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯","weight":"bold","color":"#CC0000","align":"center"}]},"body":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ลิ้งลบรัน","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://i.pinimg.com/originals/22/1d/bd/221dbd55353c0a5e70d8dbf97353b913.gif"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ลิ้งบินกลุ่ม","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://i.pinimg.com/originals/1e/d1/24/1ed12497c6e2a85faba0dcc650ccc211.gif"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ลิ้งรันกลุ่ม","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://i.pinimg.com/originals/ec/2a/35/ec2a3559d975a9b124e22f6c78ef4fb6.gif"}},{"type":"button","style":"primary","color":"#FF6600","action":{"type":"uri","label":"ลิ้งเชลบอทฟรี","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://i.pinimg.com/originals/9d/c3/a8/9dc3a875b6be5af567f6213a3d388843.gif"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"ต้องการลิ้งอะไรสามารกดที่ปุ่มได้เลย","color":"#CC0000","align":"center"}]},"styles":{"header":{"backgroundColor":"#000000","separator":True,"separatorColor":"#000000"},"hero":{"separator":True,"separatorColor":"#000000"},"footer":{"backgroundColor":"#000000","separator":True,"separatorColor":s},"body":{"separator":True,"separatorColor":s,"backgroundColor":a}}}}
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#                                
                elif cmd == "เวลา":
                    s = temp["te"]
                    a = temp["t"]
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "" + hasil + "\nที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    data = {
                            "type": "flex",
                            "altText": "เวลา",
                                "contents": {
                                "styles": {
                                "body": {
                                "backgroundColor":a
                                },
                                "footer": {
                                  "backgroundColor":"#000000"
                                }
                                },
                                    "type": "bubble",
                                        "hero": {
                                            "type": "image",
                                            "url": "https://sv1.picz.in.th/images/2019/09/03/ZCHw5g.png",
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "text":  "{}".format(readTime),
                                        "size": "xl",
                                        "align": "center",
                                        "color":s,
                                        "wrap": True,
                                        "weight": "bold",
                                        "type": "text"
                                    }
                                ]
                            },                                        
                                "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "button",
                                        "style": "link",
                                        "height": "sm",
                                        "action": {
                                            "type": "uri",
                                            "label": "ADD ME",
                                            "uri": "https://line.me/ti/p/~" + nn1.profile.userid
                                        }
                                },
                                {
                                    "type": "spacer",
                                    "size": "sm",
                                }
                            ],
                            "flex": 0
                            }
                        }
                    }                                        
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#                    
                elif cmd == "tag":
                  if msg.toType == 2:
                    group = nn1.getGroup(to)
                    ret_ = "╭━━━══[ สมาชิกในกลุ่ม ]"
                    no = 0 + 1
                    for mem in group.members:
                      ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                      no += 1
                    ret_ += "\n╰━━━══[ จำนวน {} คน]".format(str(len(group.members)))
                    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                    warnanya1 = random.choice(warna1)
                    data = {
                        "type": "flex",
                        "altText": "{} membagikan aplikasi".format(nn1.getProfile().displayName),
                        "contents": {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": str(ret_),
                                        "wrap": True,
                                        "color": warnanya1,
                                        "align": "center"
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [{
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "uri",
                                        "label": "ADD ME",
                                        "uri": "https://line.me/ti/p/~" + nn1.profile.userid
                                        }													
                                    },
                                {   
                                    "type": "spacer",
                                    "size": "sm",
                                }],
                                "flex": 0
                            }
                        }
                    }
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#                    
                elif cmd == "ข้อมูล":
                        s = "#66FF00"
                        a = "#000000"
                        contact = nn1.getContact(nn1MID)
                        contacts = nn1.getAllContactIds()
                        groups = nn1.getGroupIdsJoined()
                        suplist = []
                        lists = []
                        tz = pytz.timezone("Asia/Makassar")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        timeNoww = time.time()
                        runtime = timeNoww - Start
                        runtime = format_timespan(runtime)
                        blockedlist = nn1.getBlockedContactIds()
                        blockeds = nn1.getContacts(blockedlist)
                        cu = nn1.getProfileCoverURL( nn1MID)
                        image = str(cu)
                        for i in range(len(day)):
                           if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                           if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n│ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        data = {
                                "type": "flex",
                                "altText": "ข้อมูลเรา",
                                    "contents": {
                                    "styles": {
                                    "body": {
                                    "backgroundColor":a
                                    },
                                    "footer": {
                                      "backgroundColor": "#000000"
                                    }
                                    },
                                        "type": "bubble",
                                        "hero": {
                                            "type": "image",
                                            "url": image,
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                        },                                        
                                        "body": {
                                        "contents": [
                                          {
                                            "contents": [
                                              {
                                        "url": "https://obs.line-scdn.net/{}".format(nn1.getContact( nn1MID).pictureStatus),
                                        "type": "image"
                                              },
                                            ],
                                            "type": "box",
                                            "spacing": "sm",
                                            "layout": "vertical"
                                          },
                                          {
                                            "type": "separator",
                                            "color":s
                                          },
                                          {
                                            "contents": [
                                              {
                                        "text": "ข้อมูลเรา",
                                        "size": "xxl",
                                        "align": "center",
                                        "color": s,
                                        "wrap": True,
                                        "weight": "bold",
                                        "type": "text"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "sm",
                                            "layout": "vertical"
                                          },
                                          {
                                            "type": "separator",
                                            "color":"#6F4E37"
                                          },
                                          {
                                            "contents": [
                                              {
                                        "contents": [
                                          {
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "type": "icon",
                                            "size": "lg"
                                          },
                                          {
                                            "text": "ชื่อ: {}".format(nn1.getProfile().displayName),
                                            "size": "lg",
                                            "margin": "none",
                                            "color":s,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                              },
                                              {
                                        "type": "separator",
                                        "color": "#6F4E37"
                                              },
                                              {
                                        "contents": [
                                          {
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "type": "icon",
                                            "size": "lg"
                                          },
                                          {
                                            "text": "「ออน」 : {}".format(str(runtime)),
                                            "size": "lg",
                                            "margin": "none",
                                            "color": s,
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                              },
                                              {
                                        "contents": [
                                          {
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "type": "icon",
                                            "size": "lg"
                                          },
                                          {
                                            "text": "「เพื่อนเรา」 : {}".format(str(len(contacts))),
                                            "size": "lg",
                                            "margin": "none",
                                            "color":s,
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                              },
                                              {
                                        "contents": [
                                          {
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "type": "icon",
                                            "size": "lg"
                                          },
                                          {
                                            "text": "「กลุ่มเรา」 : {}".format(str(len(groups))),
                                            "size": "lg",
                                            "margin": "none",
                                            "color":s,
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                              },
                                              {
                                        "contents": [
                                          {
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "type": "icon",
                                            "size": "lg"
                                          },
                                          {
                                            "text": "「คนที่เราบล็อค」 : {}".format(str(len(blockeds))),
                                            "size": "lg",
                                            "margin": "none",
                                            "color":s,
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                              },
                                              {
                                        "contents": [
                                          {
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "type": "icon",
                                            "size": "lg"
                                          },
                                          {
                                            "text": "「เวอร์ชั่น」 : NN1",
                                            "size": "lg",
                                            "margin": "none",
                                            "color":s,
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                              },
                                              {
                                        "contents": [
                                          {
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "type": "icon",
                                            "size": "lg"
                                          },
                                          {
                                            "text": "「ทีมบอท」 :™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯",
                                            "size": "lg",
                                            "margin": "none",
                                            "color":s,
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                              }
                                            ],          
                                            "type": "box",
                                            "layout": "vertical"
                                          }
                                        ],
                                        "type": "box",
                                        "spacing": "md",
                                        "layout": "vertical"
                                    },
                                        "footer": {
                                        "contents": [
                                          {
                                            "contents": [
                                              {
                                        "contents": [
                                          {
                                            "text": "「ติดต่อ」",
                                            "size": "lg",
                                            "action": {
                                              "uri": "https://line.me/ti/p/~" + nn1.profile.userid,
                                              "type": "uri",
                                              "label": "ติดต่อผู้สร้าง"
                                            },
                                            "margin": "lg",
                                            "align": "start",
                                            "color": "#F5F5DC",
                                            "weight": "bold",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                              }
                                            ],
                                            "type": "box",
                                            "layout": "horizontal"
                                          },
                                          {
                                            "type": "separator",
                                            "color": "#6F4E37"
                                          },
                                          {
                                            "contents": [
                                              {
                                        "contents": [
                                          {
                                            "text": "ADD ME",
                                            "size": "lg",
                                            "action": {
                                              "uri": "https://line.me/ti/p/~" + nn1.profile.userid,
                                              "type": "uri",
                                              "label": " 「Open Order」"
                                            },
                                            "margin": "lg",
                                            "align": "start",
                                            "color": "#F5F5DC",
                                            "weight": "bold",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                              }
                                            ],
                                            "type": "box",
                                            "layout": "horizontal"
                                        }
                                    ],
                                    "type": "box",
                                    "layout": "vertical"
                                }
                            }
                        }
                        sendTemplate(to, data) 
#----------------------------------------------------------------------------#                        
                elif cmd == "ข้อมูลเรา1":
                        s = temp["te"]
                        a = temp["t"]
                        cover = nn1.getProfileCoverURL(nn1MID)
                        contact = nn1.getContact(nn1MID)
                        contacts = nn1.getAllContactIds()
                        name = nn1.getProfile().displayName
                        groups = nn1.getGroupIdsJoined()
                        suplist = []
                        lists = []
                        tz = pytz.timezone("Asia/Makassar")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        timeNoww = time.time()
                        runtime = timeNoww - Start
                        runtime = format_timespan(runtime)
                        blockedlist = nn1.getBlockedContactIds()
                        blockeds = nn1.getContacts(blockedlist)
                        cu = nn1.getProfileCoverURL( nn1MID)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = "" + hasil + "ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        data = {'type':'flex','altText':"about me",'contents':{"styles":{"body":{"backgroundColor":a},"footer":{"backgroundColor":s},"header":{"backgroundColor":s}},"type":"bubble","body":{"contents":[{"contents":[{"url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"type":"image"},{"type":"separator","color":"#800080"},{"text":"ข้อมูลผู้ใช้\nNN1\n","size":"md","color":s,"wrap":True,"weight":"bold","type":"text"}],"type":"box","spacing":"md","layout":"horizontal"},{"type":"separator","color":"#800080"},{"contents":[{"text":"ข้อมูลเรา","size":"xl","align":"center","color":s,"wrap":True,"weight":"bold","type":"text"}],"type":"box","spacing":"md","layout":"vertical"},{"type":"separator","color":"#800080"},{"contents":[{"contents":[{"url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"type":"icon","size":"md"},{"text":"ชื่อผู้ใช้ : {}".format(nn1.getProfile().displayName),"size":"md","margin":"none","color":s,"weight":"bold","type":"text"}],"type":"box","layout":"baseline"},{"type":"separator","color":"#800080"},{"contents":[{"url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"type":"icon","size":"md"},{"text":"「ออน」 : {}".format(str(runtime)),"size":"xs","margin":"none","color":s,"wrap":True,"weight":"regular","type":"text"}],"type":"box","layout":"baseline"},{"contents":[{"url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"type":"icon","size":"md"},{"text":"「เพื่อนเรา」 : {}".format(str(len(contacts))),"size":"xs","margin":"none","color":s,"wrap":True,"weight":"regular","type":"text"}],"type":"box","layout":"baseline"},{"contents":[{"url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"type":"icon","size":"md"},{"text":"「กลุ่มเรา」 : {}".format(str(len(groups))),"size":"xs","margin":"none","color":s,"wrap":True,"weight":"regular","type":"text"}],"type":"box","layout":"baseline"},{"contents":[{"url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"type":"icon","size":"md"},{"text":"「คนที่เราบล็อค」 : {}".format(str(len(blockeds))),"size":"xs","margin":"none","color":s,"wrap":True,"weight":"regular","type":"text"}],"type":"box","layout":"baseline"},{"contents":[{"url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"type":"icon","size":"md"},{"text":"「เวอร์ชั่น」 : NN1","size":"xs","margin":"none","color":s,"wrap":True,"weight":"regular","type":"text"}],"type":"box","layout":"baseline"},{"contents":[{"url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),"type":"icon","size":"md"},{"text":"{}".format(readTime),"size":"xs","margin":"none","color":s,"wrap":True,"weight":"regular","type":"text"}],"type":"box","layout":"baseline"}],"type":"box","layout":"vertical"}],"type":"box","spacing":"md","layout":"vertical"},"footer":{"type":"box","layout":"vertical","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"button","flex":2,"style":"primary","color":"#0000FF","height":"sm","action":{"type":"uri","label":"™T̶e̶a̶m̶b̶o̶t̶ ̶a̶v̶e̶n̶g̶e̶r̶s̶✯͜͡❂➣","uri":"https://line.me/ti/p/~0969245004"}}]}]},"header":{"contents":[{"contents":[{"contents":[{"text":"™T̶e̶a̶m̶b̶o̶t̶ ̶a̶v̶e̶n̶g̶e̶r̶s̶✯","size":"xl","weight":"bold","align":"center","color":"#FF0000","type":"text"}],"type":"box","layout":"baseline"}],"type":"box","layout":"horizontal"}],"type":"box","layout":"vertical"}}}   
                        sendTemplate(to, data)        
#----------------------------------------------------------------------------#                    
                elif text.lower() == "หลุดมือ":
                            gifnya = ['https://i.pinimg.com/originals/87/a8/9b/87a89b5aeaf35ba0c8879db5a136ccbd.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/~steveneverdie002"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                            
                elif "เชคกลุ่ม " in text.lower():
                       if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                G = nn1.getGroupIdsJoined()
                                cgroup = nn1.getGroups(G)
                                ngroup = ""
                                for mention in mentionees:
                                  for x in range(len(cgroup)):
                                    gMembMids = [contact.mid for contact in cgroup[x].members]
                                    if mention['M'] in gMembMids:
                                        ngroup += "\n🐱➣ " + cgroup[x].name + " | สมาชิก: " + str(len(cgroup[x].members))    
                                if ngroup == "":
                                      nn2(to, "ไม่พบ")
                                else:
                                    nn2(to, "🐱➣ตรวจพบออยู่ในกลุ่มด้วยกัน\n %s"%(ngroup))
                                    
                elif text.lower() == "ยิงๆ" or text.lower() == "ยิง":
                            gifnya = ['https://i.pinimg.com/originals/25/bf/35/25bf35850f22b00ff04505f173e16ec8.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/~steveneverdie002"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                            
                elif msg.text.lower().startswith("ขอรูป "):
                    try:
                        chivareeZ = text.replace("ขอรูป ","")
                        chivareeX = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(chivareeZ))
                        chivareeA = chivareeX.text
                        chivareeA = json.loads(chivareeA)
                        if chivareeA["content"] != []:
                            chivareeS = chivareeA["content"]
                            chivaree2 = random.choice(chivareeS)
                            ajang1 = chivareeS.index(chivaree2)
                            ajang2 = len(chivareeS)
                            nn1.sendMessage(msg.to,"🐱รอสักครู่ค่ะ 🕚 " +datetime.today().strftime('%H:%M:%S')+ "🐱")
                            nn1.sendImageWithURL(to, str(chivaree2))
                    except Exception as error:
                         logError(error)
                         var= traceback.print_tb(error.__traceback__)
                         nn1.sendMessage(to,str(var))
#----------------------------------------------------------------------------#                         
                if  text.lower().startswith("ตั้งรูปโปรไฟล์ "):
                    keyword = msg.text.replace(msg.text.split(" ")[0] + " ", "")
                    pic = "http://dl.profile.line-cdn.net/{}".format(nn1.profile.pictureStatus)
                    a = subprocess.getoutput('youtube-dl --format mp4 --output tmp.mp4 {}'.format(keyword))
                    pict = nn1.downloadFileURL(pic)
                    vids = "tmp.mp4"
                    changeVideoAndPictureProfile(pict, vids)
                    os.remove("tmp.mp4")
                    nn3(to, "เปลี่ยน Profile เป็น คลิป YouTube เรียบร้อย")
#=====================================================================
#=====================================================================
                elif msg.text.lower().startswith("ดำ "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        apalo["Talkblacklist"][ls] = True
                                        nn2(to, '🐱 เพิ่มลงในบัญชีดำเรียบร้อย 🐱')
                                    except:
                                        pass
                elif msg.text.lower().startswith("ล้าง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del apalo["Talkblacklist"][ls]
                                        nn2(to, '🐱 ลบออกจากบัญชีดำเรียบร้อย 🐱')
                                    except:
                                        pass
                elif text.lower() == "เชคดำ":
                            if apalo["Talkblacklist"] == {}:
                              nn2(to,"🐱 ไม่พบควายที่เรายัดดำ 🐱")
                            else:
                              ma = ""
                              a = 0
                              for m_id in apalo["Talkblacklist"]:
                                  a = a + 1
                                  end = '\n'
                                  ma += str(a) + ". " +nn1.getContact(m_id).displayName + "\n"
                              nn2(to,"🐱 รายชื่อคนติดดำ 🐱\n\n"+ma+"\nจำนวน %s คนติดดำ" %(str(len(apalo["Talkblacklist"]))))
#=====================================================================                
                if text.lower() == "เปิดบล็อค":
                  if msg._from in admin:
                      autobl["autoblock"] = True
                      autobl["autoaddf"] = True
                      sa = "🐱 ระบบบล็อค2ชั้น ทำงาน 🐱"
                  else:
                      sa = "🐱 ระบบบล็อค2ชั้น ทำงาน 🐱"
                  nn2(to, sa)                  
                if text.lower() == "ปิดบล็อค":
                  if msg._from in admin:
                      autobl["autoblock"] = False
                      autobl["autoaddf"] = False
                      nn2(to,"🐱 ปิดออโต้บล็อคแล้ว 🐱")
                  else:
                      nn2(to,"ปิดอยู่แล้ว (｀・ω・´)")
                if text.lower() == "เปิดแทค":
                    tagadd["tags"] = True
                    sa = "🐱 เปิดแล้วว 🐱"
                    nn2(to,str(sa))
                if text.lower() == "ปิดแทค":
                    tagadd["tags"] = False
                    sa = "🐱 ปิดแล้ว 🐱"
                    nn2(to,str(sa))
                if text.lower() == "เปิดกันรัน":
                    autorejit["autoCancel"]["on"] = True
                    nn2(to,"🌠 เปิดแล้ว 🌠")
                if text.lower() == "ปิดกันรัน":
                    autorejit["autoCancel"]["on"] = False
                    nn2(to,"🌠 ปิดแล้ว 🌠")
                if text.lower() == "เปิดแอร์":
                    autobl["autoblock"] = True
                    nn2(to,"🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดแอร์":
                    autobl["autoblock"] = False
                    nn2(to,"🐱 ปิดแล้ว 🐱")
                if text.lower() == "เปิดไลค์":
                    autolike["autolike"] = True
                    nn2(to,"🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดไลค์":
                    autolike["autolike"] = False
                    nn2(to,"🐱 ปิดแล้ว 🐱")
                if text.lower() == "เปิดแทคเตะ":
                    tagadd["tagkick"] = True
                    nn2(to, "🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดแทคเตะ":
                    tagadd["tagkick"] = False
                    nn2(to, "🐱 ปิดแล้ว 🐱")                  
                if text.lower() == "เปิดคอมเม้น":
                    commant["com"] = True
                    nn2(to,"🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดคอมเม้น":
                    commant["com"] = False
                    nn2(to, "🐱 ปิดแล้ว 🐱")  
                if text.lower() == "เปิดต้อนรับ":
                    welcomes["Welcome"] = True
                    nn2(to, "🐱เปิดแล้ว >_<🐱")
                if text.lower() == "ปิดต้อนรับ":
                    welcomes["Welcome"] = False
                    nn2(to,"🐱ปิดแล้ว >_<🐱")                                                     
                if text.lower() == "เปิดต้อนรับ2":
                    welcomes["Wc"] = True
                    nn2(to,"🐱เปิดแล้ว >_<🐱")
                if text.lower() == "ปิดต้อนรับ2":
                    welcomes["Wc"] = False
                    nn2(to,"🐱ปิดแล้ว >_<🐱")
                if text.lower() == "เปิดคนออก":
                    welcomes["Leave"] = True
                    nn2(to,"🐱เปิดแล้ว >_<🐱")
                if text.lower() == "ปิดคนออก":
                    welcomes["Leave"] = False
                    nn2(to,"🐱ปิดแล้ว >_<🐱")                   
                if text.lower() == "เปิดติ๊กคนออก":
                    welcomes["lv"] = True
                    nn2(to,"🐱เปิดแล้ว >_<🐱")
                if text.lower() == "ปิดติ๊กคนออก":
                    welcomes["lv"] = False
                    nn2(to,"🐱ปิดแล้ว >_<🐱")
                if text.lower() == "เปิดติ๊กคนเข้า":
                    welcomes["wcsti2"] = True
                    nn2(to,"🐱เปิดแล้ว >_<🐱")
                if text.lower() == "ปิดติ๊กคนเข้า":
                    welcomes["wcsti2"] = False
                    nn2(to,"🐱ปิดแล้ว >_<🐱")                    
                if text.lower() == "เปิดยกเลิก":
                    settings["unsendMessage"] = True
                    nn2(to, "🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดยกเลิก":
                    settings["unsendMessage"] = False
                    nn2(to,"?? ปิดแล้ว 🐱")
                if text.lower() == "เปิดออกแชท":
                    sets["autoLeave"] = True
                    sa = "🐱เปิดแล้วว >_<🐱"
                    nn2(to,str(sa))
                if text.lower() == "ปิดออกแชท":
                    sets["autoLeave"] = False
                    sa = "🐱ปิดแล้ว >_<🐱"
                    nn2(to,str(sa)) 
                if text.lower() == "เปิดติ๊กใหญ่":
                    settings["Sticker"] = True
                    nn2(to,"🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดติ๊กใหญ่":
                    settings["Sticker"] = False
                    nn2(to,"🐱 ปิดแล้ว 🐱")
                if text.lower() == "เปิดโค๊ดติ๊ก":
                    sets["Sticker"] = True
                    nn2(to,"🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดโค๊ดติ๊ก":
                    sets["Sticker"] = False
                    nn2(to,"🐱 ปิดแล้ว 🐱")
                if text.lower() == "เปิดแทค3":
                    sets["tagsticker"] = True
                    nn2(to,"🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดแทค3":
                    sets["tagsticker"] = False
                    nn2(to,"🐱 ปิดแล้ว 🐱")         
                if text.lower() == "เปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = True
                    nn2(to,"🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = False
                    nn2(to,"🐱 ปิดแล้ว 🐱")
                if text.lower() == "เปิดapi":
                    sets["Api"] = True
                    nn2(to,"🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดapi":
                    sets["Api"] = False
                    nn2(to,"🐱 ปิดแล้ว 🐱")
                if text.lower() == "เปิดอ่าน":
                    sets["autoRead"] = True
                    nn2(to,"🐱 เปิดแล้ว 🐱")
                if text.lower() == "ปิดอ่าน":
                    sets["autoRead"] = False
                    nn2(to,"🐱 ปิดแล้ว 🐱.")
#==============================================================================#
                if text.lower() == "ดึง":
                    sets["inv"] = True
                    nn2(to,"🐱 ส่งคท.ลงมา 🐱")
                if text.lower() == "ปิดดึง":
                    sets["inv"] = False
                    nn2(to,"🐱 ปิดแล้ว 🐱")
#==============================================================================#
                if text.lower() == "ตั้งรูปประกาศ5":
                    sets["gpict"] = True
                    nn2(to,"🐱ส่งรูปลงมา🐱")
                    
                if text.lower() == "เชครูปประกาศ5":
                    path = sets["glistpict"]
                    nn1.sendImage(to, path)
                    
                elif msg.text.lower() == "ประกาศมุด3":
                  a = nn1.getGroupIdsJoined()
                  path = sets["glistpict"]
                  for group in apalo["bc"]:
                    if group in a:
                       nn1.sendImage(group, str(path))
                  nn1.sendMessage(to,"สำเร็จแล้ว") 
#----------------------------------------------------------------------------#                  
                if text.lower() == "ตั้งรูปประกาศ":
                    sets["pict"] = True
                    nn2(to,"🐱 ส่งรูปลงมา 🐱")
                if text.lower() == "เชครูปประกาศ":
                    path = sets["listpict"]
                    nn1.sendImage(to, path)
#----------------------------------------------------------------------------#                    
                elif msg.text.lower() == "ประกาศ2":
                            groups = nn1.getGroupIdsJoined()
                            path = sets["listpict"]
                            for group in groups:
                                nn1.sendImage(group, str(path))
                            nn2(to, "ส่งคำประกาศเสร็จแล้ว จำนวน {} กลุ่ม".format(str(len(groups))))
#==============================================================================#
                elif text.lower() == "แทค":
                        group = nn1.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(nn1.getProfile().mid)
                        nn1.datamention(to,'แทคทุกคน',nama)
                elif text.lower() == "/แทค" or text.lower() == "tagall":
                    if msg._from in nn1MID:
                        group = nn1.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, jml = [], [], [], [], [], [], [], [], [], len(nama)
                        if jml <= 20:
                          mentionMembers(msg.to, nama)
                        if jml > 20 and jml < 40:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, len(nama)):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                        if jml > 40 and jml < 60:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, len(nama)):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                        if jml > 60 and jml < 80:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, len(nama)):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                        if jml > 80 and jml < 100:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for m in range (80, len(nama)):
                              nm5 += [nama[m]]
                          mentionMembers(msg.to, nm5)
                        if jml > 100 and jml < 120:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, len(nama)):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                        if jml > 120 and jml < 140:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for v in range (120, len(nama)):
                              nm7 += [nama[v]]
                          mentionMembers(msg.to, nm7)
                        if jml > 140 and jml < 160:
                          for i in range (0, 19):
                               nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for r in range (140, len(nama)):
                              nm8 += [nama[r]]
                          mentionMembers(msg.to, nm8)
                        if jml > 160 and jml < 180:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for z in range (140, 159):
                              nm8 += [nama[z]]
                          mentionMembers(msg.to, nm8)
                          for f in range (160, len(nama)):
                              nm9 += [nama[f]]
                          mentionMembers(msg.to, nm9)
#==============================================================================#
                elif msg.text.lower().startswith("!เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=ee1289,70&chf=bg,s,ff99cc"
                    nn1.sendImageWithURL(msg.to, urlnya)
                    
                elif msg.text.lower().startswith("ดึง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                       nn1.findAndAddContactsByMid(ls)
                                       nn1.inviteIntoGroup(to, [ls])
                                    except:
                                       nn1.sendMessage(to, "Limited !")
                                       
                elif msg.text.lower().startswith("สะกดจิต"):
                  if msg.toType == 2:
                    data = text.replace("สะกดจิต ","")
                    yud = data.split(' ')
                    yud = yud[0].replace(' ','_')
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            nn1.unsendMessage(msg_id)
                            nn1.sendMessage(to, yud,contentMetadata={"MSG_SENDER_NAME": str(nn1.getContact(ls).displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/%s" % nn1.getContact(ls).pictureStatus})
#----------------------------------------------------------------------------#                            
                elif msg.text.lower().startswith("ยูทูป"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#FF99CC"
                                            },
                                            "body": {
                                               "backgroundColor": "#333333",
                                               "separator": True,
                                               "separatorColor": "#66FFFF"
                                            },
                                            "footer": {
                                                "backgroundColor": "#FF99CC",
                                                "separator": True,
                                               "separatorColor": "#66FFFF"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "Youtube",
                                                    "weight": "bold",
                                                    "color": "#66FFFF",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=u8b4c22de6d4a1e18190ae14f76465d66"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#66FFFF"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#66FFFF",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#66FFFF",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#66FFFF",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#66FFFF",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#66FFFF",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    sendTemplate(to, data)
                                    
                elif msg.text.lower().startswith("image "):
                                query = removeCmd("image", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
#----------------------------------------------------------------------------#                                        
                if text.lower().startswith("เตะ"): 
                           key = eval(msg.contentMetadata["MENTION"])
                           key["MENTIONEES"][0]["M"]
                           targets = []
                           for x in key["MENTIONEES"]:
                               targets.append(x["M"])
                           for target in targets:
                               if target in nn1MID:
                                   pass
                               else:
                                   try:
                                       nn1.kickoutFromGroup(msg.to,[target])
                                   except:
                                       nn1.sendMessage(msg.to,"สมาชิกไม่ได้อยู่ในกลุ่มนี้ !")
                                       
                elif msg.text.lower().startswith("playstore "):
                                query = removeCmd("playstore", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                                        
                elif msg.text.lower().startswith("รูป "):
                                query = removeCmd("รูป", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.boteater.co/googleimg?search={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
#----------------------------------------------------------------------------#                                        
                elif msg.text.lower().startswith("เพิ่มเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = nn1.getContact(ls)
                                    nn1.findAndAddContactsByMid(ls)
                                nn2( to, "เพิ่ม " + str(contact.displayName) + "เป็นเพื่อนแล้ว")  
#----------------------------------------------------------------------------#  
                elif msg.text.lower().startswith("ลบเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = nn1.getContact(ls)
                                    n = len(nn1.getAllContactIds())
                                    try:
                                        nn1.deleteContact(ls)
                                    except:pass
                                    t = len(nn1.getAllContactIds())
                                    nn2( to, "Type: Friendlist\n • Detail: Delete friend\n • Status: Succes..\n • Before: %s Friendlist\n • After: %s Friendlist"%(n,t))
#----------------------------------------------------------------------------#                                    
                elif cmd == "เชคกลุ่มค้างเชิญ":
                            groups = nn1.getGroupIdsInvited()
                            ret_ = "「 รายชื่อกลุ่มค้างเชิญ 」\n"
                            no = 1
                            for gid in groups:
                                group = nn1.getGroup(gid)
                                ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no = (no+1)
                            ret_ += "\n\nจำนวน {} กลุ่ม".format(str(len(groups)))
                            ret_ += "\n\nUsage : Reject [num]"
                            nn2(to, str(ret_))
#----------------------------------------------------------------------------#                            
                elif msg.text.lower().startswith("บล็อค "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = nn1.getContact(ls)
                                    nn1.blockContact(ls)
                                nn2(to, "บล็อค" + str(contact.displayName) + "บุคคลนี้สำเร็จแล้ว")
#----------------------------------------------------------------------------#                                
                elif msg.text.lower().startswith("ไอดีไลน์ "):
                            a = removeCmd("ไอดีไลน์", text)
                            b = nn1.findContactsByUserid(a)
                            line = b.mid
                            nn1.sendMessage(msg.to,"line://ti/p/~" + a)
                            nn1.sendContact(to, line)                                                                                           
                            nn1.sendMessage(to,str(hasil))
#----------------------------------------------------------------------------#                            
                elif msg.text.lower().startswith("stag "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = nn1.getContact(receiver)
                                RhyN_(to, contact.mid)

#==============================================================================#
                elif text.lower() == 'คนสร้างกลุ่ม' or text.lower() == "แอด":
                    group = nn1.getGroup(to)
                    cg = group.creator
                    c = cg.mid
                    name = cg.displayName
                    pp = cg.pictureStatus                 
                    data = {
                        "type": "flex",
                        "altText": "แอดกลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": "By : ™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯",
                                        "size":"md",                                       
                                        "color":"#66FFFF",
                                        "align":"center"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://profile.line-scdn.net/" + str(pp),
                                        "size": "lg"
                                    },
                                    {
                                        "type":"text",
                                        "text":" "
                                    },
                                    {
                                       "type":"text",
                                       "text": name,
                                       "color":"#66FFFF",
                                       "align":"center",
                                       "size":"xl",
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                    nn1.sendContact(to, c)
#----------------------------------------------------------------------------#                    
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = nn1.getGroup(to)                    
                    nn2(to, "{ Group ID }\n" + gid.id)
                    nn2(to, nn1.getGroup(to).name, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+nn1.getGroup(to).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~', 'type': 'mt', 'subText': "™T̶e̶a̶m̶b̶o̶t̶ ̶a̶v̶e̶n̶g̶e̶r̶s̶✯", 'a-installUrl': 'https://line.me/ti/p/~', 'a-installUrl': ' https://line.me/ti/p/~', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~', 'i-linkUri': 'https://line.me/ti/p/~', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~'}, contentType=19)
                elif text.lower() == 'รูปกลุ่ม':
                    group = nn1.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    nn1.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = nn1.getGroup(to)
                    nn2(to, "ชื่อกลุ่ม -> \n" + gid.name)   
                elif text.lower() == 'ลิ้ง':
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = nn1.reissueGroupTicket(to)
                            nn1.sendMessage(to, "ลิ้งของกลุ่ม : "+group.name+"\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
#----------------------------------------------------------------------------#                            
                elif text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nn2(to, "🐱เปิดลิ้งเรียบร้อย🐱")
                        else:
                            group.preventedJoinByTicket = False
                            nn1.updateGroup(group)
                            nn2(to, "🐱เปิดลิ้งเรียบร้อย🐱")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nn2(to, "🐱ปิดลิ้งเรียบร้อย🐱")
                        else:
                            group.preventedJoinByTicket = True
                            nn1.updateGroup(group)
                            nn2(to, "🐱ปิดลิ้งเรียบร้อย🐱")
#----------------------------------------------------------------------------#                            
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = nn1.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ผู้สร้างกลุ่มนี้ลบชี"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(nn1.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม👉 : {}".format(gTicket)
                    ret_ += "\n╚══[ ™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯ ]"
                    data = {
                        "type": "flex",
                        "altText": "กลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#333333'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [                            
                                    {
                                        "type": "text",
                                        "text": ret_,
                                        "color": "#66FFFF",
                                        "wrap": True,
                                        "size": "md",
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                    nn1.sendImageWithURL(to, path)
#----------------------------------------------------------------------------#                    
                elif text.lower() == 'คนในห้อง':
                    if msg.toType == 2:
                        group = nn1.getGroup(to)
                        ret_ = "รายชื่อสามชิกในกลุ่มนี้\n"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n\nจำนวน {} คน".format(str(len(group.members)))
                        data = {
                            "type": "flex",
                            "altText": "กลุ่ม",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                        "backgroundColor": '#000000'
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": ret_,
                                            "color": "#66FFFF",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
#----------------------------------------------------------------------------#                        
                elif text.lower() == 'กลุ่มทั้งหมด':
                        groups = nn1.groups
                        ret_ = "รายชื่อกลุ่มทั้งหมด :\n"
                        no = 0 + 1
                        for gid in groups:
                            group = nn1.getGroup(gid)
                            ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n\nจำนวน {} กลุ่ม".format(str(len(groups)))
                        data = {
                            "type": "flex",
                            "altText": "Group list",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                         "backgroundColor": '#000000'
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type":"text",
                                            "text": ret_,
                                            "color": "#66FFFF",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
#----------------------------------------------------------------------------#                        
                elif "อัพชื่อ " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = nn1.getProfile()
                        profile_A.displayName = string
                        nn1.updateProfile(profile_A)
                        nn2(to,"🐱สำเร็จ🐱 :\n" + string)
                        print ("Update Name")

                elif "อัพตัส " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = nn1.getProfile()
                        profile_A.statusMessage = string
                        nn1.updateProfile(profile_A)
                        nn2(to,"🐱สำเร็จ🐱 :\n" + string)
                        print ("Update Bio Succes")
#----------------------------------------------------------------------------#                        
                elif text.lower() == "อัพรูปโปร":
                    sets["changePictureProfile"] = True
                    nn2(to, "??ส่งรูปภาพที่ต้องการลงมา🐱")
#----------------------------------------------------------------------------#                    
                elif text.lower() == "อัพรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in sets["changeGroupPicture"]:
                            sets["changeGroupPicture"].append(to)
                        nn2(to, "🐱ส่งรูปภาพที่ต้องการลงมา🐱")
#----------------------------------------------------------------------------#                
                elif cmd == "รูปทั้งห้อง":
                  kontak = nn1.getGroup(to)
                  group = kontak.members
                  picall = []
                  for ids in group:
                    if len(picall) >= 400:
                      pass
                    else:
                      picall.append({
                        "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                        "action": {
                          "type": "uri",
                          "uri": "http://line.me/ti/p/~steveneverdie002"
                          }
                        }
                      )
                  k = len(picall)//10
                  for aa in range(k+1):
                    data = {
                      "type": "template",
                      "altText": "{} membagikan janda".format(nn1.getProfile().displayName),
                      "template": {
                         "type": "image_carousel",
                         "columns": picall[aa*10 : (aa+1)*10]
                      }
                    }
                    sendTemplate(to, data)
#----------------------------------------------------------------------------#                    
                elif cmd == "เราไง":
                  contact = nn1.getContact(msg._from)
                  cover = nn1.getProfileCoverURL(msg._from)
                  nn1.reissueUserTicket()
                  res = "╭━━━━ข้อมูลเรา━━━\n"
                  res += "ชื่อเรา :{}\n".format(contact.displayName)
                  res += "MIDเรา: {}\n".format(contact.mid)
                  res += "สเตตัสเรา\n{}\n".format(contact.statusMessage)
                  nn1.sendMessage(to, res)
                  try:
                    poto = "https://os.line.naver.jp/os/p/{}".format(msg._from)
                  except:
                    poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                  dax = {
                    "type": "template",
                    "altText": "berak di celana",
                    "template": {
                      "type": "image_carousel",
                      "columns": [
                        {
                          "imageUrl": poto,
                          "layout": "horizontal",
                          "action": {
                            "type": "uri",
                            "label": "PROFILE",
                            "uri": poto,
                            "area": {
                              "x": 447,
                              "y": 356,
                              "width": 1040,
                              "height": 1040
                            }
                          }
                        },
                        {
                          "imageUrl": cover,
                          "layout": "horizontal",
                          "action": {
                            "type": "uri",
                            "label": "COVER",
                            "uri": cover,
                            "area": {
                              "x": 447,
                              "y": 356,
                              "width": 1040,
                              "height": 1040
                            }
                          }
                        },
                        {
                          "imageUrl": "https://qr-official.line.me/L/"+nn1.getUserTicket().id+".png",
                          "layout": "horizontal",
                          "action": {
                            "type": "uri",
                            "label": "CONTACT",
                            "uri": "https://line.me/ti/p/"+nn1.getUserTicket().id,
                            "area": {
                              "x": 447,
                              "y": 356,
                              "width": 1040,
                              "height": 1040
                            }
                          }
                        }
                      ]
                    }
                  }
                  sendTemplate(to, dax)
                  
                elif cmd == 'เพื่อน':a = nn1.refreshContacts();nn1.datamention(msg.to,'รายชื่อเพื่อน',a)
#===============================================================
#🎃🎃🎃🎃🎃🎃🎃   โหมดไวรัสเอจัง  by.Chivaree   🎃🎃🎃🎃🎃🎃🎃
#    👉👉👉👉   คำเตือน  : เนื่องจากไวรัสเอจังเป็นคำสั่งไวรัสแบบสั่งงาน 2 ชั้น
#     หากท่านแก้ไขหัวคำสั่ง. หรือชือไวรัส อาจทำให้ไวรัสไม่แสดงผล และผิดเพี้ยนไป
#     เพราะคำสั่งจะเป็นแบบผูกกันจะมีตัวแปลซ้อนอีกทีแบบสองชั้นคับ
#  💖 แต่ถ้าท่านมีความเข้าใจในการทำงานสองชั้น เชิญท่านแก้ไขได้ตามสบายคับ จุ้ฟป้อก
              ##           แก้ดีๆ ระวังไฟล์พังไม่รุ้นะ. 5555555 เตือนแล้ว
#----------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ระเบิดเวลาเอจัง","เอจังวางระเบิด","วางระเบิด","ระเบิดเวลา"]:
                    nn1.sendMessage(msg.to,"✧••••••••❂✧A-jáng✧❂••••••••✧\n ✯:::[[[: ֆҽℓƒ-β❂T-ՃิՁণຮี :]]]:::✯")
                    nn1.sendMessage(msg.to,"💣::โหมดระเบิดเวลาเอจังคับ::💣")
                    nn1.sendMessage(msg.to,"⏳::เริ่มจุดชนวนระเบิดเวลาคับ::⌛")
                    nn1.sendMessage(msg.to,"⏰⏳::⭐9⭐::⌛⏰")
                    nn1.sendMessage(msg.to,"⏰⏳::⭐8⭐::⌛⏰")
                    nn1.sendMessage(msg.to,"⏰⏳::⭐7⭐::⌛⏰")
                    nn1.sendMessage(msg.to,"⏰⏳::⭐6⭐::⌛⏰")
                    nn1.sendMessage(msg.to,"⏰⏳::⭐5⭐::⌛⏰")
                    nn1.sendMessage(msg.to,"⏰⏳::⭐4⭐::⌛⏰")
                    nn1.sendMessage(msg.to,"⏰⏳::⭐3⭐่::⌛⏰")
                    nn1.sendMessage(msg.to,"⏰⏳::⭐2⭐::⌛⏰")
                    nn1.sendMessage(msg.to,"⏰⏳::⭐1⭐::⌛⏰")
                    nn1.sendMessage(msg.to,"⏰⏳:: ......................")
                    nn1.sendMessage(msg.to,"Error... ไม่พบสัญญาน")
                    nn1.sendMessage(msg.to, "💣💣💣??💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣??💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣??💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣??\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
                    nn1.sendMessage(msg.to, "💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣??💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣??💣💣💣💣💣💣💣??\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣??💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
                    nn1.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.??.💔.💙.")
                    nn1.sendMessage(msg.to, "??.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.ค่.ะ.💚.💟.💛.🤗.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.i0s.ก.า.ดึ๊.บ.ๆ.b.y.เ.อ.จั.ง.??.💟.💗.🤗...")
                    nn1.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    nn1.sendMessage(msg.to,"💥💥💥💥💥💥💥💥\n   ระเบิดดังตู้มเลยคร้า\n💥💥💥💥💥💥💥💥")
#=======================================================================
                elif msg.text in ["ไวรัสอวตาร","ไวรัสอวตาล"]:
                    nn1.sendMessage(msg.to,"ไวรัสอวตาร•➣➣➣➣➣➣➣➣\n    ❂••••••✧A-jáng✧•••••••❂\n➣➣➣➣➣➣➣➣ •Chiväree™")
                    nn1.sendMessage(msg.to,"💙:::⭐ 9 ⭐:::💙")
                    nn1.sendMessage(msg.to,"💚:::⭐ 8 ⭐:::💚")
                    nn1.sendMessage(msg.to,"💖:::⭐ 7 ⭐:::💖")
                    nn1.sendMessage(msg.to,"💚:::⭐ 6 ⭐:::💚")
                    nn1.sendMessage(msg.to,"💖:::⭐ 5 ⭐:::💖")
                    nn1.sendMessage(msg.to,"💔:::⭐ 4 ⭐:::💔")
                    nn1.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    nn1.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    nn1.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    nn1.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
                    nn1.sendMessage(msg.to,"💖💖💖💖💖💖💖💖💖💖💖💖\n💚💚💚💚💚💚💚💚💚💚💚💚\n   ขออภัยท่านเอจังยังไม่ใส่โค๊ดคับ\n💚💚💚💚💚💚💚💚💚💚💚💚\n💖💖💖💖💖💖💖💖💖💖💖💖")
#-----------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสแมนยู","ไวรัสผีแดง"]:
                    nn1.sendMessage(msg.to,"ไวรัสแมนยู•➣➣➣➣➣➣➣➣\n    ❂••••••✧A-jáng✧•••••••❂\n➣➣➣➣➣➣➣➣ •Chiväree™")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n?? Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n?? Glory Glory Man U ??\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U ??\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U ??\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U ??\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n?? Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U ??\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"?? Glory Glory Man U ??\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U ??\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈\n😈 Glory Glory Man U 😈")
                    nn1.sendMessage(msg.to,"เกรียน on 7 Man United Fc Club")
#----------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัสชนบท"]:
                    nn1.sendMessage(msg.to," ╬╬❂•ຟနุ้७ຟနิ้७•❂╬╬")
                    nn1.sendMessage(msg.to,"💙:::⭐ 9 ⭐:::💙")
                    nn1.sendMessage(msg.to,"💚:::⭐ 8 ⭐:::💚")
                    nn1.sendMessage(msg.to,"💖:::⭐ 7 ⭐:::💖")
                    nn1.sendMessage(msg.to,"💚:::⭐ 6 ⭐:::💚")
                    nn1.sendMessage(msg.to,"💖:::⭐ 5 ⭐:::💖")
                    nn1.sendMessage(msg.to,"💔:::⭐ 4 ⭐:::💔")
                    nn1.sendMessage(msg.to,"💙:::⭐ 3 ⭐:::💙")
                    nn1.sendMessage(msg.to,"💚:::⭐ 2 ⭐:::💚")
                    nn1.sendMessage(msg.to,"💖:::⭐ 1 ⭐:::💖")
                    nn1.sendMessage(msg.to,"💚:::⭐ 0 ⭐:::💚")
                    nn1.sendMessage(msg.to,"❂•➤➤➤➤➤➤➤➤➤➤➤➤\n • ด้วยความกันดารไร้สัญญาน\n • และสุดแสนชนบทนี้\n • ระบบจึงไม่สามารถรันไวรัสได้\n • ขออภัยอย่างสูงคะ by.เอจัง\n❂•➤➤➤➤➤➤➤➤➤➤➤➤")
#-----------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["สีชมพูคับ"]:
                    nn1.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    nn1.sendMessage(msg.to, "A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5.A.6.A.7.A.8.A.9.A.0.A.1.A.2.A.3.A.4.A.5")
                    nn1.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    nn1.sendMessage(msg.to, "\n💗•💗•💗•Virus Pink•💗•💗•💗\n")
#----------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["Man United Fc Club"]:
                    nn1.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to,"💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    nn1.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    nn1.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    nn1.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    nn1.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to,"💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    nn1.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    nn1.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to,"💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    nn1.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to,"ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    nn1.sendMessage(msg.to,"💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to,"   🔅Glory Glory ManUnited🔅\n😈•แมนเชสเตอร์ยูไนเต็ด เอฟซี•😈")
#-------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ปีโป้อร่อยจัง"]:
                    nn1.sendMessage(msg.to, "ไ.ว.รั.ส.คิ.ด.ตี้.เ.อ.จั.ง.~.💚เ.ฉ.พ.า.ะ.ไ.ล.น์.เ.ขี.ย.ว.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.♡.K.1.t.t.y.b.y.เ.อ.จั.ง.~.☆.💖.💔.💙.")
                    nn1.sendMessage(msg.to, "💖.V.i.r.u.s.A.-j.a.n.g.💗.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.⭐.เอ.จัง.1.0.V.E.??.N.e.w.2.0.1.9.💗")
                    nn1.sendMessage(msg.to, "ไ.ว.รั.ส.เ.อ.จั.ง.คุริๆอะจึ๋งๆ~🌟ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Qฆ.Q4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.Q.4.ฆ.เอจังคับ")
                    nn1.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    nn1.sendMessage(msg.to, "ไวรัสเอจังฟรุ้งฟรุ้งมุ้งมิ้ง~☆😍💜💛💚💙💗💖.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.๔.4.ฟรุ้งฟริ้ง by.เอจัง~☆🤗")
                    nn1.sendMessage(msg.to, "💗.ไ.ว.รั.ส.เ.อ.จั.ง.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                    nn1.sendMessage(msg.to, "123") #
#---------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ไวรัส"]:
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "■•■•■• Virus •■•■•■")
                    nn1.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤")
                    nn1.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤")
                    nn1.sendMessage(msg.to, "123") #
#--------------------------------------------------------------------------------------------------------------------------------                 nn1.sendMessage(msg.to,"🍰🍡🍤🍗🍋🍄🍓🍏🍉🍧🍟\n  อิ่มมากเลย ขอหลับก่อนน๊าคับ\n🍏🍇🍎🍆🍅🍄🍋🍊🍡🍙🍚")
#------------------------------------------------------------------------------------------------------------------------------------------
# 💚💛💜     สุดเขตแดนไวรัสเอจัง  ขอให้เล่นอย่างสนุกสนานนะคับ จุ้ฟป้อก
#------------------------------------------------------------------------------------------------------------------------------------------
                elif msg.text in ["ผู้สร้างไวรัส"]:
                    nn1.sendMessage(msg.to, "ผู้สร้างไวรัส➣➣➣➣➣➣➣➣\n   ❂••••••NN•••••••❂\n➣➣➣➣➣➣➣➣•™")
                    nn1.sendMessage(msg.to, "💗💗💗💗💗💗💗💗💗💗\n   •ผู้สร้างไวรัสที่แสนน่ารัก•\n💗💗💗💗💗💗💗💗💗💗")
                    nn1.sendMessage(msg.to, "💚💚💚💚💚💚💚💚💚💚\n   •ผู้สร้างไวรัสที่แสนน่ารัก•\n💚??💚💚💚💚💚💚💚💚")
                    nn1.sendMessage(msg.to, "💗💗💗💗💗💗💗💗💗💗\n   •ผู้สร้างไวรัสที่แสนน่ารัก•\n💗💗💗💗💗💗💗💗💗💗")
                    nn1.sendMessage(msg.to, "💚💚💚💚💚💚💚💚💚💚\n   •ผู้สร้างไวรัสที่แสนน่ารัก•\n💚💚💚💚💚💚💚💚💚💚")
                    nn1.sendMessage(msg.to, "●•➤➤➤➤➤➤➤➤➤➤\n    \n●•➤➤➤➤➤➤➤➤➤➤")
                    nn1.sendMessage(msg.to, "💔💔💔 [ คนไหน ] 💔💔💔")
                    nn1.sendMessage(msg.to, "💚💚💚 [ คนไหน ] 💚💚💚")
                    nn1.sendMessage(msg.to, "💜💜💜 [ คนไหน ] 💜💜💜")
                    nn1.sendMessage(msg.to, "💛💛💛 [ คนไหน ] 💛💛💛")
                    nn1.sendMessage(msg.to, "💖💖💖 [ คนไหน ] 💖💖💖")
                    nn1.sendMessage(msg.to,"🌟৩้Ꭷ৩ꪶꪶ৩้৩: 🕟 " +datetime.today().strftime('%H:%M:%S')+ "➤")
                    line.sendContact(to, "u31c5c63ce975c3129b2f2c7f0b3b4f9e")
                    nn1.sendMessage(msg.to, "👆•ผู้สร้าง•👆")
#--------------------------------------------------------------------------------------------------------------------------                    
#=====================================================================
                
                elif text.lower()== "ตั้งติ๊กคนแทค":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "tag"
                    nn2(to, "🐱 ส่งสติกเกอรที่จะใช้ลงมา 🐱")
                elif msg.text.lower() == "ลบติ๊กคนแทค":
                    sets["messageSticker"]["listSticker"]["tag"] = None
                    nn2(to, "🐱 ลบสติกเกอรคนแทคแล้ว 🐱")
                elif msg.text.lower()== "ตั้งติ๊กคนเข้า":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "wc"
                    nn2(to, "🐱 ส่งสติกเกอรที่จะใช่ลงมา 🐱")
                elif msg.text.lower() == "ลบติ๊กคนเข้า":
                    sets["messageSticker"]["listSticker"]["wc"] = None
                    nn2(to, "🐱 ลบสติกเกอรคนเข้าแล้ว 🐱")
                elif msg.text.lower()== "ตั้งติ๊กคนออก":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "lv"
                    nn2(to, "🐱 ส่งสติกเกอรที่จะใช่ลงมา 🐱")
                elif msg.text.lower() == "ลบติ๊กคนออก":
                    sets["messageSticker"]["listSticker"]["lv"] = None
                    nn2(to, "🐱 ลบสติกเกอรคนออกแล้ว 🐱")
                elif msg.text.lower()== "ตั้งติ๊กคนแอด":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "add"
                    nn2(to, "🐱 ส่งสติกเกอรที่จะใช่ลงมา 🐱")
                elif msg.text.lower() == "ลบติ๊กคนแอด":
                    sets["messageSticker"]["listSticker"]["add"] = None
                    nn2(to, "🐱 ลบสติกเกอรคนแอดแล้ว 🐱")
                elif msg.text.lower() == "ตั้งติ๊กมุดลิ้ง":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "join2"
                    nn2(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติ๊กลิ้ง":
                    sets["messageSticker"]["listSticker"]["join2"] = None
                    nn2(to, "ลบสติกเกอรแล้ว")
                    
                elif "คลอ " in msg.text.lower():
                    if msg.toType == 2:
                        sep = msg.text.split(" ")
                        resp = msg.text.replace(sep[0] + " ","")
                        num = int(resp)
                        try:
                            nn1.sendReplyMessage(msg.id,to,"กำลังดำเนินการ...")
                        except:
                            pass
                        for var in range(num):
                            group = nn1.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            nn1.acquireGroupCallRoute(msg.to)
                            nn1.inviteIntoGroupCall(msg.to, contactIds=members)
                        nn1.sendReplyMessage(msg.id,to,"เชิญคอลสำเร็จแล้ว(｀・ω・´)")    
#=====================================================================
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nn1.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            elif msg.contentType == 1:
                if sets["pictsa"] == True:
                    path = nn1.downloadObjectMsg(msg_id)
                    sets["pictsa"] = False
                    sets["sendpict"] = str(path)
                    nn2(to, "🐱บันทึกเรียบร้อย🐱")
            elif msg.contentType == 1:
                if sets["gpict"] == True:
                    path = nn1.downloadObjectMsg(msg_id)
                    sets["gpict"] = False
                    sets["glistpict"] = str(path)
                    nn2(to, "🐱สำเร็จ🐱")
                if sets["pict"] == True:
                    path = nn1.downloadObjectMsg(msg_id)
                    sets["listpict"] = str(path)
                    sets["pict"] = False
                    nn2(to, "🐱สำเร็จ🐱")
            elif msg.contentType == 1:
                if sets["changePictureProfile"] == True:
                    path = nn1.downloadObjectMsg(msg_id)
                    sets["changePictureProfile"] = False
                    nn1.updateProfilePicture(path)
                    nn2(to, "🐱ทำการเปลี่ยนรูปสำเร็จ🐱")
                if msg.toType == 2:
                    if to in sets["changeGroupPicture"]:
                        path = nn1.downloadObjectMsg(msg_id)
                        sets["changeGroupPicture"].remove(to)
                        nn1.updateGroupPicture(to, path)
                        nn2(to, "🐱เปลี่ยนรูปภาพกลุ่มเรียบร้อย🐱")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nn1.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver                                   
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                        try:
                            nn1.unsendMessage(msg.id)
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            nn1.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            nn1.sendMessage(to, str(ret_))
                        except Exception as error:
                            nn1.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in nn1MID:
                            try:
                                nn1.kickoutFromGroup(msg.to,[sender])
                                nn1.sendMessage("บอกแล้อย่าพิมไม่เชื่อจุกไปสิ55555")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = nn1.findGroupByTicket(ticket_id)
                                nn1.acceptGroupInvitationByTicket(group.id,ticket_id)
                                nn1.sendMessage(group.id,str(tagadd["m"]))
                                nn1.sendMessage(to, "เข้าไปสิงในห้องชื่อ %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            nn1.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        nn1.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
            elif msg.contentType == 7:
                if sets["Sticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    nn1.sendMessage(to, str(ret_))
#=====================================================================
#========================================================================
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nn1.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return                                 
#========================================================================
#===================LOGOUT BOT=================================#                    
                if msg.contentType == 0:
                    if msg.toType == 0 or msg.toType == 2:
                        if cmd == "logout" and sender == nn1MID:
                            nn1.generateReplyMessage(msg.id)
                            nn1.sendReplyMessage(msg.id, to, "ออกจากระบบบอทแล้วค่ะ ♪")
                            nn1.sendReplyMessage(msg.id, to, "AVENGERS BOT♪")
                            sys.exit("Logout")
            elif msg.contentType == 7:  
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        nn1.unsendMessage(msg.id)
                        contact = nn1.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        nn1.unsendMessage(msg.id)
                        contact = nn1.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != nn1MID: to = sender
                else: to = receiver
                if sets['autoRead'] == True:
                   nn1.sendChatChecked(to, msg_id)  
#---------------[ชุดคำสั่ง คีย์เวิดบอทApi]-------------------------------------------------------------#               
                if sets["Api"] == True:
            	    if msg.text in ["/Spam1 40000","/Spam1 30000","/Spam1 20000","/Spam1 10000","/Spam1 5000","/Spam1 3000","/spam1 30000","/spam1 20000","0","110","90","/spam1 40000"]:
                        nn1.kickoutFromGroup(receiver,[sender])
                        nn2(to,"🚫ตรวจพบคำสั่งสแปมเลขจำเป็นต้องเตะออก\nระบบป้องกันการสแปมเลขทำงาน")              
                if sets["Api"] == True:
            	    if msg.text in ["ควย","หี","แตด","เย็ด","ไอสัต","ไอ้สัต","เหี้ย","ไอเหี้ย","ไอ้เหี้ย","ควยไร","ไอ้ห่า","ห่า","ครวย","อีสัส","อีสัต","อีเหี้ย","ไอ้ควาย","ไอ่ควาย"]:                        
                        nn3(to,"🚫ตรวจพบคำหยาบคาย\nระบบเตะควายทำงาน จุ๊บป๊อก❣️")                          
                        nn1.kickoutFromGroup(receiver,[sender])               
                if sets["Api"] == True:
            	    if msg.text in ["เชลไก่","กะจอก","กระจอก","เชลกระจอก","บอทเหี้ย","กาก","กากก","เชลกาก","พ่อมึงตาย","ไอ้เลว","ระยำ","ชาติหมา","หน้าหี","เซลกาก","ไอ้บอทกาก","ไอ้เหี้ยบอท","พ่องตาย","ส้นตีน","แม่มึงอ่ะ","แม่มึงดิ","พ่อมึงดิ","บอทกาก"]:                        
                        nn3(to,"🚫ตรวจพบคำหยาบคาย\nระบบเตะควายทำงาน จุ๊บป๊อก❣️")  
                        nn1.kickoutFromGroup(receiver,[sender])    
                if sets["Api"] == True:
            	    if msg.text in ["!kickall","/kickall","!บิน","!หีแตด","หีแตด","!!บิน","leanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","Kick"]:                        
                        nn2(to,"🚫ตรวจพบคำสั่งบิน\nระบบเตะควายทำงาน จุ๊บป๊อก❣️")
                        nn1.kickoutFromGroup(receiver,[sender])
#----------------------------------------------------------------------------#                                               
                if sets["Api"] == True:
            	    if msg.text in ["บอท","bot","."]:                       
                        nn3(to,"👉™ᴛᴇᴀᴍʙᴏᴛɴᴇᴠᴇʀᴅɪᴇ✯͜͡❂➣👈")                          
                if sets["Api"] == True:
            	    if msg.text in ["งง","งงง",".งง"]:                       
                        nn3(to,"👉ไม่ต้อง งง ผมหล่อแบบนี้มานานแล้ว👈")                      
                if sets["Api"] == True:
            	    if msg.text in ["me","Me","/me"]:                       
                        nn3(to,"👉 🐱ม่ายมี🐱 👈")                       
                if sets["Api"] == True:
            	    if msg.text in ["Sp","sp","/sp"]:                       
                        nn3(to,"👉🚀เร็วแรงติดจรวดเลยคับ🚀👈")                                            
                if sets["Api"] == True:
            	    if msg.text in ["จารนัท","นัท","นัด","จารมน","ตามน","จารมนต์","ตามนต์"]:
                      chivaree1 = ['🌟•🌟 ลูกพี่ไม่ว่างคับ 🌟•🌟','••❂ ลูกพี่ไม่ว่างคับ ❂••']
                      chivaree2 = ['   •พี่นั่งสมาธิอยู่..เดี่ยวปืนลั่นคับ•','  •ขับเครื่องบินอยู่อย่ารบกวนคับ•','  •เรียกบ่อยแบบนี้ให้แม่มาขอต่ะ•','   •กำลังเกรียนอยู่อย่ามายุ่งคับ•','  •ให้อาหารว่างไดโนเสาร์อยู่คับ•',' •ติดธุรกิจปลากัด100ล้าน•','   • ปั่นป๊อกเด้งอยู่อย่าเรียกคับ •','  •ติดถ่ายแบบอยู่รอตามคิวน่ะคับ•','  •สร้างแลนมาร์คอยู่รอในเกมคับ•','    •รันไวรัสอยู่..เอาด้วยไหมคับ•','  •ไม่ว่างเล่นด้วยนะขัดสนิมปืนอยู่•',' •ไปเล่นขี้พลางๆนะคับพี่ยังไม่ว่าง•']
                      chivaree3 = "❂———————————————❂\n" + random.choice(chivaree1) + "\n❂———————————————❂\n" + random.choice(chivaree2) + "\n🌟 AVENGERS BOT🌟"
                      nn3(to, chivaree3)                        
                if sets["Api"] == True:
            	    if msg.text in ["555","5555","55555","555555","555+"]:
                       data={"type":"template","altText":"🌟🌟 NN Sticker 🌟🌟","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSMfx1.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•AVENGERS•🌟🌟",}}]}}
                       sendTemplate(to, data)                        
                if sets["Api"] == True:
            	    if msg.text in ["สต","สต.","ส.ต."]:
                       data={
                           "type": "flex","altText": "☆•A-jang API•☆","contents": { "type": "bubble",     
                           "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "🌟•สต.  มันคืออายัยหรอคับ•🌟","color": "#00ff00","align": "center","size": "lg"},{"type": "text","text": "••• [ AVENGERS 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ ] •••","color": "#ffffff","align": "center","size": "sm"}]},
                           "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       sendTemplate(to, data)                       
                if sets["Api"] == True:
            	    if msg.text in ["กินข้าว","ทานข้าว","กินข้าวกัน","ทานข้าวกัน","กินขนมหวาน","กินขนมจีน","กินกล้วยทอด","มาม่า","กินมาม่า","กินขนม","ขนมจีน","กล้วยทอด","ตีน","กินตีน","เมากัน","กินเหล้ากัน","เหล้ากัน","ส้นตีน","ขี้หมา","ขี้วัว","ขี้ไก่","กินขี้"]:
                       data={
                          "type": "flex","altText": "☆•A-jang API•☆","contents": { "type": "bubble",     
                          "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "🌟ไม่เคยกินเหรอคับ•🌟","color": "#00ff00","align": "center","size": "sm"},{"type": "text","text": "••• [ AVENGERS 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ ] •••","color": "#ffffff","align": "center","size": "sm"}]},
                          "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       sendTemplate(to, data)                       
                if sets["Api"] == True:
            	    if msg.text in ["ลบแชท",".ลบแชท","ลบรัน",".ลบรัน","ลบกลุ่ม","ลบเพื่อน","ลบข้อความ","ลบดำ",".ลบดำ"]:
                       data={
                           "type": "flex","altText": "☆•A-jang API•☆","contents": { "type": "bubble",     
                           "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "🌟•ขอลบเทอออกจากใจบ้างน่ะ•🌟","color": "#00ff00","align": "center","size": "sm"},{"type": "text","text": "••• [ AVENGERS 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ ] •••","color": "#ffffff","align": "center","size": "sm"}]},
                           "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       sendTemplate(to, data)                        
                if sets["Api"] == True:
            	    if msg.text in ["ล้างแชท",".ล้างแชท","ล้างรัน"".ล้างรัน","ล้างเพื่อน","ล้างดำ",".ล้างดำ"]:
                       data={
                           "type": "flex","altText": "☆•A-jang API•☆","contents": { "type": "bubble",     
                           "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "🌟•ไปล้างที่คาร์แคร์ดิ•🌟","color": "#00ff00","align": "center","size": "sm"},{"type": "text","text": "••• [ AVENGERS 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ ] •••","color": "#ffffff","align": "center","size": "sm"}]},
                           "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       sendTemplate(to, data)                       
                if sets["Api"] == True:
            	    if msg.text in ["ดึง","ฝากดึง","ดึงที","ฝากดึงที","ดึงหน่อย"]:
                       data={
                           "type": "flex","altText": "☆•A-jang API•☆","contents": { "type": "bubble",     
                           "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "🌟•ไม่ดึงนะคับไม่อยากรู้จัก•🌟","color": "#00ff00","align": "center","size": "sm"},{"type": "text","text": "••• [ AVENGERS 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ ] •••","color": "#ffffff","align": "center","size": "sm"}]},
                           "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       sendTemplate(to, data)                       
                if sets["Api"] == True:
            	    if msg.text in ["รอ","รอๆ","รอนะ","จะรอ","รออยู่","รอยู่","แปป","รอแปป","แปปปป","แปปป","แปปนึงคับ","แปปนึง","รอแปปคับ","แปปคับ","แปปคับ","แปปคะ","แปปครับ","แปปๆ","แป๊ป","แปปนะ","แปปน่ะ"]:
                       data={
                           "type": "flex","altText": "☆•A-jang API•☆","contents": { "type": "bubble",     
                           "body": {"type": "box","layout": "vertical",   "contents": [{"type": "text","text": "🌟•ไม่นานคับ แค่ 12 ชั่วโมงเอง•🌟","color": "#ffffff","align": "center","size": "sm"},{"type": "text","text": "••• [ AVENGERS 🕒 " +datetime.today().strftime('%H:%M:%S')+ "™ ] •••","color": "#ffffff","align": "center","size": "sm"}]},
                           "styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": "#ffffff","separator": True,"separatorColor": "#000000"}}}}
                       sendTemplate(to, data)
#----------------------------------------------------------------------------#                         
                if msg.contentType == 0 and sender not in nn1MID and msg.toType == 2:
                   if "MENTION" in list(msg.contentMetadata.keys())!= None:
                     if tagadd["tags"] == True:
                         user = nn1.getContact(msg._from)
                         names = user.displayName
                         pp = user.pictureStatus
                         pro = "https://profile.line-scdn.net/" + str(pp)
                         s = "#66FFFF"
                         name = re.findall(r'@(\w+)', msg.text)
                         mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                         mentionees = mention['MENTIONEES']
                         for mention in mentionees:
                             if mention['M'] in nn1MID:
                                sendTemplate(to,{"type":"flex","altText": "ตอบแทค","contents":{"type":"bubble","styles": {"body": {"backgroundColor": "#000000"},"footer": {"backgroundColor": '#000000'}},"footer":{"layout":"horizontal","contents":[{"color":"#FFCCFF","type":"text","wrap":True,"align":"center","text":"Profile","action":{"uri":"line://app/1644992891-KOnapywG?type=profile","type":"uri"},"weight":"bold","size":"xs"},{"color":"#FFCCFF","type":"separator"},{"color":"#FFCCFF","type":"text","wrap":True,"align":"center","text":"Add Me","action":{"uri":"line://ti/p/~0969245004","type":"uri"},"weight":"bold","size":"xs"}],"type":"box"},"body":{"type":"box","layout":"vertical","contents":[{"type":"separator","color":s,"margin":"lg"},{"type":"text","text":"|","color":"#000000"},{"type":"box","layout":"horizontal","contents":[{"type":"image","url": pro},{"type":"separator","color":s,"margin":"lg"},{"type":"text","text":"✯ตอบแทคอัตโนมัติ✯\nชื่อคนแทค :\n{}".format(names),"size":"sm","margin":"md","color":s,"gravity":"center","weight": "bold","flex":2,"wrap":True}]},{"type":"box","layout":"vertical","contents":[{"type":"text","text":"|","color":"#000000"},{"type":"text","text":tagadd["tag"],"size":"sm","color":s,"align":"center","weight": "bold","wrap":True},{"type":"separator","color":s,"margin":"lg"}]}]}}})

                if msg.contentType == 0 and sender not in nn1MID and msg.toType == 2:
                   if "MENTION" in list(msg.contentMetadata.keys())!= None:
                     if sets["tagkick"] == True:
                         user = nn1.getContact(msg._from)
                         names = user.displayName
                         name = re.findall(r'@(\w+)', msg.text)
                         mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                         mentionees = mention['MENTIONEES']
                         for mention in mentionees:
                             if mention['M'] in nn1MID:
                                 nn2(to, "แทคผมทำไมครับ {}".format(names))
                                 nn1.kickoutFromGroup(to, [msg._from])
                if msg.contentType == 0 and sender not in nn1MID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if nn1MID in mention["M"]:
                                    #  contact = nn1.getContact(nn1MID)
                                   #   a = contact.displayName
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = nn1.getContact(nn1MID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = nn1.getContact(nn1MID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = nn1.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n👑" + Name
                            siderMembers(op.param1, [op.param2])
                            nn1.sendContact(op.param1, op.param2)
                            contact = nn1.getContact(op.param2)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            nn1.sendImageWithURL(op.param1, image)
                            msg = sets["messageSticker"]["listSticker"]["readerSticker"]
                            if msg != None:
                                sid = msg["STKID"]
                                spkg = msg["STKPKGID"]
                                sver = msg["STKVER"]
                                sendSticker(op.param1, sver, spkg, sid)
                            
                                
                    else:       
                        pass
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 19:
            if nn1MID in op.param3:
                apalo["Talkblacklist"][op.param2] = True
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
               if mc["wr"][str(msg.text)]:
                   nn1.sendMessage(msg.to,mc["wr"][str(msg.text)])
            except:
              pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nn1.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if msg.text.lower().startswith("แปรงคท "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    nn1.sendContact(msg.to,str(getx))
                if msg.text.startswith("ตั้งapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        mc["wr"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                        nn1.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: "+ str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("ล้างapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del mc["wr"][getx]
                        nn1.sendMessage(msg.to, "คำ " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "เชคapi":
                    lisk = "[ คำตอบโต้ทั้งหมด ]\n"
                    for i in mc["wr"]:
                        lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(mc["wr"][i])+"\n"
                    lisk+="\nวิธีล้างapi >\\<\nล้างapi ตามด้วยคำที่จะล้าง"
                    data = {"type": "text","text": "{}".format(lisk),"sentBy": {"label": "™T̶e̶a̶m̶b̶o̶t̶ ̶a̶v̶e̶n̶g̶e̶r̶s̶✯", "iconUrl": "https://obs.line-scdn.net/{}".format(nn1.getContact(nn1MID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u31c5c63ce975c3129b2f2c7f0b3b4f9e"}}
                    sendTemplate(to,data)
#==============================================================================#
#==============================================================================#
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nn1.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            nn1.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        nn1.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
                        
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != nn1MID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = nn1.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = nn1.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = nn1.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = nn1.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = nn1.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                nn1.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    nn1.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        nn1.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            nn1.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                nn1.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    nn1.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        nn1.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            NOTIFIED_READ_MESSAGE(op)
    except Exception as error:
        logError(error)

#==============================================================================#
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        try:
            ops = nn1Poll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(nn1Bot(op))
                   nn1Poll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()
