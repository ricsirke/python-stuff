"""

add a little bit of logic to css by creating classes and creating selectors that acts on classes
classes can be added from SAP Design Studio's script language

exporting a .css stylesheet

use case:
    SAP Design Studio coloring of dynamic charts

    
.aa2 >  div > div > div > svg > g.v-m-main > g.v-m-plot > g.v-datashapegroup > g.v-column:nth-child(1) > g.v-datashape > rect { fill: rgb(0, 0, 0) }
"""

cols = ["red", "blue", "black", "orange", "lblue", "yell"]
colcode = ["#FF0000", "#F9AD79", "#EACF5F", "rgb(237, 124, 18)", "rgb(18, 237, 237)", "rgb(255, 250, 0)"]
sels = []
classes = []

# selectors for the class-order combs and the classes which can activate them
for c in range(len(cols)):
    for i in range(1,7):
        cssclass = "%s%d" % (cols[c], i)
        csssel = ".%s > div > div > div > svg > .v-m-main > .v-m-plot > .v-datashapesgroup > .v-column > .v-datashape:nth-child(%d) > rect { fill: %s }" % (cssclass, i, colcode[c])
        
        #classes.append(".%s{ display: default }" % (cssclass))
        sels.append(csssel)  
                    
        
def printl(l):     
    for e in l:
        print e
    
def save(filename):
    with open(filename, "w") as f:
        # for e in classes:
            # f.write(e + "\n")
        # f.write("\n\n")
        
        for e in sels:
            f.write(e + "\n")

#printl(sels)
#printl(classes)
save("style.css")