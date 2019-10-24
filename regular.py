#findall- matches all in a variable
#substitute- substitutes all
#search- search the first occurance of any char in a variable
#match- matches any first char in a variable



import re
var ="my mob num is 1234512345 & 1234657890 & 1245368907"
res=re.findall('[1][0-9]{9}',var)#matches any 10 digits
print(res)
var1 ="""CKM id is Aa658
        MKM id is P627
        UKM id is A456
        SNK id is W345"""
pat1='[A-Z]{2,}'#minimum 2 capital letters and max any
pat2='[A-Z][0-9]{3}'#one upper case letter followed by 3 numbers
names=re.findall(pat1,var1)
print(names)
ids=re.findall(pat2,var1)
print(ids)

        
var2="""INDIA ip is 123.4.5.6
        USA ip is 1.1.12.16
        UK ip is 233.455.113.4"""
pat1='[A-Z]{2,}'
pat2='[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'
name=re.findall(pat1,var2)
print(name)
ips=re.findall(pat2,var2)
print(ips)

var3="""CKM dob is 12:11:1992
        SNK dob is 01-10-1990
        UKM dob is 16.05.1996"""
pat1='[0-9]{2}[^A-Za-z0-9][0-9]{2}[^A-Za-z0-9][0-9]{4}'

pat2='[A-Z]{2,}'
pat=pat1+'|'+pat2
res=re.findall(pat,var3)
print(res)
