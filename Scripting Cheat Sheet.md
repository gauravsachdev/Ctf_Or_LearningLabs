\#!/usr/bin/env python3

#### BASH

God Tier Cheatsheet
https://devhints.io/bash


#### Python 

import requests 

response = requests.get(url,params={key: value}, args)  

session = requests.Session()
session.max_redirects = 3
session.get(url)


`
| Parameter  | Values                                                                                                                                                                                                            |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| allow_redirects | Optional. A Boolean to enable/disable redirection. Default True (allowing redirects)                                                                                                                              |
| auth            | Optional. A tuple to enable a certain HTTP authentication. Default None                                                                                                                                           |
| cert            | Optional. A String or Tuple specifying a cert file or key. Default None                                                                                                                                           |
| cookies         | Optional. A dictionary of cookies to send to the specified url. Default None                                                                                                                                      |
| headers         | Optional. A dictionary of HTTP headers to send to the specified url. Default None                                                                                                                                 |
| proxies         | Optional. A dictionary of the protocol to the proxy url. Default None                                                                                                                                             |
| stream          | Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True). Default False                                                                                         |
| timeout         | Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response. Default None which means the request will continue until the connection is closed |
| verify          | Optional. A Boolean or a String indication to verify the servers TLS certificate or not. Default True                                                                                                             |


##### Pwntools  
* from pwn import *
* r = remote(url, port)
* r.recvuntil(delim) - Receive data until a delimiter is found
        recv(n) - Receive any number of available bytes
        recvline() - Receive data until a newline is encountered
        recvuntil(delim) - Receive data until a delimiter is found
        recvregex(pattern) - Receive data until a regex pattern is satisfied
        recvrepeat(timeout) - Keep receiving data until a timeout occurs
        clean() - Discard all buffered data
* Sending data
        send(data) - Sends data
        sendline(line) - Sends data plus a newline
* Processes and Basic Features
        Creating a process and then using it for shell  
        
        ```py
                from pwn import *
                io = process('sh')
                io.sendline('echo Hello, world')
                io.recvline()
                # 'Hello, world\n'
                io.interactive()
         ```
* client = listen(8080).wait_for_connection()
* SSH 
                from pwn import *

                session = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0')

                io = session.process('sh', env={"PS1":""})
                io.sendline('echo Hello, world!')
                io.recvline()
                # 'Hello, world!\n'
