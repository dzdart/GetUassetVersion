import os
import re
while 1:
    file=input("将文件拖入这儿然后回车！")
    if file.endswith(".uasset"):
        new_data=""
        data=open(file,"rb")
        for i in range(3200):
            try:
                new_data+=str(data.read(i),encoding="utf-8")
            except:
                pass
        index=new_data.find("UE")
        info=new_data[index-20:index+20]
        info.replace(" ",'')
        info=re.sub(u"([^\u0041-\u005a\u0061-\u007a\u0030-\u0039])", "", info)
        print("该文件相关版本信息如下\n",info)
    else:
        print("务必放入正确的uasset文件！")
