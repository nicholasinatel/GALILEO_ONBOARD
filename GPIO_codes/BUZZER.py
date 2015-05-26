
#!/usr/bin/python 
import sys
import time

def pins_export():
    try:
        pin1export = open("/sys/class/pwm/pwmchip0/export","w")
        pin1export.write("3")
        pin1export.close()
    except IOError:
        print "ERRO EM PIN_EXPORT"

def enable_buzz( value ):
    try:
        enable1buzz = open( "/sys/class/pwm/pwmchip0/pwm3/enable", "w" )
        enable1buzz.write( str( value ) )
        enable1buzz.close()
    except IOError:
        print "ERRO na funcao enable_buzz"   


def period_buzz( value1 ):
    try:
        period1 = open ( "/sys/class/pwm/pwmchip0/pwm3/period ", "w" )
        period1.write( str( value1 ) )
        period1.close()
        print("Period_Buzz = "+str(value1))
    except IOError:
        print "ERRO na funcao period_buzz" 

def duty_cycle ( value2 ):
    try:
        duty1 = open ( "/sys/class/pwm/pwmchip0/pwm3/duty_cycle ", "w" )
        duty1.write( str ( value2 ) )
        duty1.close()
        print("Duty_Cycle ="+str(value2))
    except IOError:
        print "ERRO na funcao duty_cycle" 

pins_export()
enable_buzz(1)
duty_cycle(50000)
while True:
    print "on"
    period_buzz(1000)
    
    

    time.sleep( 5 )

    print "off"

    period_buzz(10)
    time.sleep( 5 ) 

