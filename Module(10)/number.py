
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
ones={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',11:'eleven'}
tens={0:"",1:'ten',2:'twenty',3:'thirty',4:'four',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}                  
value=list(map(int,input("Enter the number: ").split(" ")))

for x in range(len(value)):	
  if(value[0]==0): del(value[0])
  
 
if (len(value)>4): exit()
rr=len(value)
suffix=""
name=[]
for x in range(len(value)):
  initial=value[x]
  if(rr==4):
   word=ones[initial]+' thousand'
   name.append(word)
  if(rr==3): 
   if(initial!=0):suffix=' hundred and'
   word=ones[initial]+suffix
   name.append(word)
  if(rr==2): 
   if(value[x+1]==1 and initial==1):
    name.append(ones[11])
    break
   word=tens[initial]
   name.append(word)
  if(rr==1):
   word=ones[initial]
   name.append(word)
  rr=rr-1
 
aaa=(" ".join(name))
print(aaa)
speaker.Speak(aaa)


	
	                                                                           