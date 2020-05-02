#!/usr/bin/python3
# Copyright 2019, Aniket.N.Bhagwate, All rights reserved.
# Date Created : 25 APRIL 2020
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import urllib.request, urllib.error
import os
import argparse
import sys
import threading

banner=""" 
	 ____ ___ ____  __  ______  
  	|  _ \_ _|  _ \ \ \/ / / /  
  	| | | | || |_) | \  / / /   
  	| |_| | ||  _ <  /  \ \ \   
  	|____/___|_| \_\/_/\_\_\_\\ 
     +=============================+                          
     +--  Directory  Bruteforce  --+
     +=============================+
     +  Code by : Aniket Bhagwate  +
     +=============================+
"""

print(banner)


def bforce(response_code,collection,f,url,word,out,start,stop):


	w = word.split("/")[-1:]
	

	if url[-1:]=='/':
		pass
	else:
		url = url+'/'


	
	cnt = 0
	for x in range(start,stop+1):
		os.system("clear")
		print(banner)
		print("[*] Using Wordlist   :   \033[30;42m" + "{}".format(w) + "\033[m")
		print("[*] Total Words : {}".format(len(f)))
		print("[*] Active Threads : [4]\n")
		cnt = cnt+1
		u = url + f[x]
		try:
			for c in collection:
				print(c)
				print("+----------------------------------------------------------------------------------------+")
				
			print("------------------------------------------------_=_TESTING : \033[30;42m {} \033[m    ------".format(u))
			conn = urllib.request.urlopen(u)
			
		except urllib.error.HTTPError as e:
			# 300 , 404 ......
			
			if e.code==404:  #or e.code==403:
				pass
			else:
				temp = u + "  ==>   ( {} )  ".format(e.code) + " < {} > ".format(response_code["{}".format(e.code)])
				collection.append(temp)
				

		except urllib.error.URLError as e:
			pass
			#print(u + "( {} )".format(e.reason))


		else:
			#200
			temp = u + "  ==> ( {} )".format(conn.code) + " < {} > ".format(response_code["{}".format(conn.code)])
			collection.append(temp)

		

		
	

def main():
	
	########################################## Response Codes --- 
	rcode = open("Response_Codes.txt","r")
	rcode = rcode.read().split("\n")
	rcode.pop()
	response_code={}
	for res in rcode:
		res = res.split("_")
		response_code['{}'.format(res[0])] = res[1]
	####################################################################################
	
	collection=['']

	parser = argparse.ArgumentParser(description="Bruteforce Websites")
	parser.add_argument('-u','--url',metavar='',required=True , help='URL for Bruteforce ')
	parser.add_argument('-w','--wordlist',metavar='',required=False,help='Wordlist to use for bruteforce',)
	parser.add_argument('-o','--output',metavar='',required=False,help='File name to write the output')
	args = parser.parse_args()



	url = args.url

################################## To check if user has selected a wordlist 

	if args.wordlist==None :
		word = "common.txt"

	else:
		word=args.wordlist

####################################################################


################################## To check if user has selected Output file

	if args.output==None :
		out = None

	else:
		out=args.output

####################################################################




################################## To check proper required url format
	try:
		val = url.split(":")[1]
		
	except:
		print('Improper URL format ! ')
		print('\nFORMAT : http/https://<URL>')
		sys.exit()
####################################################################
	
	
	f = open(word,'r',encoding="ISO-8859-1")
	f = f.read().split("\n")
	f.pop()
	
	
	###################################### Divide words by index from wordlist and allot threads
	num = 4  # no of threads
	val=len(f) # no of words in wordlist

	tem = round((val/num))
	temp = val - tem*num

	lis=[]
	for x in range(num):
		if x==num-1:
			lis.append(round(val/num)+temp)
			break
		lis.append(round(val/num))
	


	l = lis[x]-lis[x]
	h = lis[x]-1
	val = lis[0]
	dic=[]
	dic.append(str(l)+"_"+str(h))
	try:
		for x in range(len(lis)):

			l = h+1
			h = h+lis[x]
			dic.append(str(l)+"_"+str(h))
	except:
		pass

	dic.pop()
	############################################################################

	
	#url,word,out,start,stop

	# temporary value for out
	


	###################################### Threads


	x1 = threading.Thread(target=bforce, args=(response_code,collection,f,url,word,out,int(dic[0].split("_")[0]),int(dic[0].split("_")[1])))
	x2 = threading.Thread(target=bforce, args=(response_code,collection,f,url,word,out,int(dic[1].split("_")[0]),int(dic[1].split("_")[1],)))
	x3 = threading.Thread(target=bforce, args=(response_code,collection,f,url,word,out,int(dic[2].split("_")[0]),int(dic[2].split("_")[1],)))
	x4 = threading.Thread(target=bforce, args=(response_code,collection,f,url,word,out,int(dic[3].split("_")[0]),int(dic[3].split("_")[1],)))


	######################################



	###################################### Start threads

	x1.start()
	os.system("clear")
	x2.start()
	os.system("clear")
	x3.start()
	os.system("clear")
	x4.start()
	os.system("clear")
	print(banner)


	######################################
	
	###################################### Join threads
	x1.join()
	x2.join()
	x3.join()
	x4.join()
	######################################

	
	
	if out!=None:
		os.system("clear")
		print(banner)

		print("\n\n \033[30;42m [!] Generating Output File....... : < {} >  \033[m\n".format(out))
		f = open("{}".format(out) , "a")
		for x in collection:
			f.write(x + "\n")
		f.close()
		sys.exit()
		
	os.system("clear")
	print(banner)
	print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
	for x in collection:
		print("[ - ]" + "\t" + x)
		print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
		

if __name__ == "__main__":
	main()
	
	
		
	
