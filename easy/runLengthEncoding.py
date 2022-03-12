def runLengthEncoding(string):
    res = ""
    identical = string[0]
    count =0
    for i in string:
        if i == identical:
            count+=1
        else:
            #add to string 
            while count>=10:
                res +="9"+identical
                count-= 9
            res += str(count)+identical
            identical = i
            count=1
    while count>=10:
        res +="9"+identical
        count-= 9
    res += str(count)+identical
    return res

string = "AAAAAAAAAAAAABBCCCCDD"
print(runLengthEncoding(string))