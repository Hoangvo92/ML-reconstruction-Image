import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from predict.predictTR import *
from predict.predictTE import *
from reconstruct.reconstructImage import *
from reconstruct.test import *

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
        
master = Tk()
master.title("MRI Reconstruction- Hoang Vo")
#app = MainWindow(master)
master.geometry("250x50")
#master.iconbitgmap("ML-reconstruction-Image/")

def open():
    global first_image
    global myImage
    global image1
    
    #first_image.grid_forget()
    btn_add_noise.grid_forget()

    btn_reconstruct.grid_forget()
   
    btn_parameters.grid_forget()
    master.filename = filedialog.askopenfilename(initialdir="data", title="Select A File", filetypes=(("png files", "*.png"),("all files", "*.*")))
    top = Toplevel()
    top.title("Chosen Image")
    myLabel = Label(master, text = master.filename)#.pack()
    #print(myLabel)
    #processing image in here
   #https://stackoverflow.com/questions/52558118/how-to-display-multiple-images-inside-tkinter-window
    image = Image.open(master.filename)
   # resized = myImage.resize((300,300),Image.ANTIALIAS)
    myImage = ImageTk.PhotoImage(Image.open(master.filename))#.resize((300,300),Image.ANTIALIAS))
    #tk_image = ImageTk.PhotoImage(myImage)
           
    first_image = Label(top, image= myImage)#.pack()
    first_image.grid(row=0, column=0, columnspan=2)
    #btn2 = Button(top, text="Add Noise").pack() #, command = top.destroy)
    #btn2.grid(row=1, column= 0)
    btn_add_noise.grid(row=0, column= 1)
    
def noise_image():
    global second_image
    global noiseImage
    global image1
    global image2
    btn_add_noise.grid_forget()

    btn_reconstruct.grid_forget()
   
    btn_parameters.grid_forget()
    #first_image.grid_forget()
    top = Toplevel()
    top.title("Noise Image")
    
    image = Image.open("testing/test.png")
    # do noise
   # resized = myImage.resize((300,300),Image.ANTIALIAS)
    noiseImage = ImageTk.PhotoImage(image)#.resize((300,300),Image.ANTIALIAS))
    #tk_image = ImageTk.PhotoImage(myImage)
           
    second_image = Label(top, image= noiseImage)#.pack()
    second_image.grid(row=0, column=0, columnspan=2)
    btn_reconstruct.grid(row=0, column=2)


def reconstruct_image():
    global third_image
    global reconstructImage
    global image2
    global image3
    btn_add_noise.grid_forget()

    btn_reconstruct.grid_forget()
   
    btn_parameters.grid_forget()
    #first_image.grid_forget()
    top = Toplevel()
    top.title("Reconstruct Image")
    
    image = Image.open("testing/test.png")
    # do noise
   # resized = myImage.resize((300,300),Image.ANTIALIAS)
    noiseImage = ImageTk.PhotoImage(image)#.resize((300,300),Image.ANTIALIAS))
    #tk_image = ImageTk.PhotoImage(myImage)
           
    second_image = Label(top, image= noiseImage)#.pack()
    second_image.grid(row=0, column=0, columnspan=2)
    btn_parameters.grid(row=0, column=3)

def predictValue():
    global third_image
    global reconstructImage
    global image2
    global image3
    btn_add_noise.grid_forget()

    btn_reconstruct.grid_forget()
   
    btn_parameters.grid_forget()
    #first_image.grid_forget()
    top3 = Toplevel()
    top3.geometry("100x250")
    top3.title("Values of TR and TE")
    

    #################
    #generate TR and TE in prediction
    test()
    TR = "5"
    TE = "2"
      # Create text widget and specify size.
    p1 = Label(top3, text= f"TR : {TR}", foreground="black")
    p2 = Label(top3, text= f"TE : {TE}", foreground="black")
    p1.grid(row=0, column= 0, columnspan=3)
    p2.grid(row=1, column= 0, columnspan=3)
    
  

  
   

#image1 = ImageTk.PhotoImage(Image.open("testing/test.png").resize((300,300),Image.ANTIALIAS))
#first_image = Label(image = image1 )
#first_image.grid(row=0, column=0, columnspan=2)
#second_image = Label(image = image1)
#second_image.grid(row=0, column=2, columnspan=2)
#third_image = Label(image = image1)
#third_image.grid(row=0, column=4, columnspan=2)
                
                  
btn_open =  Button(master, text= "Open File" , command = open) #.pack()

btn_add_noise = Button(master, text ="Add Noise", command= noise_image)
btn_reconstruct = Button(master, text="Reconstruct Image", command=reconstruct_image)
btn_parameters = Button(master, text="Predict Values", command=predictValue)



btn_open.grid(row = 0, column= 0)
btn_add_noise.grid(row=0, column= 1)
btn_add_noise.grid_forget()
btn_reconstruct.grid(row=0, column=2)
btn_reconstruct.grid_forget()
btn_parameters.grid(row=0, column =3)
btn_parameters.grid_forget()
    
master.mainloop()
#app.mainloop()


#for noise pop up image
#top = Toplevel()
#top.title("Noise Image")
#noise_image = ImageTk.PhotoImage("noise image.png")
#noise_label = Label(top, image= noise_image).pack()
#btn2 = Button(top, text="Destroy", command = top.destroy)





#https://www.youtube.com/watch?v=YXPyB4XeYLA
#https://stackoverflow.com/questions/23584325/cannot-use-geometry-manager-pack-inside