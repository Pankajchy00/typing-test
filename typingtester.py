DOINGwords = ['mango','laptop','this','ram','Apple','graps','tiger','linc','thakur','skit','For','ten','years','his','land','is','left','vacant','and if','everybody','starts','doing',
'same','thing then there is shortage','of labourers because','of shortage','labourers','interested','doing','job such issues','will be there']

def labelSlider():
    global count,sliderWords
    text ='Welcome to typing Speed Increaser Game'
    if(count >= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150,labelSlider)


def time():
    global timeleft,score,miss
    if(timeleft >= 11):
        pass
    else:
        timeLabelCount.configure(fg='red')
    if(timeleft>0):
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gameplayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notification','For Play Again Hit Retry Bottan')
        if(rr==True):
            score = 0
            timeleft = 60
            miss = 0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
def startGame(event):
    global score,miss
    if(timeleft == 60):
        time()
    gameplayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)



from tkinter import*
import random
from tkinter import messagebox

################################ Root Method
root = Tk()
root.geometry('800x600+200+50')
root.configure(bg='powder blue')
root.title('Typing speed Incresser Game')
###############################Variables
score = 0
timeleft = 60
count = 0
sliderWords = ''
miss = 0

################################ Label Methods
fontLabel = Label(root,text='',font=('airal',25,'italic bold'),bg='powder blue',fg='red',width=40)
fontLabel.place(x=10,y=10)
labelSlider()

random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('airal',40,'italic bold'),bg='powder blue')
wordLabel.place(x=300,y=200)

scoreLabel = Label(root,text='your score :',font=('airal',25,'italic bold'),bg='powder blue')
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root,text=score,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scoreLabelCount.place(x=80,y=150)

timerLabel = Label(root,text='time left :',font=('airal',25,'italic bold'),bg='powder blue')
timerLabel.place(x=600,y=100)

timeLabelCount = Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timeLabelCount.place(x=650,y=150)


gameplayDetailLabel = Label(root,text='Type Word And Hit Enter Button',font=('arial',30,'italic bold'),
                             bg='powder blue',fg='grey')
gameplayDetailLabel.place(x=120,y=450)
################################Entery method
wordEntry = Entry(root,font=('airal',25,'italic bold'),bg='white',bd=10,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()
#######################################
root.bind('<Return>',startGame)

root.mainloop()
