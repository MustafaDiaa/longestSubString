userIN = raw_input('Please enter any string you like: ')

def longestString(userIN):
    count = 0
    maxString = ''
    ans = ''
    oldAns = ''
    answer = userIN[0] + userIN[1]
    falseCount = 0
    for count in range(0, len(userIN)-1):
        if ord(userIN[count]) <= ord(userIN[count+1]):
            maxString = maxString + userIN[count]
            oldAns = ans
            oldNewAns = answer
            ans = maxString + userIN[count+1]
            if len(answer) >= len(ans):
                answer = oldNewAns
            else:
                answer = oldAns + userIN[count+1]
            #print 'answer = ' + ans        remove the comment if you want to see inner calculations
            #print 'new answer = ' + answer     remove the comment if you want to see inner calculations
        else:
            maxString = ''
            falseCount += 1

    if falseCount == len(userIN)-1:
        print 'Longest substring in alphabetical order is: ' + userIN[0]

    else:
        print 'Longest substring in alphabetical order is: ' + answer

longestString(userIN)
