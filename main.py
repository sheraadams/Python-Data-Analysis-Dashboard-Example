import pandas as pd
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

fore = "white"
back = "black"
window = tk.Tk()
window.configure(bg="white")
window.title("Dashboard")
window.geometry('900x800')
top= tk.Frame(window)
top.pack(side="top")
bottom = tk.Frame(window)
bottom.pack(side="bottom")

text_file = r"socialmedia.txt"
inputname = "socialmedia.dat"   #save csv as file
# create empty lists used to count occurrence  of words
list = []
# create  empty list with  to store unique words
new_list = []
# create dictionary to assist with assigning values to items for reference later
dict1 ={}
lowercaseDict = {}
uniqueWordsDict = {}
import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  

# read text file
with open(text_file, 'r') as myfile:
    datfile = myfile.readlines()
    for row in datfile:
        uniqueWordsDict[row.strip()] = uniqueWordsDict.get(row.strip(), 0) + 1
        row.split(' ')
        # append each word to empty list "list" for counting occurrences
        list.append(row.strip("\n"))
        for word in list:
            freq = list.count(word)
            # add word as key and frequency as value for our file reference dictionary
            dict1.update({word:freq})
            lowercaseDict.update({word.lower():freq})
myfile.close()

# write the dat file
with open(inputname, 'w') as outFile:
    for key, value in sorted(uniqueWordsDict.items()):
        stringOut = key + " " + str(value)
        outFile.write(stringOut + "\n")
        # close the files


# method and menu item 3 print a histogram for each item with asterisks denoting the number of items purchased
def getHistogram():
    for key, value in dict1.items():
        print(key, "(", end ='')
        print(value, end=') ')
        for i in range(value):
            print ("*", end='')
        print('')
    print(dict1)

#  menu item 1 prints full dictionary as a list of all inventory items.
def inventoryFunc():
    for k, v in dict1.items():
        print(k, v)


# plot
with open('socialmedia.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))
plt.plot(x, y, color='purple', linestyle='dashed',
         marker='o', label="Social Media Data")
plt.xticks(rotation=25)
plt.xlabel('Social Media Usage')
plt.ylabel('Visits')
plt.title('Social Media Usage Report', fontsize=14)
plt.grid()
plt.legend()
plt.savefig("plot.png", format="png")


# create pie chart
with open('socialmedia.csv', 'r') as csvfile:
    x2 = []
    y2 = []
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x2.append(row[0])
        y2.append(int(row[1]))
plt.xlabel('')
plt.ylabel('')
plt.pie(y2, labels=x2, autopct='%.2f%%')
plt.title('Social Media Usage Report', fontsize=14)
plt.savefig("pie.png", format="png")

# create histogram
data = pd.read_csv('socialmedia.csv', sep=',',header=None, index_col =0)
data.plot(kind='bar')
plt.ylabel('Visits')
plt.xticks(rotation= 20, ha='right')
plt.xlabel('Socia Media')
plt.title('Social Media Usage Report', fontsize=14)
plt.savefig("hist.png", format="png")


# create gui
label = Label(window, fg=back, text="Dashboard", anchor="n")
lab = Label(window, bg= fore, fg= back, font='Arial 17 bold', text="Social Media Usage Dashboard", pady=8)
lab.pack()
label2=Label(window, bg= fore, fg= back, text="Over one week the usage of eight social media sites were tracked according to total number of site visits. The most used social media sites were GitHub and YouTube which both averaged 48 views daily. Instagram was the second most viewed site with 33 daily views. ", font=('Arial 9'), width=800, height=3, wraplength=800, justify = "left")
label2.pack()

label = Label(window, fg=back, text="Dashboard", anchor="n")
lab = Label(window, bg= fore, fg= back, font='Arial 1 bold', text="", pady=8)
lab.pack()
#path = '3.png'
#img0 = ImageTk.PhotoImage(Image.open(path))
#panel = tk.Label(window, bg="white", fg="white", image=img0, borderwidth=0, highlightthickness=0)
#panel.image = img0
#panel.pack()

# gui image for pie chart
image=Image.open('pie.png')
img=image.resize((400, 300))
my_img=ImageTk.PhotoImage(img)
label=Label(window, image=my_img)
label.pack()

# gui image for plot chart
image1=Image.open('plot.png')
img1=image1.resize((400, 300))
my_img1=ImageTk.PhotoImage(img1)
panel=Label(window, image=my_img1)
panel = tk.Label(window, bg=fore, fg=fore, image=my_img1)
panel.image = img1
panel.pack(side="left", fill="both", expand="yes")

# gui image for hist chart
image2=Image.open('hist.png')
img2=image2.resize((400,300))
my_img2=ImageTk.PhotoImage(img2)
panel1=Label(window, image=my_img2)
panel1 = tk.Label(window, bg=fore, fg=fore, image=my_img2)
panel1.image = img2
panel1.pack(side="right", fill="both", expand="yes")



getHistogram()
window.mainloop()
