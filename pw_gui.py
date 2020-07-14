import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pw_gen as pw
from pw_gen import caesar,pw_generate,Encryptor

#key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
#clear = lambda: os.system('clear')

def gui_app():

    root= tk.Tk()
    root.title("Encryption App")
    root.resizable(width=FALSE,height = FALSE)
    
    canvas = tk.Canvas(root,height=500,width=600)
    canvas.pack()


    #background image
    bg_img= tk.PhotoImage(file='/Users/nickku/code/Python/pw_enc_dec/background.png')
    img_label=tk.Label(root,image=bg_img)
    img_label.place(relwidth=1,relheight=1)

    #frame
    frame = tk.Frame(root,bg="ivory3")
    frame.place(relwidth=0.8,relheight=0.8,relx=0.1 ,rely=0.1)
    
    #title
    header = tk.Label(root,text="Caesar/AES",width=43,bg="firebrick3")
    header.config(font=("Courier bold",18))
    header.place(relx = 0.10,rely=0.03)


    #input for key value
    key_label = Text(frame,height=1,width=9,bg="ivory3",highlightthickness = 0)
    key_label.insert(INSERT,"Key Value")
    key_label.place(relx=0.04,rely=0.10)

    keyVar = StringVar()
    key = Entry(frame,width=3,textvariable=keyVar)
    key.place(relx=0.20,rely=0.09)

    # CAESAR ENCRYPTION
    toEnc = StringVar()
    enc = Entry(frame,highlightbackground="red",width=38,textvariable= toEnc)
    enc.place(relx=0.20,rely=0.25)
   
    
   
    def encrypt_cmd():
        try:
            res = caesar(enc.get(),'encrypt',int(key.get()))
            enc_label['text'] = res
            enc_label['bg'] = "tomato3"
        
        except:
            print("error")
           # messagebox.showerror("KeyError","Insert Key Value")
       
    
    enc_btn = tk.Button(frame,text="Encrypt",padx=5,pady=5, fg="red", command= encrypt_cmd)
    enc_btn.place(relx=0,rely=0.25)

    enc_label = tk.Label(frame,bg="ivory3",width=51)
    enc_label.place(relx=0.02,rely=0.40)

    

    #CAESAR DECRYPTION

    toDec = StringVar()
    dec= Entry(frame,highlightbackground="red",width = 38,textvariable=toDec)
    dec.place(relx=0.20,rely=0.55)

    def decrypt_cmd():
        try:
            res = caesar(dec.get(),'decrypt',int(key.get()))
            dec_label['text'] = res
            dec_label['bg'] = "SpringGreen3"
        except:
            messagebox.showerror("KeyError","Insert Key Value")


    dec_btn = tk.Button(frame,text="Decrypt",padx=5,pady=5,fg="red",command= decrypt_cmd)
    dec_btn.place(relx=0,rely=0.55)

    dec_label = tk.Label(frame,bg="ivory3",width=51)
    dec_label.place(relx=0.02,rely=0.70)

    #RESET Button
    def reset():
        toEnc.set(" ")
        toDec.set(" ")
        keyVar.set(" ")
        dec_label['text']= " "
        enc_label['text']= " "

    ButtonReset = Button(frame, text="Reset",command=reset,borderwidth=0,fg="firebrick3")
    ButtonReset.place(relx=0.50,rely=0.84)

    root.mainloop()

    

gui_app()
