import cgi



print("Content-Type: text/html")
print()
print("<Title> 2 images</TITLE>")
print("<head>  Fill in informstion  </head>")
print(' <br>  ' )


print(' <b> Image 1:</b>')

#this line is disguesting in python...good lord why we can't do this in regular html
print('<form method="post" form action="/test/cgi-bin/display.py" target="_blank" ><input name="funcID"type="hidden"value="2">Title: <input name="title" type="text"></br>Year:<input name="year" type="text"></br>Artist: <input name="art" type="text"></br>Caption: <input name="cap" type="text"></br>image:<input name="image" type="text"></br> <b> Image 2:</b> Title: <input name="title2" type="text"></br>Year:<input name="year2" type="text"></br>Artist: <input name="art2" type="text"></br>Caption:<input name="cap2" type="text"></br>image:<input name="image2" type="text"></br><input type="submit" value="Add"></form>')


FORM = cgi.FieldStorage()
title1 = FORM.getlist("title")
year1 = FORM.getlist("year")
art1 = FORM.getlist("art")
cap1 = FORM.getlist("cap")
image1 = FORM.getlist("image")

title2 = FORM.getlist("title2")
year2 = FORM.getlist("year2")
art2 = FORM.getlist("art2")
cap2 = FORM.getlist("cap2")
image2 = FORM.getlist("image2")


