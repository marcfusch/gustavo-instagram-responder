"""
@author: marcfusch
Thanks to @adw0rd for creating instagrapi,to @ssut for creating the Google translate API,
to @jacebrowning for creating memegen and Silio for this incredible idea
"""

from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import time
from googletrans import Translator
import requests

photo_path = 'gusmeme.jpg'
username='YOUR_USERNAME'
password='YOUR_PASSWORD'

cl = Client()
tr=Translator()

def log(message):
    print(str(time.strftime("%H:%M:%S", time.localtime())) + " "+ message)
    pass

def get_followers(myselfid):
    mydict=cl.user_following(myselfid,False,0)
    L=[]
    for followingid in mydict.keys():
        L.append(int(followingid))
    if L:
        log("Followers list succesfully retrieved")
        log("Followers: "+str(len(L)))
    else:
        log("Error while retrieving followers list. Maybe the account is private or has no followers")
    return(L)
    pass

def sanitize(inputstr):
    direcstring=str(inputstr[0])
    L=direcstring.split(', ')
    X = [i for i in L if i.startswith('text=')]
    X=X[0].split('=')
    L=L[1].split('=')
    message=str(X[1])
    newmesid=int(L[1])
    return(newmesid,str(message[1:-1]))
    pass

def unread_to_userid():
    direct_pending=cl.direct_pending_inbox(1)
    if direct_pending:
        return(sanitize(direct_pending))
    direct_mainbox=cl.direct_threads(1,"unread")
    if direct_mainbox:
        return(sanitize(direct_mainbox))
    else:
        return(0,"")
    pass


def send_message(scammerid,message):
    create_gustavo(message)
    cl.direct_send_photo(photo_path, user_ids=[scammerid])
    pass

def create_gustavo(trans):
    translang=['fr','ko','de','la','en','fr']
    
    trans=tr.translate(trans,dest=translang[0],src=translang[0])
    for i in range(len(translang)-1):
        trans=tr.translate(trans.text,dest=translang[i+1],src=translang[i])
    trans=trans.text

    regex=['@','#','$','*','&','?',')','(','!','"',"'"]
    for i in regex:
        trans=trans.replace(i,"")
    
    log("Translated reponse: "+str(trans))
    
    url="https://api.memegen.link/images/custom/_/"+trans+".jpg?background=https://marcfusch.com/img/gus.png"
    r= requests.get(url, allow_redirects=True)
    open(photo_path,'wb').write(r.content)
    pass

cl.set_locale('fr_FR')
cl.set_timezone_offset(1 * 60 * 60)
cl.login(username,password)
log("Login succesfull")

log("Getting your account id")
myselfid=cl.user_id_from_username(username)

log("Getting followers from user: "+ username)
lstfollowers=get_followers(myselfid)
oldmesid=0
newmesid,message=unread_to_userid()

while True:
    for i in range(30):
        try:
            if  newmesid==0 or newmesid==oldmesid or newmesid==myselfid:
                log("No unread messages")
                newmesid,message=unread_to_userid()
            else:
                log("New activity from user: " + str(newmesid))
                if newmesid in lstfollowers:
                    log(str(newmesid)+" is a follower")
                else:
                    log(str(newmesid)+" isnt a follower")
                    log(str(newmesid)+" says: " +message)
                    send_message(newmesid,message)
                    log("Gustavo sent!")
                    newmesid=0
                oldmesid=newmesid
            time.sleep(1)
        except LoginRequired:
            cl.relogin()
      
    log("Refreshing followers list")
    lstfollowers=get_followers(myselfid)
    pass
