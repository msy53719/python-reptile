str = 'abc1cd2df3'


def getPos(str):
    for st in str:
        if st.isdigit():
            sst = st
            if int(sst) == 1:
                pos1 = str.index(sst)
                str1 = str[0:pos1] * int(sst)
            elif int(sst) == 2:
                pos2 = str.index(sst)
                str2 = str[pos1 + 1:pos2] * int(sst)
            elif int(sst) == 3:
                str3 = str[pos2 + 1:len(str) - 1] * int(sst)
    return str1 + str2 + str3

print(getPos(str))


# return sst,pos
#print(str1, end='')
def getNum(str):
    for st in str:
        if st.isdigit():
            sst = st
            print(sst)
            pos = str.index(sst)
    return sst, pos

# print(getNum(str))
