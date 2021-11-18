import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

import sys
import math
import random

#GUI_reconstruct_mri_tk_HV.py



#class MainWindow(tk.Frame):
#
 #   def __init__(self, master = None):
  #      super().__init__(master)
   #     self.pack()
   #      ''' Step 1: Initialize the Qt window '''
    #    self.master.title("MRI Reconstruction- Hoang Vo")
     #   #https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/
    #    self.master.geometry("1000x500")
        
     #   self.master.grid_rowconfigure(0, weight=1)
      #  self.master.grid_columnconfigure(0, weight=1)
       # ''' Step 1: Initialize the Qt window '''
 
        

        
        #''' Step 3: Add the control panel to the right hand side of the central widget '''
 
                
      #https://www.youtube.com/watch?v=Aim_7fC-inw
      #https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
        
master = tk.Tk()
master.title("MRI Reconstruction- Hoang Vo")
#app = MainWindow(master)
master.geometry("1000x500")
#master.iconbitgmap("ML-reconstruction-Image/")

def open():
    global myImage
    
    master.filename = filedialog.askopenfilename(initialdir="data", title="Select A File", filetypes=(("png files", "*.png"),("all files", "*.*")))
                  
    myLabel = Label(master, text = master.filename).pack()
    print(myLabel)
    #processing image in here
   #https://stackoverflow.com/questions/52558118/how-to-display-multiple-images-inside-tkinter-window
    myImage = ImageTk.PhotoImage(Image.open(master.filename))
                  
    myImageLabel = Label(image=MyImage).pack()

image1 = ImageTk.PhotoImage(Image.open("testing/test.png"))
first_image = Label(image = image1 )
first_image.grid(row=0, column=0, columnspan=4)
second_image = Label(image = image1)
second_image.grid(row=1, column=0, columnspan=4)
third_image = Label(image = image1)
third_image.grid(row=2, column=0, columnspan=4)
                
                  
btn_open =  Button(master, text= "Open File" , command = open) #.pack()

btn_add_noise = Button(master, text ="Add Noise")
btn_reconstruct = Button(master, text="Reconstruct Image")
btn_parameters = Button(master, text="Predict Values")



btn_open.grid(row = 3, column= 0)
btn_add_noise.grid(row=3, column= 1)
btn_reconstruct.grid(row=3, column=2)
btn_reconsctruct.grid(row=3, column =3)
    
master.mainloop()
#app.mainloop()
