"""
@author: marcfusch
Thanks to adw0rd (for making this project possible)
Thanks to Silio for giving me this incredible idea at midnight.
"""
from instagrapi import Client
import time
cl = Client()
cl.set_locale('fr_FR')
cl.set_timezone_offset(1 * 60 * 60)

myself='***YOUR USERNAME***'
cl.login("***YOUR USERNAME***", "***YOUR PASSWORD***")
print("Login succesfull")

photo_path = 'gus.jpg'

def log(message):
    print(str(time.strftime("%H:%M:%S", time.localtime())) + " "+ message)

def get_followers(myselfid):
    mydict=cl.user_following(myselfid)
    L=[]
    for followingid in mydict.keys():
        L.append(int(followingid))
    if L:
        log("Followers list succesfully retrieved")
    else:
        log("Error while retrieving folllowers list. Maybe the account isn't yours...")
        log("The program will not run correctly!")
    return(L)
    pass

def sanitize(inputstr):
    direcstring=str(inputstr[0])
    L=direcstring.split(',')
    L=L[1].split('=')
    newmesid=int(L[1])
    return(newmesid)

def unread_to_userid():
    direct_pending=cl.direct_pending_inbox(1)
    if direct_pending:
        return(sanitize(direct_pending))
    direct_mainbox=cl.direct_threads(1,"unread")
    if direct_mainbox:
        return(sanitize(direct_mainbox))
    else:
        return(0)

def send_message(scammerid):
    cl.direct_send_photo(photo_path, user_ids=[scammerid])
    pass


log("Getting your account id")
myselfid=cl.user_id_from_username(myself)

log("Getting followers from user: "+ myself)
lstfollowers=get_followers(myselfid)
oldmesid=0
newmesid=unread_to_userid()

while True:
    for i in range(50):
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
    #log("Actualising login")
    #cl.relogin()
    log("Actualising followers list")
    lstfollowers=get_followers(myselfid)
    pass
