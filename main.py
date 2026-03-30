# Shakespeare Sentiment Analysis
# Rule-based NLP system
# Author: Harshit Jain


#Block-1 Intoducing variables
positive_words=["powerful","shine","bright","living","memory","praise","room","posterity","arise","live","dwell","lovers"]#List of positive words
negative_words=["unswept","besmeared","sluttish","wasteful","war","overturn","broils","fire","burn","death","enmity","oblivious","doom"]#List of negative words
sentiment=0
lower_list=[]

#Block2-Opening files
txt=open("H:\Assignment-2-Sentiment-Analysis-using-Shakespeare\sonet.txt","r")#Opening the text file containing the sonet
output=open("H:\Assignment-2-Sentiment-Analysis-using-Shakespeare\output.txt","w")#Opening the text file to store output in

#Block3-Preprocessing on given sonet
txt_list=txt.readlines()#braking text into lines
for line in txt_list:
    line=line.lower()#Lowercasing 
    split_list=line.split()#Breaking into individual words
   
    #Block4-Assigning sentiment value
    for word in split_list:
        if word in positive_words:#Chechking if word is positive 
            sentiment+=1
        if word in negative_words:#Chechking if word is negative 
            sentiment-=1

    #Block5-Writting output
    if sentiment>0:#Checking sentiment value of respective line
        output.write(f"line={i},sentiment=positive\n")#Storing line and sentiment in output.txt file
    if sentiment<0:#Checking sentiment value of respective line
        output.write(f"line={i},sentiment=negative\n")#Storing line and sentiment in output.txt file
    if sentiment==0:#Checking sentiment value of respective line
        output.write(f"line={i},sentiment=neutral\n")#Storing line and sentiment in output.txt file
    sentiment=0#resetting sentiment value for eachrespective line

#Block6-Closing files
txt.close()#Closing text file containing sonet
output.close()#Closing text file containing output
