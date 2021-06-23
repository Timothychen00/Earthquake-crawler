# Summary
This program will connect to https://www.cwb.gov.tw/V8/C/E/index.html and cause the web is edited by AJAX.
So I try to parse the web and find the real data.Then use hashlib(md5) to check if the web is updated.
At the end,send Mac Notification about the detail of the latest Earthquake
# Config(python lib.......)
bs4            |parser
subprocess     |mac system module 
os             |path operating
hashlib        |md5
sys            |current file location
time           |sleep
requests       |request
# About Auther
Auther: Timothychen(陳澤榮) \n
Email:  tiomthychenpc@gmail.com
