import random


def randomwords(lists):

    num = len(lists)
    random.shuffle(lists)
    print lists
    for word in lists:
        length = len(word)
        #print length
        if length >0:
            if word[length-1] <= 'Z' and word[length-1] >= 'A' or word[length-1] <= 'z' and word[length-1] >= 'a':
                filedes.write(word+' ')
            else:
                filedes.write(word[:length-1]+' ')
    filedes.write('\n')
    filedes.write('\n')



fileobj = open('source.txt', 'r')
filedes = open('destine.txt', 'w+')
for linestr in fileobj:
    #print linestr
    wordslist = linestr.split(' ')
    randomwords(wordslist)

fileobj.close()
filedes.close()
print "Random is completed,Please see destine.txt"



