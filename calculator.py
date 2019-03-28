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
#定义两个标志初始值设为True
reset=True
second=True
def buttonCallBack(event):
  global label
  global reset
  global second
  try:
    num=event.widget['text']  #num用来保存此次点击事件的文本
    if num=='C':    #清屏设置
      label1['text']="0"
      label2['text']=''
      return
    if num in "=":   #等于号输出结果，使用eval函数进行计算，结果输出在label1上
      label2['text']=label1['text']
      label1['text']=str(eval(label1['text']))
      reset=True
      second=True
      return
    if num == "←":     #退位键，用切片的方式舍掉label1的最后一位
      label1['text']=label1['text'][0:-1]
      return
    s=label1['text']   #s是用来存储按下按钮前label1的内容
    if s=='0':
      s='' 
    if second==False and num in "+-*/":
      num=""
    if num in "'sin','cos','tan','sqrt'":  #三角函数和开平方使用后自动加上左括号
      num=num+"("
      reset=False
    if num in "0,1,2,3,4,5,6,7,8,9,0":
      second=True
    if second==True and num in "+-*/":
      reset=False
      second=False
    if reset==True and num in "0,1,2,3,4,5,6,7,8,9,'sin','cos','tan','sqrt'":
      s=""
      reset=False
    label1['text']=s+num   #将按下按钮前的label内容和此次点击的文本进行连接
  except:
    label1['text']="ERROR"
#主窗口
root=Tk()
root.wm_title("四王计算器4.0")
#用grid进行按钮和显示框的布局，row为行，column为列
#在Label（）和Button（）中是按钮和显示框的基本属性，其上显示文本就是用text来操作的
#显示栏
image_1=PhotoImage(file="display.gif")  #打开图片，以备使用
label1=Label(root,text="0",font = ('楷体',20),background="yellow",anchor="e",width=21,height=2)
label2=Label(root,text="",font = ('楷体',15),anchor="e",compound='center',image=image_1)
label1.grid(row=2,columnspan=4,sticky=W)
label2.grid(row=1,columnspan=4,sticky=W)
#按钮设置
img_o=PhotoImage(file="button.gif")  #打开图片，以备使用
showText=['sin','cos','tan']
for i in range(3):
  b=Button(root,text=showText[i],compound='center',activebackground="blue",image=img_o,font = ('黑体',20),fg="blue")
  b.grid(row=3,column=i)
  b.bind("<Button-1>",buttonCallBack)
b=Button(root,text="sqrt",compound='center',image=img_o,font = ('黑体',18),fg="blue")
b.grid(row=3,column=3)
b.bind("<Button-1>",buttonCallBack)
showText="789/456*123-0←C+().="
for i in range(5):
  for j in range(4):
    b=Button(root,text=showText[i*4+j],compound='center',image=img_o,font = ('黑体',20),fg="blue")
    b.grid(row=i+5,column=j)
    b.bind("<Button-1>",buttonCallBack)
root.mainloop()
