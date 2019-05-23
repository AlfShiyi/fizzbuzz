import os
from task1 import changeline
filedict= dict()
def walk(dirname):
	global filedict
	for name in os.listdir(dirname):
		path = os.path.join(dirname,name)
		if os.path.isfile(path):
			path = path.split("/")
			dirname = "/".join(path[:-1])
			filename = path[-1]
			#print("/".join(path[:-1]),path[-1])
			filedict[dirname] = filedict.get(dirname,list())
			filedict[dirname].append(filename)
		else:
			walk(path)

walk(input("input dir:"))
ffw = open("file.list","wt")
fsw = open("folder.list","wt")
for i in filedict.items():
    k = i[0]
    v = i[1]
    for item in v:
        names = item.split(".")
        name = names[0]
        if len(names[0])==0:
            name = "."+names[1]
        if len(names)>1 and len(names[0])>0:
            ext = names[-1]
        else:
            ext="null"
        fullname = k+'/'+item
        charcnt = os.path.getsize(fullname)
        wline = f"{name}-{ext}-{charcnt}\n"
        ffw.writelines(wline)

for i in filedict.keys():
    i = changeline(i)
    fsw.writelines(i+"\n")
#print(filedict)