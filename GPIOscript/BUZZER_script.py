
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

#def write_buzz( value ):
 #   buzz1 = open( "/sys/class/gpio/gpio3/value", "w" )
  #  buzz1.write( str( value ) )
   # buzz1.close()
#except IOError:
 #   print "ERRO na funcao write_buzz"   

def period_buzz( value1 ):
    try:
        period1 = open ( " ", "w" )
        period1.write( str( value1 ) )
        period1.close()
        print("Period_Buzz = "+str(value1))
    except IOError:
        print "ERRO na funcao period_buzz"

def duty_cycle ( value2 ):
    try:
        duty1 = open ( " ", "w" )
        duty1.write( str ( value2 ) )
        duty1.close()
        print("Duty_Cycle ="+str(value2))
    except IOError:
        print "ERRO na funcao duty_cycle"    


   
   
pins_export()


while True:
    print "on"
    
    enable_buzz( 1 )
    period_buzz(1000)
    duty_cycle(500000)
    time.sleep( 5 )
    print "off"
    enable_buzz( 0 )
    period_buzz(100)
    time.sleep( 5 ) 
