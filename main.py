positive_words=["powerful","shine","bright","living","memory","praise","room","posterity","arise","live","dwell","lovers"]
negative_words=["unswept","besmeared","sluttish","wasteful","war","overturn","broils","fire","burn","death","enmity","oblivious","doom"]
sentiment=0
lower_list=[]
txt=open("H:\Assignment-2-Sentiment-Analysis-using-Shakespeare\sonet.txt","r")
output=open("H:\Assignment-2-Sentiment-Analysis-using-Shakespeare\output.txt","w")
txt_list=txt.readlines()
for i in txt_list:
    i=i.lower()
    split_list=i.split()
    for j in split_list:
        if j in positive_words:
            sentiment+=1
        if j in negative_words:
            sentiment-=1
    if sentiment>0:
        output.write(f"line={i},sentiment=positive\n")
    if sentiment<0:
        output.write(f"line={i},sentiment=negative\n")
    if sentiment==0:
        output.write(f"line={i},sentiment=neutral\n")
    sentiment=0