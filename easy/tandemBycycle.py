from audioop import reverse


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    s=0
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()

    for idx,(value1,value2) in enumerate(zip(redShirtSpeeds,blueShirtSpeeds)):
            s+=max(value1,value2)
    return s

redShirtSpeed=[5, 5, 3, 9, 2]
blueShirtSpeed=[3, 6, 7, 2, 1]
fastest = True
print(tandemBicycle(redShirtSpeed,blueShirtSpeed,fastest))
