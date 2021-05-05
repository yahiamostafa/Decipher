cipher = 'gur synt vf 2w68lsudym Vg vf cerggl rnfl gb frr gur synt ohg pna lbh frr vg v gbbx arneyl 1 zvahgr gb rapbqr guvf jvgu EBG13 tbbq yhpx va fbyivat gung' # encrypted message
for i in range(0,26):
    temp = ''
    for j in cipher:
        if (j ==' ' or j.isdigit()):
            temp = temp+j
        else:
            if (j.isupper()):
                index = (ord(j)+i)
                if (index > ord('Z')):
                    temp = temp + chr(index-ord('Z')+ord('A')-1)
                else:
                    temp= temp + chr(index)
            else:
                index = (ord(j)+i)
                if (index > ord('z')):
                    temp = temp + chr(index-ord('z')+ord('a')-1)
                else:
                    temp= temp + chr(index)
    print(temp)
