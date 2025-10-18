def kbc():
 questions = [
  [
     "1. quran paak jis raat mai nazil kiya gaya us mubarak raat ko kya kehte hain", "lailatul qadr" , "shab e meraj", "yomae aashoora","shab e barat",1
  ],
  [
    "2. In Namazo mai se kon si Namaz Farz Namaz nahi hai","Namaz e juma","Namaz e fajr", "Namaz e magrib", "Namaz e eidul fitr",4
  ],
  [
    "3. In Nabi a.s. mai aise kon se nabi they jo bahut beemaar raha kartey they","yusuf a.s." , "yunus a.s." , " ayyoob a.s.","yahya a.s.",3
  ],
  [
     "4.wo konse khalifa they jinhone 2200000 murabba meel zameen par hukmarani ki"," Hazrat abubakar rz.", "Hazrat umar rz.", "Hazrat usman rz","Hazrat Ali rz",2
  ],
  [
     "5. Nabi moosa a.s. ka Nabi haroon a.s. se kya rishta tha"," bap bete ka",  "bhai bhai ka","dada pote ka", "chacha bhatije ka",2
  ],
  [
    "6. jannat mai \"tuba\" naam ka kya hoga","ek phal ","ek phool", "ek ped", "ek farista",3
  ],
  [
    "7. Wo kon se nabi they jinhone lanati badshah namrood se jang ki thi","Hazrat ibrahim a.s.", "Hazrat idres a.s" , "Hazrat suleman a.s ","Hazratadam a.s.",1
  ],
  [
    "8. Aisa kon sa fal hai jiska naam quran mai mojood hai","Aam", "Anar" ,"Angoor","seb",3
  ],
  [
    "9. Wo kon se nabi hai jinka naam quran mai sabse zyada baar aaya hai","Dawood a.s.", "moosa a.s.","eesa a.s." ,"nooh a.s.",2
  ],
  [
    "10. wo kon se sahaba hai jinka naam quraan paak mai mojood hai","hazrat talha rz.", "hazrat zubair rz.", "hazrat akrama rz.", "hazrat zaid rz.",4
  ],
  [
    "11. Inme se konse sahaba ashro mubassira sahaba mai shamil nahi hai","hazrat khalid bin waleed r.a.","hazrat talha r.a.","hazrat zubair r.a.","hazrat saeed r.a.",1
  ],
  [
    "12. jang e badr mai faristo ne kis sahabi ki peeli pagdi ki nakal ki thi","Saadibn AbiWaqqas ","Bilalibn Rabbah","Zubayr ibn Awwam","Ali ibn AbiTaalib",3
  ],
  [
    "quran mai Madinah ka naam kis naam se liya gaya hai","bakkah","marwah ","quds" , "yathrib",4
  ],
  [
     "Inme se wo kon se sahabi e rasool hai jonhone Qaisarah seher ko mukammal fatah kiya tha","hazrat e muaz bin jabl","hazrat e ameer e muawiya", "hazrat e abu sufiyan","hazrat e abu huraira",2
  ]

]
 levels = [1000, 2000,5000, 10000, 20000, 40000, 80000, 160000,320000,640000,1250000,2500000,5000000,10000000]
 
 for i in range(0,   len(questions)):
  
   question = questions[i]
   print(f"\n\nQuestion for Rs. {levels[i]}")
   print(f" {question[0]} \n a. {question[1]}          b. {question[2]} ")
   print(f"c. {question[3]}          d. {question[4]} ")
   reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
   if (reply == 0):
    if i==0:
        print(f" okk you quit, you take money home is {0}")
    else:        
        print(f" okk you quit, you take money home is {levels[i-1]}")
    break
   if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")

   if(i > 4 and i<=9 and reply!=question[-1]):
    print("wrong answer")
    print("You take home money is 10000")
    break
    
   elif(i>=0 and i<=4 and reply!=question[-1]):
    print("Wrong answer!")
    break
    
   elif(i > 9 and i<=14 and reply!=question[-1]):
    money = 320000
    print("wrong answer")
    print("You take home money is 320000")
    break
   elif(i == 14 and reply==question[-1]):
    
      print("you win")
      print("You take home money is 10000000")
      print("Game is END")
      break
    
kbc()