# hidenseek-gustavo-instagram
Python script that automatically sends Hide n Seek Gustavo meme to untrusted people

## Install process:
First you need the instagrapi form adword
```
git clone https://github.com/adw0rd/instagrapi
cd instagrapi
python setup.py install
```
As well as a special version of the googletranslate api
```
pip3 uninstall googletrans                                                                                              pip3 install googletrans==3.1.0a0
```

After that, clone the script from this repo:

```
git clone https://github.com/marcfusch/hidenseek-gustavo-instagram
cd hidenseek-gustavo-instagram
```
Then, you need to configure the script with your Instagram credentials.
You will need to modify those lines:
```
username='YOUR_USERNAME'
password='YOUR_PASSWORD'
```

## Running the script
You are now ready to run the script
```
python gustavo.py
```

## Additional notes
If you want to use another follower list, it is possible. just set the variable myself to the account you wish to get the followers list from.
Moreover, if you plan to use another image to respond to untrusted people, you can just change gus.jpg by another jpeg image.

### In case of frequent crashes:
Since this bot is still in development, you may encounter crashes throughout it's use.
You can always run the script like this:

```
while True; do {python gustavo.py}; done
```


## Credits:
Thanks to @adw0rd for creating instagrapi,to @ssut for creating the Google translate API, to @jacebrowning for creating memegen and Silio for this incredible idea
