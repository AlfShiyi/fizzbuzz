import re
def changeline(line):
	line = line.replace('O','0')
	line = line.replace('o','0')
	line = line.replace('I','1')
	line = line.replace('i','1')
	line = line.replace('A','4')
	line = line.replace('a','4')
	line = re.sub("..er","xor",line)
	line = line.replace('E','3')
	line = line.replace('e','3')
	return line
def l33ttwist(targetfile,folder=""):
	name = targetfile.split("/")
	name = name[-1]
	name = name.split('.')
	name[-2] += "Copy"
	name = ".".join(name)
	try:
		fr = open(targetfile)
		fw = open(folder+"/"+name,'wt')
		for line in fr:
			line = changeline(line)
			fw.writelines(line+"\n")
	except:
		print("error happend")
	finally:
		fr.close()
		fw.close()	
if __name__=="__main__":
	l33ttwist(input("filename:"))
