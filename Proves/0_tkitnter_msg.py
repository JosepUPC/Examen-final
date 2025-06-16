## funcio bàsica per tal d'enviar unes questions, els primer program que faré

import tkinter.messagebox as msg

varMdg= msg.askquestion("titol","el missatge que es vol enviar",detail="detall del missatge",icon="question",type="yesno")

if varMdg == "yes":
    msg.showinfo("titol","el missatge que es vol enviar",detail="detall del missatge",icon="info")
else:
    msg.showwarning("titol","el missatge que es vol enviar",detail="detall del missatge",icon="warning")