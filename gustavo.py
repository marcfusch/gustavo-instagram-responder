"""
@author: marcfusch
Thanks to adw0rd (for making this project possible)
Thanks to Silio for giving me this incredible idea at midnight.
"""

from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import time

photo_path = 'gus.jpg'
username='YOUR_USERNAME'
password='YOUR_PASSWORD'

cl = Client()

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
    L=direcstring.split(',')
    L=L[1].split('=')
    newmesid=int(L[1])
    return(newmesid)
    pass

def unread_to_userid():
    direct_pending=cl.direct_pending_inbox(1)
    if direct_pending:
        return(sanitize(direct_pending))
    direct_mainbox=cl.direct_threads(1,"unread")
    if direct_mainbox:
        return(sanitize(direct_mainbox))
    else:
        return(0)
    pass

def send_message(scammerid):
    cl.direct_send_photo(photo_path, user_ids=[scammerid])
    pass



cl.set_locale('fr_FR')
cl.set_timezone_offset(1 * 60 * 60)
cl.login(username,password)
print("Login succesfull")


log("Getting your account id")
myselfid=cl.user_id_from_username(username)

log("Getting followers from user: "+ username)
lstfollowers=get_followers(myselfid)
oldmesid=0
newmesid=unread_to_userid()


while True:
    for i in range(50):
        try:
            if  newmesid==0 or newmesid==oldmesid or newmesid==myselfid:
                log("No unread messages")
                newmesid=unread_to_userid()
            else:
                log("New activity from user: " + str(newmesid))
                if newmesid in lstfollowers:
                    log(str(newmesid)+" is a follower")
                else:
                    log(str(newmesid)+" isnt a follower")
                    send_message(newmesid)
                    log("Gustavo sent!")
                    newmesid=0
                oldmesid=newmesid
            time.sleep(1)
        except LoginRequired:
            cl.relogin()
      
    log("Refreshing followers list")
    lstfollowers=get_followers(myselfid)
    pass
