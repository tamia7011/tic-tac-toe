from tkinter import *

def victory() :
	msg = Message(window, text="You victiory!")
	msg.grid(row=3, column=1)

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"

      row = i//3
      col = i%3

      if list[row*3]["text"] == list[row*3+1]["text"] == list[row*3+2]["text"] :
            victory()
      elif list[col]["text"] == list[col+3]["text"] == list[col+6]["text"] :
            victory()
      elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     " or list[2]["text"] == list[4]["text"] == list[6]["text"] != "     " :
            victory()

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()
