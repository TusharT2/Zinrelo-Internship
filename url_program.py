from __future__ import division
import random
import datetime
import requests
# import urllib.request
import urllib
 
url1 = 'https://akshaysandbox4.mybigcommerce.com/'
url2 = 'https://akshaysandbox4.mybigcommerce.com/bath/'
url3 = 'https://akshaysandbox4.mybigcommerce.com/garden/'
url4 = 'https://akshaysandbox4.mybigcommerce.com/kitchen/'
url5 = 'https://akshaysandbox4.mybigcommerce.com/publications/'
urllist = [url1, url2, url3, url4, url5]

i = 0
response_time = 0
max_l = 0
min_l = 0
avg_l = 0
r1 = random.randint(1, 20)
select_num = input("Enter the number of the page you want to access: ")
select_url = urllist[select_num - 1]
times = []

for i in range(r1 + 1):
    urllib.urlopen(select_url)
    response = requests.get(select_url, timeout=6)
    times.append(response.elapsed.total_seconds())
    print(response.elapsed.total_seconds())

max_l = max(times)
min_l = min(times)
avg_l = sum(times)/len(times)

print "Here are the min, max and average response times for URL #%d" % select_num 
print "Maximum = " + str(max_l) + ", Minimum = " + str(min_l) + ", Average = " + str(avg_l)

#    r = requests.get(url, timeout=6)
#    r.raise_for_status()
#    respTime = str(round(r.elapsed.total_seconds(),2))
#    currDate = datetime.datetime.now()
#    currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
#    print(currDate + " " + respTime)
