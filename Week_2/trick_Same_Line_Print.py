#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:56:44 2017

@author: RyanMunguia
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:51:04 2017

@author: RyanMunguia
"""

# Notice how if we have two print statements                

#print("Hi")
#print("there")

# The output will have each string on a separate line:                
#Hi
#there
                
# Now try adding the following:
print("Hi",end='')
print("there")
print("Hi",end='*')
print("there")   
                
# The output will place the subsequent string on the same line
# and will connect the two prints with the character given by end

#Hithere
#Hi*there   

print("Hi", end='')
print("Ryan", end='')
print("Munguia")