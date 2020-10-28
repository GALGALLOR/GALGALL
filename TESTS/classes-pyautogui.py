import pyautogui
import datetime
import time
import os
MATH ='782 191 0689'
MATH_PASS='123456'
MATH_LINK='https://zoom.us/j/7821910689?pwd=SU9LREV0UVpZWHZLWW5nMWNYdENDQT09'
MINE = '710 762 9261'
MY_LINK  = 'https://zoom.us/s/91027223074'
COMPUTER = '573 904 3667'
COMPUTER_PASS = '12345678'
COMPUTER_LINK='https://zoom.us/j/5739043667?pwd=Wm00b21PdWJxaXpLUUc5TzNyRHhLQT09'
KISWAHILI='9548478307'
KISWAHILI_PASS = '123456'
KISWAHILI_LINK='https://zoom.us/j/9548478307?pwd=TCtMSHJ2ZmRqdnU2MWtQUEc1Y1FWdz09'
ENGLISH='7563264376'
ENGLISH_PASS = '123456'
ENGLISH_LINK='https://zoom.us/j/7563264376?pwd=TFUrMlJwUXdKTlVvNmpVeUIxVHhFdz09'
BIOLOGY='6292489277'
BIOLOGY_PASS = '123456'
BIOLOGY_LINK='https://zoom.us/j/6292489277?pwd=MjNFWG81QmN3Q0FvN21NTkgraGU3QT09'
PHYSICS='9841406308'
PHYSICS_PASS='123456'
PHYSICS_LINK='https://zoom.us/j/9841406308?pwd=NXNQVmszWUFScGU1bkZtTTBoWDJQdz09'
CHEMISTRY='7651793624'
CHEMISTRY_PASS = '123456'
CHEMISTRY_LINK='https://zoom.us/j/7651793624?pwd=N1lFUmM0aUZ5anB5WitOMVk1TEFydz09'
HISTORY='9049924850'
HISTORY_PASS = '12345678'
HISTORY_LINK='https://zoom.us/j/9049924850?pwd=TWh5N0NwZUhFQkZMWjZvelNHdExUZz09'
PATH='Zoom.lnk'
now=datetime.datetime.now()
firstlessonhour = int(input('what is the first lesson hour '))
firstlessonminute = int(input('what is the minute '))
ampm=input('am or pm ')
day = input('what day is it ')
if 'pm' in ampm:
    firstlessonhour+=12

hour_duration = firstlessonhour-now.hour
minute_duration= firstlessonminute-now.minute
seconds = hour_duration*60*60
seconds=seconds+minute_duration*60
while 1==1:
    seconds = seconds-1
    minutes = seconds // 60
    if minutes < 60:
        seconds_in_minute=seconds%60
        print(minutes,' minutes : ',seconds_in_minute,' seconds')
    elif minutes > 60:
        seconds_in_minute = seconds%60
        hours = minutes//60
        minutes=minutes%60
        print(hours,' hours : ', minutes,' minutes: ',seconds_in_minute,'seconds')
    else:
        print(seconds,' seconds')
    time.sleep(1)
    pyautogui.press('shift')
    if seconds==0:
        print('time is upppppp')
        break
os.system(PATH)
time.sleep(5)
pyautogui.press('enter')
time.sleep(5)

if 'onday' in day:
    #LESSON1
    pyautogui.press('enter')
    pyautogui.typewrite(BIOLOGY)
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(BIOLOGY_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')

    #calling time delay
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    seconds = seconds + minute_duration * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break

    #LESSON2
    pyautogui.press('enter')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON3
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(CHEMISTRY)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(CHEMISTRY_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON4
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(MATH)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON5
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(ENGLISH)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(ENGLISH_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break

elif 'uesday' in day:
    #LESSON1
    pyautogui.press('enter')
    pyautogui.typewrite(KISWAHILI)
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(KISWAHILI_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break

    #LESSON2
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(MATH)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(MATH_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break

    #LESSON3
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(HISTORY)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(HISTORY_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON4
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(COMPUTER)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(COMPUTER_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON5
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(PHYSICS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(PHYSICS_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break

elif 'ednesday' in day:
    #LESSON1
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(KISWAHILI)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(KISWAHILI_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON2
    pyautogui.press('enter')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON3
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(CHEMISTRY)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(CHEMISTRY_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON4
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')

    pyautogui.typewrite(PHYSICS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(PHYSICS_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON5
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(HISTORY)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(HISTORY_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


elif 'hursday' in day:
    #LESSON1
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(KISWAHILI)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(KISWAHILI_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON2
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(PHYSICS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(PHYSICS_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break

    #LESSON3
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(BIOLOGY)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(BIOLOGY_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON4
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(CHEMISTRY)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(CHEMISTRY_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON5
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(ENGLISH)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(ENGLISH_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


elif 'riday' in day:
    #LESSON1
    pyautogui.press('enter')
    pyautogui.typewrite(MATH)
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(MATH_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON2
    pyautogui.press('enter')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON3
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(BIOLOGY)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(BIOLOGY_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON4
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(ENGLISH)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(ENGLISH_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


    #LESSON5
    pyautogui.press('enter')

    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.typewrite(COMPUTER)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(COMPUTER_PASS)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    pyautogui.keyDown('alt')
    pyautogui.press('a')
    print('muted')
    pyautogui.press('v')
    print('camera off')
    pyautogui.keyUp('alt')
    #calling time
    hour_duration = 1
    seconds = hour_duration * 60 * 60
    while 1 == 1:
        seconds = seconds - 1
        minutes = seconds // 60
        if minutes < 60:
            seconds_in_minute = seconds % 60
            print(minutes, ' minutes : ', seconds_in_minute, ' seconds')
        elif minutes > 60:
            seconds_in_minute = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print(hours, ' hours : ', minutes, ' minutes: ', seconds_in_minute, 'seconds')
        else:
            print(seconds, ' seconds')
        time.sleep(1)
        pyautogui.press('shift')
        if seconds == 0:
            print('time is upppppp')
            pyautogui.press('esc')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.keyDown('alt')
            pyautogui.press('q')
            pyautogui.keyUp('alt')
            pyautogui.press('tab')
            pyautogui.press('enter')
            print('class left successfully')
            break


