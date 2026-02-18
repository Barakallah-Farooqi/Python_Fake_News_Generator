# Fake news generator
import random
# Fo
l1 = ["Imran_Khan","Pervaiz_Muhsaraf","Nawaz SHariff","Babar Azam","Hasina Wajid"]
l2 = ["posted his pic","riding donkey","went t wahroom","opened his mouth","created a tunnel"]
l3 = ["at Minar-E-Pakistan","in his bathroom","at gulgasht","at Anar kali Bazar","On the top of Mountain"]
ab = random.choice(l1)
bc = random.choice(l2)
cd = random.choice(l3)
allo = ab + " "+ bc + " " + cd 
while True:
 ask_1 = input("Do you want to generate Fake News(y/n)? ").lower()
 if ask_1=="y":
  ask = input("For which field, Do you want to generate fake news: (sports/politics/wwe/coding/random)? ").lower()
  if ask == "sports":
   def sports():
    list1_sports_objects =["Ronaldo","MBABE","BHOLU"]
    list2_sports_actions =["Goaled a score","Pooped","Shocked"]  
    list3_sports_place = ["In the Antartica","At the top of plan","while sitting at the top of  burj khalifa :))))"]
    oa,ob,oc = random.choice(list1_sports_objects),random.choice(list2_sports_actions),random.choice(list3_sports_place)
    return (f"{oa} {ob} {oc}")
   av = sports()
   print(av)
   ask_3 = input("Do you want to store it in text file?: ") 
   if ask_3=="y":
    with open("fake_news.txt","a") as f:
     f.write(av)
   else:
    continue
 
  if ask == "politics":
   def politics():
    list1_politics_objects =["Kharbuza Sharif","Mariyuum Kawaz","Goated Bilawl GHUTTO"]
    list2_politics_actions =["Panicked","became unconsious","worked hard"]  
    list3_politics_place = ["In the America","At her palace","while sitting at the top of burj khalifa :))))"]
    oa,ob,oc = random.choice(list1_politics_objects),random.choice(list2_politics_actions),random.choice(list3_politics_place)
    return (f"{oa} {ob} {oc}")
   av = politics()
   print(av)
   ask_3 = input("Do you want to store it in text file?: ") 
   if ask_3=="y":
    with open("fake_news.txt","a") as f:
     f.write(av)
   else:
    continue
  if ask == "wwe":
     def wwe():
      list1_wwe_objects =["Roman_Reigns","John Cena","Seth Freakin Rollins"]
      list2_wwe_actions =["Speared","Hitted Double AA","stomped"]  
      list3_wwe_place = [" Stephani  at Bani Gala","The President OF AMERICA MR DOLAND TRUMP","at the top of burj khalifa :))))"]
      oa,ob,oc = random.choice(list1_wwe_objects),random.choice(list2_wwe_actions),random.choice(list3_wwe_place)
      return (f"{oa} {ob} {oc}")
     av = wwe()
     print(av)
     ask_3 = input("Do you want to store it in text file?: ") 
     if ask_3=="y":
      with open("fake_news.txt","a") as f:
       f.write(av)
     else:
      continue
  if ask == "coding":
     def coding():
      list1_coding_objects =["Barakallah","Muteeb","Goated Hassan RAZA"]
      list2_coding_actions =["became pro","became extremely good","is still noob"]  
      list3_coding_place = ["after getting degree from University of EdinBurg and can become space scientist after completing every aspect of AI","At python","in many things include python :))))"]
      oa,ob,oc = random.choice(list1_coding_objects),random.choice(list2_coding_actions),random.choice(list3_coding_place)
      return(f"{oa} {ob} {oc}")
     av = coding()
     print(av)
     ask_3 = input("Do you want to store it in text file?: ") 
     if ask_3=="y":
      with open("fake_news.txt","a") as f:
       f.write(av)
     else:
      continue
  if ask == "random":
   print(allo)
 else:
  break
  
 
