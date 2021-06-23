import os 
somme=0
mot=input("Saisissez le mot  : ")
for element in mot :
  if element.lower() in "aeiouy":
    somme+= ord(element)
print ("la somme donne :".somme)
