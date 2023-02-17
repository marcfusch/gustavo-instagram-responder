# hidenseek-gustavo-instagram
Python script that automatically sends Hide n Seek Gustavo meme to untrusted people

## Install process:
First you need the instagrapi form adword
```
git clone https://github.com/adw0rd/instagrapi
cd instagrapi
python setup.py install
```
Then, you need to configure the script with your Instagram credentials.
You will need to modify line 12 and 13 that are:
```
myself='***YOUR USERNAME***'
cl.login("***YOUR USERNAME***", "***YOUR PASSWORD***")
```

## Running the script
You are now ready to run the script
```
python gustavo.py
```

## Additional notes
If you want to use another follower list, it is possible. just set the variable myself to the account you wish to get the followers list from.
Moreover, if you plan to use another image to respond to untrusted people, you can just change gustavo.jpg by another jpeg image.
