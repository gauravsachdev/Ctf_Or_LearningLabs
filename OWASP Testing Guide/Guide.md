Easier and more efficent to spot security flags if one has access to the source code. Each step of SDLC should incorporate security.

## Passive Testing  

### 4.1 Information Gathering  

#### 4.1.1 Conduct Search Engine Discovery Reconnaissance for Information Leakage  

* Baidu, China’s most popular search engine.  
* Bing, a search engine owned and operated by Microsoft, and the second most popular worldwide. Supports advanced search keywords.  
* binsearch.info, a search engine for binary Usenet newsgroups.  
* DuckDuckGo, a privacy-focused search engine that compiles results from many different sources. Supports search syntax.  
* Google, which offers the world’s most popular search engine, and uses a ranking system to attempt to return the most relevant results. Supports search operators. 
* Startpage, a search engine that uses Google’s results without collecting personal information through trackers and logs. Supports search operators.  
* Shodan, a service for searching Internet-connected devices and services. Usage options include a limited free plan as well as paid subscription plans.

Common filters for google

* site: will limit the search to the provided URL.
* inurl: will only return results that include the keyword in the URL.
* intitle: will only return results that have the keyword in the page title.
* intext: or inbody: will only search for the keyword in the body of pages.
* filetype: will match only a specific filetype, i.e. png, or php.
* cache: view cached data  

[Exploit-DB has a good resource to get sensitive files](https://www.exploit-db.com/google-hacking-database)

#### 4.1.2 Fingerprinting
Process of determining what tech stack is being used. 

##### Banner Grabbing 
A banner grab is performed by sending an HTTP request to the web server and examining its response header. This can be accomplished using a variety of tools, including telnet for HTTP requests, or openssl for requests over SSL.  
In cases where the server information is obscured, testers may guess the type of server based on the ordering of the header fields.  
Not a fool proof method can lead to times where it is not confirmed.
As default error pages offer many differentiating factors between types of web servers, their examination can be an effective method for fingerprinting even when server header fields are obscured.

Using Automated Scanning Tools
* Netcraft, an online tool that scans websites for information, including the web server.
* Nikto, an Open Source command-line scanning tool.
* Nmap, an Open Source command-line tool that also has a GUI, Zenmap.

#### 4.1.3 Review Webserver Metafiles for Information Leakage
Test Objectives 
* Information leakage of the web application’s path(s) or functionality.
* Create the list of directories that are to be avoided by Spiders, Robots, or Crawlers.
* Identify other information which may benefit testers or attackers.

##### Robots.txt
wget or curl both work.
```
 curl -O -Ss http://www.google.com/robots.txt && head -n5 robots.txt
```
Robots.txt contains disallow fields to prevent crawlers from accessing those sub-directories. Getting the contents of these files can reveal more directories.

##### META Tags
<META> tags are located within the HEAD section of each HTML document and should be consistent across a web site in the event that the robot/spider/crawler start point does not begin from a document link other than webroot i.e. a deep link. Robots directive can also be specified through use of a specific META tag.

If there is no ```<META NAME="ROBOTS" ... >``` entry then the “Robots Exclusion Protocol” defaults to INDEX,FOLLOW respectively. Therefore, the other two valid entries defined by the “Robots Exclusion Protocol” are prefixed with NO... i.e. NOINDEX and NOFOLLOW.

Based on the Disallow directive(s) listed within the robots.txt file in webroot, a regular expression search for <META NAME="ROBOTS" within each web page is undertaken and the result compared to the robots.txt file in webroot.

Organizations often embed informational META tags in web content to support various technologies such as screen readers, social networking previews, search engine indexing, etc. Such meta-information can be of value to testers in identifying technologies used, and additional paths/functionality to explore and test.

##### Sitemaps 
A sitemap is a file where a developer or organization can provide information about the pages, videos, and other files offered by the site or application, and the relationship between them. Search engines can use this file to more intelligently explore your site. Testers can use sitemap.xml files to learn more about the site or application to explore it more completely.

##### Security.txt
security.txt is a proposed standard which allows websites to define security policies and contact details.
The file may be present either in the root of the webserver or in the .well-known/ directory. Ex:
* https://example.com/security.txt
* https://example.com/.well-known/security.txt

##### Humans TXT
humans.txt is an initiative for knowing the people behind a website. It takes the form of a text file that contains information about the different people who have contributed to building the website.

##### Others
Check the .wellknown directory
Tools
* Browser (View Source or Dev Tools functionality)
* curl
* wget
* Burp Suite
* ZAP

#### 4.1.4 Enumerate Applications on Webserver

A paramount step in testing for web application vulnerabilities is to find out which particular applications are hosted on a web server. Many applications have known vulnerabilities and known attack strategies that can be exploited in order to gain remote control or to exploit data. In addition, many applications are often misconfigured or not updated, due to the perception that they are only used “internally” and therefore no threat exists.
Most of the times across multuple ips and domain names. Important to identify wahts in scope and whats not.

##### Black-Box Testing

There are three factors influencing how many applications are related to a given DNS name (or an IP address):

* Different Base URL

The obvious entry point for a web application is www.example.com, i.e., with this shorthand notation we think of the web application originating at http://www.example.com/ (the same applies for https). However, even though this is the most common situation, there is nothing forcing the application to start at /.

For example, the same symbolic name may be associated to three web applications such as: http://www.example.com/url1 http://www.example.com/url2 http://www.example.com/url3

In this case, the URL http://www.example.com/ would not be associated with a meaningful page, and the three applications would be hidden, unless the tester explicitly knows how to reach them, i.e., the tester knows url1, url2 or url3. There is usually no need to publish web applications in this way, unless the owner doesn’t want them to be accessible in a standard way, and is prepared to inform the users about their exact location. This doesn’t mean that these applications are secret, just that their existence and location is not explicitly advertised.

here is no way to fully ascertain the existence of non-standard-named web applications. Being non-standard, there is no fixed criteria governing the naming convention, however there are a number of techniques that the tester can use to gain some additional insight.

First, if the web server is mis-configured and allows directory browsing, it may be possible to spot these applications. Vulnerability scanners may help in this respect.

Second, these applications may be referenced by other web pages and there is a chance that they have been spidered and indexed by web search engines. If testers suspect the existence of such hidden applications on www.example.com they could search using the site operator and examining the result of a query for site: www.example.com. Among the returned URLs there could be one pointing to such a non-obvious application.

Another option is to probe for URLs which might be likely candidates for non-published applications. For example, a web mail front end might be accessible from URLs such as https://www.example.com/webmail, https://webmail.example.com/, or https://mail.example.com/. The same holds for administrative interfaces, which may be published at hidden URLs (for example, a Tomcat administrative interface), and yet not referenced anywhere. So doing a bit of dictionary-style searching (or “intelligent guessing”) could yield some results. Vulnerability scanners may help in this respect.

* Non-standard Ports

While web applications usually live on port 80 (http) and 443 (https), there is nothing magic about these port numbers. In fact, web applications may be associated with arbitrary TCP ports, and can be referenced by specifying the port number as follows: http\[s\]://www.example.com:port/. For example, http://www.example.com:20000/.
It is easy to check for the existence of web applications on non-standard ports. A port scanner such as nmap is capable of performing service recognition by means of the -sV option, and will identify http[s] services on arbitrary ports. What is required is a full scan of the whole 64k TCP port address space.

For example, the following command will look up, with a TCP connect scan, all open ports on IP 192.168.1.100 and will try to determine what services are bound to them (only essential switches are shown – nmap features a broad set of options, whose discussion is out of scope):
```
nmap –PN –sT –sV –p0-65535 192.168.1.100
```
* Virtual Hosts

DNS allows a single IP address to be associated with one or more symbolic names. For example, the IP address 192.168.1.100 might be associated to DNS names www.example.com, helpdesk.example.com, webmail.example.com. It is not necessary that all the names belong to the same DNS domain. This 1-to-N relationship may be reflected to serve different content by using so called virtual hosts. The information specifying the virtual host we are referring to is embedded in the HTTP 1.1 Host header.

One would not suspect the existence of other web applications in addition to the obvious www.example.com, unless they know of helpdesk.example.com and webmail.example.com.

DNS Zone Transfers
This technique has limited use nowadays, given the fact that zone transfers are largely not honored by DNS servers. However, it may be worth a try. First of all, testers must determine the name servers serving x.y.z.t. If a symbolic name is known for x.y.z.t (let it be www.example.com), its name servers can be determined by means of tools such as nslookup, host, or dig, by requesting DNS NS records.

If no symbolic names are known for x.y.z.t, but the target definition contains at least a symbolic name, testers may try to apply the same process and query the name server of that name (hoping that x.y.z.t will be served as well by that name server). For example, if the target consists of the IP address x.y.z.t and the name mail.example.com, determine the name servers for domain example.com.

The following example shows how to identify the name servers for www.owasp.org by using the host command:
```
$ host -t ns www.owasp.org
www.owasp.org is an alias for owasp.org.
owasp.org name server ns1.secure.net.
owasp.org name server ns2.secure.net.
```
A zone transfer may now be requested to the name servers for domain example.com. If the tester is lucky, they will get back a list of the DNS entries for this domain. This will include the obvious www.example.com and the not-so-obvious helpdesk.example.com and webmail.example.com (and possibly others). Check all names returned by the zone transfer and consider all of those which are related to the target being evaluated.

Trying to request a zone transfer for owasp.org from one of its name servers:
```
$ host -l www.owasp.org ns1.secure.net
Using domain server:
Name: ns1.secure.net
Address: 192.220.124.10#53
Aliases:

Host www.owasp.org not found: 5(REFUSED)
; Transfer failed.
```
DNS Inverse Queries
This process is similar to the previous one, but relies on inverse (PTR) DNS records. Rather than requesting a zone transfer, try setting the record type to PTR and issue a query on the given IP address. If the testers are lucky, they may get back a DNS name entry. This technique relies on the existence of IP-to-symbolic name maps, which is not guaranteed.

Web-based DNS Searches
This kind of search is akin to DNS zone transfer, but relies on web-based services that enable name-based searches on DNS. One such service is the Netcraft Search DNS service. The tester may query for a list of names belonging to your domain of choice, such as example.com. Then they will check whether the names they obtained are pertinent to the target they are examining.

Reverse-IP Services
Reverse-IP services are similar to DNS inverse queries, with the difference that the testers query a web-based application instead of a name server. There are a number of such services available. Since they tend to return partial (and often different) results, it is better to use multiple services to obtain a more comprehensive analysis.

Domain Tools Reverse IP (requires free membership)

Bing, syntax: ip:x.x.x.x

Webhosting Info, syntax: http://whois.webhosting.info/x.x.x.x

DNSstuff (multiple services available)

Net Square (multiple queries on domains and IP addresses, requires installation)

The following example shows the result of a query to one of the above reverse-IP services to 216.48.3.18, the IP address of www.owasp.org. Three additional non-obvious symbolic names mapping to the same address have been revealed.

OWASP Whois Info\ Figure 4.1.4-1: OWASP Whois Info

Googling
Following information gathering from the previous techniques, testers can rely on search engines to possibly refine and increment their analysis. This may yield evidence of additional symbolic names belonging to the target, or applications accessible via non-obvious URLs.

For instance, considering the previous example regarding www.owasp.org, the tester could query Google and other search engines looking for information (hence, DNS names) related to the newly discovered domains of webgoat.org, webscarab.com, and webscarab.net.

Tools
* DNS lookup tools such as nslookup, dig and similar.
* Search engines (Google, Bing and other major search engines).
* Specialized DNS-related web-based search service: see text.
* Nmap
* Nessus Vulnerability Scanner
* Nikto

#### 4.1.5 Review Webpage Content for Information Leakage

As code becomes more and more complicated as it has look for comments, meta data and "source map". Look for information.

##### Review webpage comments and metadata
Self-explanatory

##### Identifying JavaScript Code and Gathering JavaScript Files
Programmers often hardcode sensitive information with JavaScript variables on the front-end. Testers should check HTML source code and look for JavaScript code between ```<script>``` and ```</script>``` tags. Testers should also identify external JavaScript files to review the code (JavaScript files have the file extension .js and name of the JavaScript file usually put in the src (source) attribute of a ```<script>``` tag). API keys and harcoded credentials.

##### Identifying Source Map Files
Source map files will usually be loaded when DevTools open. Testers can also find source map files by adding the “.map” extension after the extension of each external JavaScript file. For example, if a tester sees a ```/static/js/main.chunk.js``` file, they can then check for its source map file by visiting ```/static/js/main.chunk.js.map.```
Tools
* Wget
* Browser “view source” function
* Eyeballs
* Curl
* Burp Suite
* Waybackurls
* Google Maps API Scanner

#### Identify Application Entry Points
