import zipfile
import time 
folderpath =input("Path to the file")
zipf = zipfile.ZipFile(folderpath)
global result
result=0
global tried
tried=0
c=0
if not zipf:
    print("The zipped file/folder is not password protected! You can open it!")


if (result ==0):
    print("Sorry, password not found. A total of "+str(c)+"possible combinations tried in"+str(duration)+"seconds. Password is of 4 characters"

else:
    duration = endtime-startime
    print("Congratulations!!! Password found after trying "+str(duration)+"seconds")


else:
    startime=time.time()
    wordListFile = open("wprdlist.txt","r",errors="ignore")
    body = wordListFile.read().lower()
    words = body.split("\n")

for i in range(len(words)):
    word = words(i)
    password=word.emcode("utf8").strip()
    c=c+1
    print("trying to deode password by: {}".format(word))
    try:
        with zipfile.ZipFile(folderpath,"r") as zf:
            zf.extractall(pwd=password)
            print("Success! The password is:"+word)
            endtime =time.time()
            result = lenbreak

        break
    except:


    