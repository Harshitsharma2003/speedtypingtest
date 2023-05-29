import time 

String= ''' Pollution is the intermixing of harmful substances known as pollutants with the natural environmental components.'''
wordcount = len(String.split())
print("psg = " ,String)
while True:
    t0 = time.time()
    inputtext=str(input('Enter the  Sentence:'))
    t1 = time.time()
    acc=len(set(inputtext.split())&set(String.split()))
    acc=acc/wordcount
    timetaken = t1-t0
    wpm = wordcount/timetaken
    print("WPM",wpm,"Accuracy",acc,"Timetaken",timetaken)