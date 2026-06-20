from analyser import *

request = input('How can I help you? ')
while request != 'off':
    analyse(request)
    request = input('How else can I help you? (off - exit) ')
