from __future__ import division
import random
import datetime
import requests
# import urllib.request
import urllib
import urllib2
# import ssl

# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
 
url1 = 'https://akshaysandbox4.mybigcommerce.com/'
url2 = 'https://akshaysandbox4.mybigcommerce.com/bath/'
url3 = 'https://akshaysandbox4.mybigcommerce.com/garden/'
url4 = 'https://akshaysandbox4.mybigcommerce.com/kitchen/'
url5 = 'https://akshaysandbox4.mybigcommerce.com/publications/'
urldict = {1 : url1, 2: url2, 3: url3, 4 :url4, 5 : url5}

result_dict = {}
total = 0

def collect_input():
	raw_input("Enter the number of the page you want to access: ")

def displayResult(page_number):
	minMaxAvgValues = result_dict.get(page_number)
	print "Maximum = %s" % minMaxAvgValues.get('max')
	print "Minimum = %s" % minMaxAvgValues.get('min')
	print "Avg = %s" % minMaxAvgValues.get('avg')

def processData():
	for i in range(len(urldict.keys())):
		select_url = urldict.get(i+1)
		random_number = random.randint(1, 20)
		min_l = 999999
		max_l = 0
		avg = 0
		for j in range(random_number):# hit the URL and get the responses time.
			urllib.urlopen(select_url)
    		response = requests.get(select_url, timeout=6)
    		response_time = response.elapsed.total_seconds()# compare it with min and max and replace the values accordingly.
    		if response_time < min_l:
    			min_l = response_time
    		if response_time > max_l:
    			max_l = response_time
			# avg = ((avg x i ) + current_response_time)/ i + 1
			global total	
			total = total + response_time
			avg = total/(i+1)
			#avg = ((avg * i) + response_time)/(i + 1)
		# result_dict.append({j:{'min':min, 'max':max, 'avg':avg}}
		result_dict.update({i+1:{'min':min_l, 'max':max_l, 'avg':avg}})

if __name__ == "__main__":
	processData()
	print(result_dict)
	page_number = collect_input()
	displayResult(page_number)

	#(len(urldict.keys()

			#if response_time > 0:
			#	min_l = response_time
			#if response_time < 0:
			#	max_l = response_time

		#	if __name__ == '__main__':
	#processData()
	#page_number = collect_input()
	#displayResult(page_number)
