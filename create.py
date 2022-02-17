import hashlib
import os
import shutil

def create(user, src):
    index = hashlib.md5(user.encode()).hexdigest()
    os.mkdir("site/"+ index)
    shutil.copytree("site/copy/access", "site/" + index  + "/access")
    shutil.copy("site/copy/index.html", "site/" + index + "/")
    shutil.copy("site/copy/manifest.json", "site/" + index + "/")
    shutil.copy("site/copy/sign.png", "site/" + index + "/")
    shutil.copy("done/" + src, "site/" + index + "/photo.jpg")
    shutil.copy("data/" + user + ".json", "site/" + index + "/config.json")
    shutil.copy("site/copy/get.php", "site/" + index + "/")
    
    return(index)
    
