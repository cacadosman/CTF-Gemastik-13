from collections import OrderedDict
import os
import re

def replace(email, payload):
    rules = re.compile('(email\[[\-]?\d*\])')
    match = rules.findall(payload)
    email = email.replace('\\n','\n')

    for m in match:
        substitute = eval(m)
        payload = payload.replace(m, substitute)

    payload = payload.replace('+', '') 
    return payload

emails = open('email').readlines()
payloads = open('payload').readlines()
results = OrderedDict()

for email, payload in zip(emails, payloads):
    email = email[5:-1]    
    clean = replace(email, payload)
    command = re.findall('p\(([\w\.\s\*]*)\)', clean)[0]
    position = int(re.findall('(\d+)', clean[-60:][:5])[0])
    character = re.findall(r'\[__eq__\]\(([\n\w\\\/\.\:\+\= ]*)', clean)[0]

    data = results.get(command, dict())
    if not data:
        results[command] = data
    data[position] = character

for k,v in results.iteritems():
    print '$', k
    print ''.join(v.values()).strip()
    print 
