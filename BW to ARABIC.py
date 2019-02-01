# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
import codecs
#----------- v----------
l=[]
l2=[]
aro=[]
x=0
c=0
words="la`kin sawof misaAs haA^&um <il~aA >abadFA Hiyn yawoma}i*"
d=""
#-----------------------------------------------

try:
   for s in words:
    x=0
#-----------------letters---------------
    if s ==  "F":
       aro.append(unicode("ً", "utf-8"))
       x=1
    if s ==  "A":
       aro.append(unicode("ا", "utf-8"))
       x=1
    if s ==  ">":
       aro.append(unicode("أ", "utf-8"))
       x=1
    if s ==  "b":
       aro.append(unicode("ب", "utf-8"))
       x=1
    if s ==  "t":
       aro.append(unicode("ت", "utf-8"))
       x=1
    if s ==  "v":
       aro.append(unicode("ث", "utf-8"))
       x=1
    if s ==  "j":
       aro.append(unicode("ج", "utf-8"))
       x=1
    if s ==  "H":
       aro.append(unicode("ح", "utf-8"))
       x=1
    if s ==  "x":
       aro.append(unicode("خ", "utf-8"))
       x=1
    if s ==  "d":
       aro.append(unicode("د", "utf-8"))
       x=1
    if s ==  "*":
       aro.append(unicode("ذ", "utf-8"))
       x=1
    if s ==  "r":
       aro.append(unicode("ر", "utf-8"))
       x=1
    if s ==  "z":
       aro.append(unicode("ز", "utf-8"))
       x=1
    if s ==  "s":
       aro.append(unicode("س", "utf-8"))
       x=1
    if s ==  "$":
       aro.append(unicode("ش", "utf-8"))
       x=1
    if s ==  "S":
       aro.append(unicode("ص", "utf-8"))
       x=1
    if s ==  "D":
       aro.append(unicode("ض", "utf-8"))
       x=1
    if s ==  "T":
       aro.append(unicode("ط", "utf-8"))
       x=1
    if s ==  "Z":
       aro.append(unicode("ظ", "utf-8"))
       x=1
    if s ==  "E":
       aro.append(unicode("ع", "utf-8"))
       x=1
    if s ==  "g":
       aro.append(unicode("غ", "utf-8"))
       x=1
    if s ==  "f":
       aro.append(unicode("ف", "utf-8"))
       x=1
    if s ==  "q":
       aro.append(unicode("ق", "utf-8"))
       x=1
    if s ==  "k":
       aro.append(unicode("ك", "utf-8"))
       x=1
    if s ==  "l":
       aro.append(unicode("ل", "utf-8"))
       x=1
    if s ==  "m":
       aro.append(unicode("م", "utf-8"))
       x=1
    if s ==  "n":
       aro.append(unicode("ن", "utf-8"))
       x=1
    if s ==  "w":
       aro.append(unicode("و", "utf-8"))
       x=1
    if s ==  "Y":
       aro.append(unicode("ى", "utf-8"))
       x=1
    if s ==  "h":
       aro.append(unicode("ه", "utf-8"))
       x=1
    if s ==  "y":
       aro.append(unicode("ي", "utf-8"))
       x=1
    if s ==  "|":
       aro.append(unicode("آ", "utf-8"))
       x=1
    if s ==  "'":
       aro.append(unicode("ء", "utf-8"))
       x=1
    if s ==  "&":
       aro.append(unicode("ؤ", "utf-8"))
       x=1
    if s ==  "{":
       aro.append(unicode("ئ", "utf-8"))
       x=1
    if s ==  "p":
       aro.append(unicode("ة", "utf-8"))
       x=1
    if s ==  "a":
       aro.append(unicode("َ", "utf-8"))
       x=1
    if s ==  "u":
       aro.append(unicode("ُ", "utf-8"))
       x=1
    if s ==  "i":
       aro.append(unicode("ِ", "utf-8"))
       x=1
    if s ==  "~":
       aro.append(unicode("ّ", "utf-8"))
       x=1
    if s ==  "o":
       aro.append(unicode("ْ", "utf-8"))
       x=1
    if s ==  "<":
       aro.append(unicode("إ", "utf-8"))
       x=1
    if s== "`":
       aro.append(unicode("ٰ", "utf-8"))
       x=1
    if s== "\n":
       aro.append(unicode("\n", "utf-8"))
      
       x=1
    if s== "^":
       aro.append(unicode("ٓ", "utf-8")) 
       x=1
    if s ==  "_":
       aro.append(unicode("-", "utf-8"))
       x=1
    if s ==  "N":
       aro.append(unicode("ٌ", "utf-8"))
       x=1
    if s ==  "K":
       aro.append(unicode("ٍ", "utf-8"))
   
    if s ==  "}":
       aro.append(unicode("ئ", "utf-8"))

#------------punc-------------------------------

#-----------------------------------------------
    else:
      if x == 0 :
       aro.append(s)
      else:
        pass

finally:
   for f in aro:
      d=d+f
   print d
   print words
      


