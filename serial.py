x= 1

import time, serial 
arduino = serial.Serial( 'COM12',baudrate=9600, timeout=.1)

print ('Python Serial Control for Rotary Based Stewarts Platform')
print ('Initializeing...')

time.sleep(1) #allows python to start comunication with the arduino

print ('Ready for user input.')
print ('Please type your command...(type "help" for command list)')



while x==1:

    cmd0 = raw_input('CMD0>  ') #user input for platform control

    #prints available commands
    if cmd0 == 'help':
        print ('Availible commands are: ')
        
        print ('"setbackoff" (turns LCD backlight off)')
        print ('"setbackon" (turns LCD backlight on)')
        print ('"setpositions" (sets servo positions)')
        print ('"printpos" (prints the location and rotation of the platform to LCD)') #future change here add print to serial as well
        print ('"stopprintpos" (stops printing)')
        print ('"switchirda" (toggles IR control)')
        #    print ('"setpositionsinms"') I still need to figure out what this does
        print ('"switchirdaoff" (turns IRDA control off)')
        #    print ('"getposition"') I still need to figure out what this does
        
        #turns table backlight off
    elif cmd0 == 'setbackoff':
        arduino.write('0')
        print ('backlight has been turned off')
    
 #turns table backlight on
    elif cmd0 == ('setbackon'):
        arduino.write('1')
        print ('blacklight has been turned on')

    #sets servo positions
    elif cmd0 == ('setpositions'):
        arduino.write('2')
        print ('please enter 6 numbers for the "X" location:')
        xl = raw_input()
        xlc = int(xl)
        xlw = float(xlc)
        xli = xlw*100*25
        arduino.write(xli)
            
        print ('please enter 6 numbers for the "Y" location:')
        yl = raw_input()
        ylc = yl*100*24
        if ylc <= 99999:
            arduino.write('0')
            arduino.write(ylc)
        elif ylc <= 9999:
            arduino.write('00')
            arduino.write(ylc)
        elif ylc <= 999:
            arduino.write('000')
            arduino.write(ylc)
        elif ylc <= 99:
            arduino.write('0000')
            arduino.write(ylc)
        elif ylc <= 9:
            arduino.write('00000')
            arduino.write(ylc)
        elif ylc <= 0:
            arduino.write('000000')
            arduino.write(ylc)
        else:
            arduino.write(ylc)
        
        
        print ('please enter 6 numbers for the "Z" location')
        zl = raw_input()
        zlc = zl*100*24
        if zlc <= 99999:
            arduino.write('0')
            arduino.write(zlc)
        elif zlc <= 9999:
            arduino.write('00')
            arduino.write(zlc)
        elif zlc <= 999:
            arduino.write('000')
            arduino.write(zlc)
        elif zlc <= 99:
            arduino.write('0000')
            arduino.write(zlc)
        elif zlc <= 9:
            arduino.write('00000')
            arduino.write(zlc)
        elif zlc <= 0:
            arduino.write('000000')
            arduino.write(zlc)
        else:
            arduino.write(zlc)
        
        print ('please enter 6 numbers for the "X" rotation')
        xr = raw_input()
        xrc = yl*100*24
        if xrc <= 99999:
            arduino.write('0')
            arduino.write(xrc)
        elif xrc <= 9999:
            arduino.write('00')
            arduino.write(xrc)
        elif xrc <= 999:
            arduino.write('000')
            arduino.write(xrc)
        elif xrc <= 99:
            arduino.write('0000')
            arduino.write(xrc)
        elif xrc <= 9:
            arduino.write('00000')
            arduino.write(xrc)
        elif xrc <= 0:
            arduino.write('000000')
            arduino.write(xrc)
        else:
            arduino.write(xrc)

        print ('Location and Rotation have been set. To veiw location and rotation, use "printpos"')    
        
        #prints rotation and location to LCD future will also print to serial
    elif cmd0 == ('printpos'):
        arduino.write('3')
        print ('started printing positions')

#stops location and rotation printing to LCD and Serial
    elif cmd0 == ('stopprintpos'):
        arduino.write('4')
        print ('printing positions has stoped')
        
    #toggles IRDA control
    elif cmd0 == ('switchirda'):
        arduino.write('5')
        print ('IRDA control toggeled')
        
    #turns IRDA off
    elif cmd0 == ('switchirdaoff'):
        arduino.write('7')
        print ('IRDA control turned off')
    else:
        print ('invalid command type "help" for command list')
    
    
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        print data
    
