from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
#from PIL import ImageTk,Image
bot=ChatBot("My Bot")
convo= [
    'hello',
    'hi there !',
    'what is your name ?',
    'my name is Superman, and Sudip is my best friend',
    'where do you live?',
    'i live in Gotham',
    'what do you like?',
    'i like helping people',
    'do you like Sudip?',
    'yes,absolutely, he is the only man who can beat me but is so humble too',
    'how are you?',
    'i am doing great,although i wish Sudip was here'
]
trainer=ListTrainer(bot)
trainer.train(convo)

main= Tk()
main.geometry("500x650")
main.title("Superman")

def ask_from_bot():
    #print("clicked")
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"you : " +query)
    msgs.insert(END, "Superman :" +str(answer_from_bot))
    textF.delete(0,END)


frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Send Message",font=("Verdana",20),command=ask_from_bot)
btn.pack();


main.mainloop()
