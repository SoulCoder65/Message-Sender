import requests #TO SEND REQUEST TO WEBSITE
import _json
from tkinter import *
from tkinter.messagebox import showerror,showinfo

#MESSAGE FUN. FOR SENDING SMS
def sendMessage(phone_no,message):
    url="https://www.fast2sms.com/dev/bulk"
    para_list={
    'authorization':'',
    'sender_id':'FSTSMS',
    'message':message,
    'language':'english',
    'route':'p',
    'numbers': phone_no
 }
    response=requests.get(url,params=para_list)
    dic=response.json()
    print(dic)
    return dic.get('return')

#THIS FUN. CALL AFTER USER CLICK ON SEND BTN
def onClick():
    num=numberInput.get()
    msg=msgInput.get("1.0",END)
    result=sendMessage(num,msg)
    print(result)
    if result:
        showinfo("SMS By AKSH","Message Sent Successfully")
    else:
        showerror("SMS By AKSH","Some Error Occured while Sending SMS")



#GUI
message_screen=Tk()
message_screen.title("Message By Akshay")
message_screen.geometry("400x550")
font=("Helvetica",22,"bold")
numberInput=Entry(message_screen,font=font)
numberInput.pack(fill=X,pady=20)

msgInput=Text(message_screen)
msgInput.pack(fill=X)
send_btn=Button(message_screen,text="Send SMS",command=onClick)
send_btn.pack()
message_screen.mainloop()