from posixpath import split
import re

camelCase = 'ThisIsCamelCaseR'


def camelCaseFun(camelString):
    wordList = []
    camelIndex = 0
    i = 0 
    while i < len(camelCase):
        if re.match('[A-Z]', camelCase[i]):
            if camelCase[camelIndex:i] != '':
                wordList.append(camelCase[camelIndex:i])
            camelIndex= i
        i+=1
    wordList.append(camelCase[camelIndex:])

    # print(len(wordList))
    return len(wordList)

cam = camelCaseFun(camelCase)
print(cam)