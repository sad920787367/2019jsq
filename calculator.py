# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# from tkinter import *
# import tkinter
# top = tkinter.Tk()
# top.title('四王计算器1.0')
# numbers1 = [1,2,3]
# numbers2 = [4,5,6]
# numbers3 = [7,8,9]
# i=0
# for shu in numbers3:
#     i+=1
#     Button(top,text=shu).grid(row=100,column=i,sticky=W,padx=20,pady=15)
# i=0
# for shu in numbers2:  
#     i+=1
#     Button(top,text=shu).grid(row=200,column=i,sticky=W,padx=20,pady=15) 
# i=0
# for shu in numbers1:  
#     i+=1
#     Button(top,text=shu).grid(row=300,column=i,sticky=W,padx=20,pady=15)   
#             # number1.pack()
# # 进入消息循环
# # B = tkinter.Button(top, text ="点我")
# # B.pack()

# top.mainloop()




# from tkinter import *
# reset=True
# def buttonCallBack(event):
#   global label
#   global reset
#   num=event.widget['text']
#   if num=='C':
#     label1['text']="0"
#     label2['text']=''
#     return
#   if num in "=":
#     label2['text']=label1['text']
#     label1['text']=str(eval(label2['text']))
#     return
#   s=label1['text'] 
#   if s=='0' or reset==True:
#     s=""
#     reset=False
#   label1['text']=s+num
# #主窗口
# root=Tk()
# root.wm_title("四王计算器2.0")
# #显示栏
# label1=Label(root,text="0",font = ('楷体',30),background="green",anchor="e")
# label2=Label(root,text="",font = ('楷体',20),background="yellow",anchor="e")
# label1['width']=19
# label2['width']=27
# label1['height']=2
# label2['height']=2
# label1.grid(row=2,columnspan=4,sticky=W)
# label2.grid(row=1,columnspan=4,sticky=W)
# #菜单
# menu = Menu(root)
# root.config(menu=menu)#显示菜单
# filemenu = Menu(menu)
# menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="Open",command=open_help)
# filemenu.add_command(label="Save")
# filemenu.add_separator()
# filemenu.add_command(label="退出", command=root.quit)
# #按钮设置
# showText="789/456*123-0.C+"
# for i in range(4):
#   for j in range(4):
#     b=Button(root,text=showText[i*4+j],height=3,width=12)
#     b.grid(row=i+4,column=j)
#     b.bind("<Button-1>",buttonCallBack)
# showText="()"
# for i in range(2):
#     b=Button(root,text=showText[i],height=3,width=12)
#     b.grid(row=8,column=2+i)
#     b.bind("<Button-1>",buttonCallBack)
# b=Button(root,text="=",height=3)
# b.grid(row=8,columnspan=2,sticky="we")
# b.bind("<Button-1>",buttonCallBack)
# root.mainloop()


# from tkinter import *
# from math import *
# reset=True
# def buttonCallBack(event):
#   global label
#   global reset
#   try:
#     num=event.widget['text']
#     if num=='C':
#       label1['text']="0"
#       label2['text']=''
#       return
#     if num in "=":
#       label2['text']=label1['text']
#       label1['text']=str(eval(label2['text']))
#       return
#     if num == "←":
#       label1['text']=label1['text'][0:-1]
#       return
#     s=label1['text'] 
#     if s=='0' or reset==True:
#       s=""
#       reset=False
#     label1['text']=s+num
#   except:
#     label1['text']="ERROR"

# #主窗口
# root=Tk()
# root.wm_title("四王计算器3.0")
# #显示栏
# label1=Label(root,text="0",font = ('楷体',30),background="green",anchor="e")
# label2=Label(root,text="",font = ('楷体',20),background="yellow",anchor="e")
# label1['width']=19
# label2['width']=27
# label1['height']=2
# label2['height']=2
# label1.grid(row=2,columnspan=4,sticky=W)
# label2.grid(row=1,columnspan=4,sticky=W)
# #菜单
# menu = Menu(root)
# root.config(menu=menu)#显示菜单
# filemenu = Menu(menu)
# menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="Open")
# filemenu.add_command(label="Save")
# filemenu.add_separator()
# filemenu.add_command(label="退出", command=root.quit)
# #按钮设置
# img_o=PhotoImage(file="tt.gif")
# showText=['sin','cos','tan','←']
# for i in range(4):
#   b=Button(root,text=showText[i],compound='center',activebackground="blue",image=img_o,font = ('黑体',20),fg="blue")
#   b.grid(row=3,column=i)
#   b.bind("<Button-1>",buttonCallBack)
# showText="789/456*123-0.C+"
# for i in range(4):
#   for j in range(4):
#     b=Button(root,text=showText[i*4+j],height=3,width=12)
#     b.grid(row=i+5,column=j)
#     b.bind("<Button-1>",buttonCallBack)
# showText="()"
# for i in range(2):
#     b=Button(root,text=showText[i],height=3,width=12)
#     b.grid(row=9,column=2+i)
#     b.bind("<Button-1>",buttonCallBack)
# b=Button(root,text="=",height=3)
# b.grid(row=9,columnspan=2,sticky="we")
# b.bind("<Button-1>",buttonCallBack)
# root.mainloop()

from tkinter import *
from math import *
reset=True
def buttonCallBack(event):
  global label
  global reset
  try:
    num=event.widget['text']
    if num=='C':
      label1['text']="0"
      label2['text']=''
      return
    if num in "=":
      label2['text']=label1['text']
      label1['text']=str(eval(label2['text']))
      return
    if num == "←":
      label1['text']=label1['text'][0:-1]
      return
    s=label1['text'] 
    if s=='0' or reset==True:
      s=""
      reset=False
    label1['text']=s+num
  except:
    label1['text']="ERROR"

#主窗口
root=Tk()
root.wm_title("四王计算器2.0")
#显示栏
image_1=PhotoImage(file="display.gif")
label1=Label(root,text="0",font = ('楷体',31),background="yellow",anchor="e")
label2=Label(root,text="",font = ('楷体',20),anchor="e",compound='center',image=image_1)
label1['width']=14
#label2['width']=21
label1['height']=1
# label2['height']=1
label1.grid(row=2,columnspan=4,sticky=W)
label2.grid(row=1,columnspan=4,sticky=W)
#菜单
menu = Menu(root)
root.config(menu=menu)#显示菜单
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
#按钮设置
img_o=PhotoImage(file="button.gif")
showText=['sin','cos','tan','←']
for i in range(4):
  b=Button(root,text=showText[i],compound='center',activebackground="blue",image=img_o,font = ('黑体',20),fg="blue")
  b.grid(row=3,column=i)
  b.bind("<Button-1>",buttonCallBack)
showText="789/456*123-0.C+"
for i in range(4):
  for j in range(4):
    b=Button(root,text=showText[i*4+j],compound='center',image=img_o,font = ('黑体',20),fg="blue")
    b.grid(row=i+5,column=j)
    b.bind("<Button-1>",buttonCallBack)
showText="()=^"
for i in range(4):
    b=Button(root,text=showText[i],compound='center',image=img_o,font = ('黑体',20),fg="blue")
    b.grid(row=9,column=i)
    b.bind("<Button-1>",buttonCallBack)
# b=Button(root,text="=",compound='center',image=img_o,font = ('黑体',20),fg="blue")
# b.grid(row=9,columnspan=2,sticky="we")
# b.bind("<Button-1>",buttonCallBack)
root.mainloop()



# import math
# import wx
 
# class CalcFrame(wx.Frame):
 
#     def __init__(self,title):
#         super(CalcFrame, self).__init__(None, title = title, size = (300, 250))
#         self.InitUI()
#         self.Centre()
#         self.Show()
 
#     def InitUI(self):
#         vbox = wx.BoxSizer(wx.VERTICAL)#以列放置，文本框在最上方
#         self.textprint = wx.TextCtrl(self, style=wx.TE_RIGHT)
 
#         vbox.Add(self.textprint, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)      
#         gridBox = wx.GridSizer(5, 4, 5, 5)##行数，列数，垂直间隔，水平间隔
#         labels=['AC','DEL','PI','CLOSE','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
#         for label in labels: 
#             gridBox.Add(wx.Button(self,label = label), 1, wx.EXPAND)
 
#         vbox.Add(gridBox, proportion=1, flag=wx.EXPAND)
#         self.SetSizer(vbox)
 
# if __name__ == '__main__':
 
#     app = wx.App()
#     CalcFrame(title = 'Calculator')
#     app.MainLoop()