import libnum
info = """13 1 17 3 14 10 18 18 16 13 15 5 5 6 12 8 8 3 2 5 4 10 11 3 1 5 10 1 7 5 6 10 9 4 3 10 15 13
muffins
safetydance
updateerror
tracebackerror
abcdefghijklmnopqrstuvwxyz
woweatcool
great
filefolders
goodnessgracious
tombstone
aidanglickman
qwertyuiopasdfghjklzxcvbnm
ABCTFLearn
CornOnTheCob
le14{octobre}
cryptographyFORENSICS
BJblazkowicz
red_HeRRiNGG<>TIME!
"""
word = []
for x in info.split("\n"):
	word.append(x)
res = ""
info2 = word[0].split(" ")
for i in range(0,len(info2),2):
	par1 = int(info2[i])
	if i+1 >= len(info2):
		continue
	par2 = int(info2[i+1])
	if par2 <= len(word[par1]):
		res += word[par1][par2-1]
print res