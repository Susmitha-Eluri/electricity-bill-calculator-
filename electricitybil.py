prevkwh = int(input("Enter Previous KWH : "))
preskwh = int(input("Enter Present KWH : "))
# Calculation of units
units=preskwh-prevkwh
print("UNITS =",units)
 
if units<=30:
 amount= units*2.31
  
elif units<=75:
   amount= ((units-30)*3.33 + 30*2.31)
   
elif  units<=125:
   amount= ((units-75)*6.37 + 45*3.33 + 30*2.31)

elif  units<=225:
   amount= ((units-125)*6.41 + 50*6.37 + 45*3.33 + 30*2.31)
   
else:
   amount= ((units-225)*8.75 + 100*6.41 + 50*6.37 + 45*3.33 + 30*2.31)
   
print("Amount:",amount)
