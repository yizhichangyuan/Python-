def nameTest(first,second,middle =''):
    if middle:
        name = first + ' ' + second + ' ' +middle
    else:
        name = first + ' ' + second
    return name.title()