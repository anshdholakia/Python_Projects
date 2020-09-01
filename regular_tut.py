import re



mystr='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin bahut badiya
admii hainin
+919234012242
+912435325543
+912314254545
+912343654645
+915060940524
+913025054345
+912323534553
+914534543452
+912343453345
+913254564545
'''


# Type of functions
# findall,search,finditer,split,sub

# findall=It returns specific string matches.
# search=It returns match object

# patt=re.compile(r'fass')#r'' is a raw string

# print(r"\n") #whill print\n as it is a raw string type

#patt=re.compile(r'.adm') #using meta characters(.)

# patt=re.compile(r'^Tata')   #As it starts with Tata ^ meta character is used for this

# patt=re.compile(r'nin$')   # As it ends with nin $ ised like this

# patt=re.compile(r'ai*') #will print a aii, ai, or aiiiiiiii;

# patt=re.compiler(r'ai+') #at least one 'i' so a wont print

# patt=re.compile(r'ai{1}'); #it will search for only ai

# patt=re.compile(r'(ai){2}')  #it will search for aiai # ai is a group due to parenthsis

# patt=re.compile(r'a{2}')

# patt=re.compile(r'ai{2}|t')  #ai or t searching

#Special Sequences

# patt=re.compile(r'\ATata')  # mystr starts with tata

# patt=re.compile(r'\bTata') # string starts with Tata

# patt=re.compile(r'Tata\b') # string end with Tata

# Finding Patterns

# patt=re.compile(r'\d{5}-\d{4}')

patt=re.compile(r'[91]\d{10}')

match=patt.finditer(mystr)

print("[",end="")
for matches in match:

    print(matches,end=", ")#means that if you slice is 448:452, it wil give fass

    # print(mystr[448:452]) # prints fass

print("]")