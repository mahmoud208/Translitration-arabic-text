# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
import codecs
import string

aro=[]
l=[]
l2=[]
x=0
c=0
try:
     words=codecs.open("in.txt","r","utf-8")
     words= words.read()
     words=words[0:]

finally:

    pass



try:
   for s in words:
    x=0
#-----------------letters---------------
    if s == unicode("ا","utf-8"):
       aro.append("A")
       x=1
    if s == unicode("أ","utf-8"):
       aro.append("<")
       x=1
    if s == unicode("ب","utf-8"):
       aro.append("b")
       x=1
    if s == unicode("ت","utf-8"):
       aro.append("t")
       x=1
    if s == unicode("ث","utf-8"):
       aro.append("v")
       x=1
    if s == unicode("ج","utf-8"):
       aro.append("j")
       x=1
    if s == unicode("ح","utf-8"):
       aro.append("H")
       x=1
    if s == unicode("خ","utf-8"):
       aro.append("x")
       x=1
    if s == unicode("د","utf-8"):
       aro.append("d")
       x=1
    if s == unicode("ذ","utf-8"):
       aro.append("*")
       x=1
    if s == unicode("ر","utf-8"):
       aro.append("r")
       x=1
    if s == unicode("ز","utf-8"):
       aro.append("z")
       x=1
    if s == unicode("س","utf-8"):
       aro.append("s")
       x=1
    if s == unicode("ش","utf-8"):
       aro.append("$")
       x=1
    if s == unicode("ص","utf-8"):
       aro.append("S")
       x=1
    if s == unicode("ض","utf-8"):
       aro.append("D")
       x=1
    if s == unicode("ط","utf-8"):
       aro.append("T")
       x=1
    if s == unicode("ظ","utf-8"):
       aro.append("Z")
       x=1
    if s == unicode("ع","utf-8"):
       aro.append("E")
       x=1
    if s == unicode("غ","utf-8"):
       aro.append("g")
       x=1
    if s == unicode("ف","utf-8"):
       aro.append("f")
       x=1
    if s == unicode("ق","utf-8"):
       aro.append("q")
       x=1
    if s == unicode("ك","utf-8"):
       aro.append("k")
       x=1
    if s == unicode("ل","utf-8"):
       aro.append("l")
       x=1
    if s == unicode("م","utf-8"):
       aro.append("m")
       x=1
    if s == unicode("ن","utf-8"):
       aro.append("n")
       x=1
    if s == unicode("و","utf-8"):
       aro.append("w")
       x=1
    if s == unicode("ى","utf-8"):
       aro.append("Y")
       x=1
    if s == unicode("ه","utf-8"):
       aro.append("h")
       x=1
    if s == unicode("ي","utf-8"):
       aro.append("y")
       x=1
    if s == unicode("آ","utf-8"):
       aro.append("|")
       x=1
    if s == unicode("ء","utf-8"):
       aro.append("'")
       x=1
    if s == unicode("ؤ","utf-8"):
       aro.append("&")
       x=1
    if s == unicode("ة","utf-8"):
       aro.append("p")
       x=1
    if s == unicode("ـ","utf-8"):
       aro.append("")
       x=1
    if s == unicode("َ","utf-8"):
       aro.append("a")
       x=1
    if s == unicode("ُ","utf-8"):
       aro.append("u")
       x=1
    if s == unicode("ِ","utf-8"):
       aro.append("i")
       x=1
    if s == unicode("ّ","utf-8"):
       aro.append("~")
       x=1
    if s == unicode("ْ","utf-8"):
       aro.append("o")
       x=1
    if s == unicode("إ","utf-8"):
       aro.append(">")
       x=1
    if s == unicode("آ","utf-8"):
       aro.append("^")
       x=1
    if s == unicode("ٰ","utf-8"):
       aro.append("`")
       x=1
    if s== " ":
       aro.append(" ")
       x=1
    if s== "\n":
       aro.append("\n")
       x=1
#------------punc------------------------------

#-----------------------------------------------
    else:
      if x == 0 :
       aro.append(s)
finally:
   pass


try:
   text2=codecs.open("BW Text.txt","w+","utf-8")
   text2.writelines(aro)
   text2.close()
finally:
    pass
