# Shakespeare Sentiment Analysis
# Rule-based NLP system
# Author: Harshit Jain


#Block-1 Introducing variables
positive_words=["powerful","shine","bright","living","memory","praise","room","posterity","arise","live","dwell","lovers"]#List of positive words
negative_words=["unswept","besmeared","sluttish","wasteful","war","overturn","broils","fire","burn","death","enmity","oblivious","doom"]#List of negative words
sentiment=0

#Block2-Opening files
txt=open("sonnet.txt","r")#Opening the text file containing the sonnet in read mode
output=open("output.txt","w")#Opening the text file to store output in write mode

#Block3-Preprocessing on given sonet
txt_list=txt.readlines()#Breaking text into lines
for line in txt_list:
    line=line.lower()#Lowercasing 
    words=line.split()#Breaking into individual words
   
    #Block4-Assigning sentiment value
    for word in words:
        if word in positive_words:#Checking if word is positive 
            sentiment+=1
        elif word in negative_words:#Checking if word is negative 
            sentiment-=1

    #Block5-Writting output
    if sentiment>0:#Checking sentiment value of respective line
        output.write(f"line:{line}sentiment:positive\n")#Storing line and sentiment in output.txt file
    elif sentiment<0:#Checking sentiment value of respective line
        output.write(f"line:{line}sentiment:negative\n")#Storing line and sentiment in output.txt file
    elif sentiment==0:#Checking sentiment value of respective line
        output.write(f"line:{line}sentiment:neutral\n")#Storing line and sentiment in output.txt file
    sentiment=0#resetting sentiment value for each respective line

#Block6-Closing files
txt.close()#Closing text file containing sonnet
output.close()#Closing text file containing output
