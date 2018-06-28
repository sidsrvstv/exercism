import re

def verify(isbn):
    pattern = r"^([0-9]{1})-*([0-9]{3})-*([0-9]{5})-*([0-9]|[X]{1})$"

    if re.search(pattern, isbn):
        match = re.search(pattern, isbn)
        s1 = match.group(1)
        val1 = int(s1)
        val1 *= 10

        s2 = match.group(2)
        val2=9*int(s2[0]) + 8*int(s2[1]) + 7*int(s2[2])
        
        s3 = match.group(3)
        val3 = 6*int(s3[0]) + 5*int(s3[1]) + 4*int(s3[2]) + 3*int(s3[3]) + 2*int(s3[4])

        s4 = match.group(4)
        print(s4)
        if s4 == "X":
            val4 = 10
        else:
            val4 = int(s4)

        if (val1+val2+val3+val4) % 11 == 0:
            return True
        else:
            return False
        
    else:
        return False



# print(verify('3-598-21508-XX'))
# print(verify('3-598-21507-XX'))
