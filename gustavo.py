"""
@author: marcfusch
Thanks to adw0rd (for making this project possible)
Thanks to Silio for giving me this incredible idea at midnight.
"""

from instagrapi import Client
import time

cl = Client()

myself='***YOUR USERNAME***'
cl.login("***YOUR USERNAME***", "***YOUR PASSWORD***")
print("Login succesfull")

photo_path = 'gus.jpg'

def get_followers(myself):
    myselfid=cl.user_id_from_username(myself)
    mydict=cl.user_following(myselfid)
    L=[]
    for followingid in mydict.keys():
        L.append(int(followingid))
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

  
print("Getting followers from user: "+ myself)
lstfollowers=get_followers(myself)
if lstfollowers:
    print("Followers list succesfully retrieved")
else:
    print("Error while retrieving folllowers list. Maybe the account isn't yours...")
    print("The program will not run correctly!")

oldmesid=0
newmesid=unread_to_userid()
while True:
    if  newmesid==0 or newmesid==oldmesid:
        print("No unread messages")
        newmesid=unread_to_userid()
    else:
        print("New activity from user: " + str(newmesid))
        if newmesid in lstfollowers:
            print(str(newmesid)+" is a follower")
        else:
            print(str(newmesid)+" isnt a follower")
            send_message(newmesid)
            print("Gustavo sent!")
            newmesid=0
        oldmesid=newmesid
    time.sleep(1)
    pass

