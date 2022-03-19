#replace all space in a string with "%20"




import string


def URLify(url:string):
    url = url.strip()
    return url.replace(" ","%20")

string = "Mr Jhon Smith    "
print(URLify(string))