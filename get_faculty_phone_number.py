#Tusubira David 2018/HD05/198U
#Angole Daniel
#Allan Murungi
#Nanziri Eunice

import urllib.request       #Adjusted library/module name to python3 version
import re

# a helper function to remove html tags from a string
def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

# a function which retrieves a user's mobile phone number by requesting a web-page from the Makerere staff directory
def findphonenumber(name):
    name = name.lower()
    name = name.replace(' ','-')
    staffdirectorypage = 'http://directory.mak.ac.ug/users/%s.html' % (name)
    try:
        for line in urllib.request.urlopen(staffdirectorypage):
            if ('256' in line) and ('7' in line) :                   #change identifiers to typical phone number characters
                line = remove_html_tags(line)
                return line
    except urllib.request.HTTPError:
        return 'Person not found'

# now call the above function to find some phone numbers
for staffmember in ['Aluk Meshac', 'Benjamin Kanagwa', 'John Quinn']:
    phone_number = findphonenumber(staffmember)
    print (phone_number)

