# OpenRedireXSS
Open redirects/xss URL discovery tool
This tool is designed primarily for fuzzing open redirects or URL parameters that may be susceptible to XSS. For example, you can fuzz URLs like www.example.com/account/HERE/signin or parameters such as example.com?redirectURL=FUZZ.

The purpose of this tool is to generate ready-to-test URLs, which you can click to quickly verify if an endpoint is vulnerable.

Usage
URL Middle Mode
This mode is for URLs that have a variable part in the middle of the path. For example:
https://site.com/signin/{account}/signin
You can use:

python openredirexss.py -u http://site.com/signin/HERE/signin --openredirect no -w /path/to/payload

URL Parameter Mode
This mode is for URLs that include parameters, such as:

http://site.com/sign?redirectURL=
You can use:

python openredirexss.py -u http://site.com/sign?redirectURL= -w /path/to/payload
Example
To output the results to a file for further analysis, you can use :

python openredirexss.py -u http://site.com/signin/HERE/signin --openredirect no -w /path/to/payload >> file.txt
