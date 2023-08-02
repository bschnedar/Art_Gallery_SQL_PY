import cgi

from mp2_25821724 import title2
from mp2_25821724 import image2
from mp2_25821724 import art2
from mp2_25821724 import year2
from mp2_25821724 import cap2

from mp2_25821724 import title1
from mp2_25821724 import image1
from mp2_25821724 import art1
from mp2_25821724 import year1
from mp2_25821724 import cap1


t1x  = ''.join(title1)
i1x = ''.join(image1)
a1x  = ''.join(art1)
y1x = ''.join(year1)
c1x = ''.join(cap1)



print(' <script> function ChangeText2() { document.getElementById("tt").innerHTML = %s; document.getElementById("ii").src = %s;document.getElementById("aa").innerHTML = %s;document.getElementById("yy").innerHTML = %s; document.getElementById("cc").innerHTML = %s; } </script>'%(title2, image2, art2, year2, cap2))

print(' <script> function ChangeText1() { document.getElementById("tt").innerHTML = %s; document.getElementById("ii").src = %s;document.getElementById("aa").innerHTML = %s;document.getElementById("yy").innerHTML = %s; document.getElementById("cc").innerHTML = %s; } </script> '%(title1, image1, art1, year1, cap1))



print('<p id="tt">%s</p> '  %(t1x))
print('<img id="ii" src=%s> ' %(i1x))
print('<p id="aa">%s</p> '  %(a1x))
print('<p id="yy">%s</p> ' %(y1x) )
print('<p id="cc">%s</p> ' %(c1x))




print('<button type="button" onclick="ChangeText1()">Image 1</button> ')
print('<button type="button" onclick="ChangeText2()">Image 2</button> ')




