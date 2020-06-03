# program to search 3 digits number in given string

import re

'''
st = input('Enter any string:')

reobj = re.compile('\d\d\d')
print(reobj.search(st))
print(reobj.findall(st))


st = 'hellogd god good morning'
reobj = re.compile('gd or god or good')
reobj = re.compile('gd')
reobj = re.compile('god')
reobj = re.compile('good')
print(reobj.search(st))

# using ? :: zero or one time
# search for gd or god or good

st = 'hellogd god good morning'
reobj = re.compile('g(o)?d')
print(reobj.search(st))

# using * :: zero or more times
# search for gd or god or good

st = 'hellogd god good morning'
reobj = re.compile('g(o)*d')
print(reobj.search(st))

# using + :: one or more times
# search for gd or god or good or goood

st = 'hellogoood god good morning '
reobj = re.compile('g(o)+d')
print(reobj.search(st))

# search for hahahahaha ha{3}

st = 'Hello anand hahaha anand ha'
reobj = re.compile('hahaha')
print(reobj.search(st))

st = 'Hello anand hahaha anand ha'
reobj = re.compile('ha{3}')
print(reobj.search(st))

st = 'Hello anand hahahahaha anand ha'
reobj = re.compile('ha{3,5}')
print(reobj.search(st))

# \d === 0 to 9
# | ====
# /D other than digit
# search for 4 or 5 or 6 for {3} digits compulsory

st = 'Hello prem123 hah45578ahaha66ha'
reobj = re.compile('\d\d\d')
print(reobj.search(st))

st = 'Hello prem123 hah45578ahaha66ha'
reobj = re.compile('4|5|6')  # pipe symbol
print(reobj.search(st))

# search for 4 or 5 or 6 for {3} digits compulsory


st = 'Hello prem123 hah45578ahaha66ha'
reobj = re.compile('456')  # search 456
print(reobj.search(st))

# search for 4 or 5 or 6 for {3} digits compulsory

st = 'Hello prem123 hah45578ahaha66ha'
reobj = re.compile('(4|5|6){3}')  # pipe symbol
print(reobj.search(st))

st = 'raju123j@eeevankumar'
reobj = re.compile('\d\d\d\D\D\D')  # pipe symbol
print(reobj.search(st))

# \d  only digit
# \D only alphabits
# \d+  only multiple digit


st = 'raju123j@eeevankumar'
reobj = re.compile('\d+')  # multiple digit
print(reobj.search(st))

st = """ 12 December month christmas 11 November 10 October 7 July schools open
        8 August dussera"""

reobj = re.compile('\d+\s\w+')
reobj = re.compile('\d\d\s\w+')
print(reobj.search(st))
print(reobj.findall(st))

# identify Vowels

st = 'I am using Umbrella As it is Raining'

reobj = re.compile('[aeiou]')  # or [aeiouAEIOU] ===> continues characters# Search for a or e or i or o or u
print(reobj.search(st))
print(reobj.findall(st))

st = 'I am using Umbrella As it is Raining'

reobj = re.compile('a|e|i|o|u')  # Search for a or e or i or o or u
print(reobj.search(st))
print(reobj.findall(st))

st = 'I am using Umbrella As it is Raining'

reobj = re.compile('[aeiouAEIOU]{2}')  # Search for any 2 characters continuous
print(reobj.search(st))
print(reobj.findall(st))

# ^ :: Not in between in squqre brackests
# ^ :: Starts with

st = 'I am using Umbrella As it is Raining'
reobj = re.compile('[^aeiouAEIOU]{2}')  # excepts aeiouAEIOU All character displays
print(reobj.search(st))
print(reobj.findall(st))

st = 'good Morning Hello Brother'
reobj = re.compile('Hello')
print(reobj.search(st))

st = 'Hello Brother'
reobj = re.compile('^Hello')
print(reobj.search(st))

# $ :: Ends with

st = 'good Morning Hello Brother Hello'
reobj = re.compile('Hello$')  # Hello ending word

reobj = re.compile('Hello!$')  # Hello ending word
print(reobj.search(st))

st = 'good Morning Hello Brother Hello'
reobj = re.compile('$Hello')
print(reobj.search(st))

# start with digit and ending with digits
st = '123654'
reobj = re.compile('^\d+$') # starts with digit and ends with digits

st = 'goodat Morning Hello Brother Helloat'
reobj = re.compile('at')
print(reobj.search(st))

st = 'good Morning Hello Brother Helloat'
reobj = re.compile('.at')  # ('.{1,3}at')
reobj = re.compile('.{1,3}at')  # ('.{1,3}at')

print(reobj.search(st))

'''

a = int(input("Enter any mobile number:"))
m=re.compile("(0/9)?[7-9]\d{9}")
if m!=None:
    print("Entered mobile number is valid:",a)
else:
    print("Entered mobile number is not valid:",a)

a=input("Enter any email id:")
m=re.compile('[a-zA-Z-0-9-]@(gmial,yahoo,outlook)[.]com')
if m!=None:
    print("Entered email id is valid:",a)
else:
    print("Entered email id not valid:")
