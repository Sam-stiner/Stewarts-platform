import serial, time 
arduino = serial.Serial('COM13', 9600, timeout=.1)

print ('Python Serial Control for Rotary Based Stewarts Platform')
print ('Initializeing')

while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print data

time.sleep(1) #allows python to start comunication with the arduino

print ('Ready for user input.')
print ('Please type your command...(type "help" for help)')

command = input() #user input for platform control

#prints available commands
for command = ('help') :
	print ('Availible commands are: ')
	
	print ('"setbackoff" (turns LCD backlight off)')
	print ('"setbackon" (turns LCD backlight on)')
	print ('"setpositions" (sets servo positions)')
	print ('"printpos" (prints the location and rotation of the platform to LCD)') #future change here add print to serial as well
	print ('"stopprintpos" (stops printing)')
	print ('"switchirda" (toggles IR control)')
#	print ('"setpositionsinms"') I still need to figure out what this does
	print ('"switchirdaoff" (turns IRDA control off)')
#	print ('"getposition"') I still need to figure out what this does

#turns table backlight off
for command = ('setbackoff'):
	arduino.write(0)
	print ('backlight has been turned off')
	
#turns table backlight on
for command = ('setbackon'):
	arduino.write(1)
	print ('blacklight has been turned off')

#sets servo positions
for command = ('setpositions'):
	arduino.write(2)
	
	print ('please enter 6 numbers for the "X" location:')
	xlocation = input()
	arduino.write(xlocation)
	
	print ('please enter 6 numbers for the "Y" location:')
	ylocation = input()
	arduino.write(ylocation)
	
	print ('please enter 6 numbers for the "Z" location')
	zlocation = input()
	arduino.write(zlocation)
	
	print ('please enter 6 numbers for the "X" rotation')
	xrotation = input()
	arduino.write(xrotation)
	
	print ('please enter 6 numbers for the "Y" rotation')
	yrotation = input()
	arduino.write(yrotation)
	
	print ('please enter 6 numbers for the "Z" rotation')
	zrotation = input()
	arduino.write(zrotation)
	
	print ('Location and Rotation have been set. To veiw location and rotation, use "printpos"')
	
#prints rotation and location to LCD future will also print to serial
for command = ('printpos'):
	arduino.write(3)
	print ('started printing positions')

#stops location and rotation printing to LCD and Serial
for command = ('stopprintpos'):
	arduino.write(4)
	print ('printing positions has stoped')
	
#toggles IRDA control
for command = ('switchirda'):
	arduino.write(5)
	print ('IRDA control toggeled')

#turns IRDA off
for command = ('switchirdaoff'):
	arduino.write(7)
	print ('IRDA control turned off')
	

