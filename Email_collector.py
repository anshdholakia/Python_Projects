import re

str='''
Random Lists
Phone Numbers
Passwords
URLs
Fake Names
Credit Cards
SEARCH
MENU

 
Random Email Addresses:
RERUNOPTIONS
esbeck@sbcglobal.net
thaljef@msn.com
fbriere@comcast.net
manuals@aol.com
ryanshaw@me.com
nasarius@live.com
miturria@me.com
animats@att.net
keiji@att.net
gerlo@sbcglobal.net
mrsam@msn.com
webdragon@me.com
<dsfgnfvdnf@ojndfsodf.com>
RERUN
OPTIONS
SHARE

 
Edit Settings
Quantity
12
RERUN

Notice: Since these are randomly generated, some of this email address may be unintentionally real.

Want a fake name or address too?

Home
FAQ
Privacy Policy
Contact
Randomize your custom list
Sitemap
This site is offered as is to those who visit it. We make no guarantees regarding its services. Just enjoy yourself.

'''


patt=re.findall(r'\w+@\S+\w',str)  #findall function will find email in some paragrap. very important function
for i in range(0,len(patt)):
    print(patt[i])
# email=patt.finditer(str)
# i=0
# for emails in email:
#     e=emails.start()
#     d =emails.end()
#     i+=1
#     print(f"email {i}:",str[e:d])





