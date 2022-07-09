import time
import sys
import itertools
import threading
import datetime
from flights import *
from payment import *
from flights2 import *

def welcome():
  print("\nWelcome to Tangina Airlines")

  print("\nOne way or roundtrip flight?")
  print("Press 1 if One way")
  print("Press 2 if Round trip\n")
welcome()

choice = input()
if choice == "1":
    origin = input("\nFrom: ")
    destination = str(input("Destination: "))
    departure_date = str(input("Departure date: (in MM/DD/YYYY): "))
    departuredate = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
elif choice == "2":
    origin = input("\nFrom: ")
    destination = str(input("Destination: "))
    departure_date = str(input("Departure date: (in MM/DD/YYYY): "))
    departuredate = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
    returning_date = str(input("Returning date: (in MM/DD/YYYY): "))
    returndate = datetime.datetime.strptime(returning_date, "%m/%d/%Y").date()


guests = int(input("How many adults: "))
guests_1 = int(input("How many children: "))
guests_2 = int(input("How many infants: "))

total_guest = guests + guests_1 + guests_2
print()
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(6)
done = True


print("\n\n--------------------------------------------------------------------------")
# cebu condtion
#def decision_roundtrip():
#    if (choice == "2" and destination == "Cebu" and departure_date == "06/01/2022"):
#        print("\nSCHEDULES                     PRICES\n")
#        print(cebutomanilajune1)




def decision_oneway():

   if (choice == "1" and destination == "Cebu" and departure_date == "06/01/2022"):
       print("\nSCHEDULES                     PRICES\n")
       print(cebu_june1)
   elif (choice == "1" and destination == "Cebu" and departure_date == "06/02/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june2_price = "₱ 1,500"
       #cebu_june2_price2 = "₱ 1,540"
       #cebu_june2_price3 = "₱ 2,190"
       #cebu_june2_price4 = "₱ 2,123"
       #cebu_june2_price5 = "₱ 2,001"
       #cebu_june2_price6 = "₱ 4,190"
       print(cebu_june2)
   elif (choice == "1" and destination == "Cebu" and departure_date == "06/03/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june3)
   elif (choice == "1" and departure_date == "06/04/2022" and destination == "Cebu"):
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june4)
   elif (choice == "1" and departure_date == "06/05/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june5_price = "₱ 1,500"
       #cebu_june5_price2 = "₱ 1,540"
       #cebu_june5_price3 = "₱ 2,190"
       #cebu_june5_price4 = "₱ 2,123"
       #cebu_june5_price5 = "₱ 2,001"
       #cebu_june5_price6 = "₱ 4,190"
       print(cebu_june5)
   elif choice == "1" and departure_date == "06/06/2022" and destination == "Cebu":
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june6_price = "₱ 1,500"
       #cebu_june6_price2 = "₱ 1,540"
       #cebu_june6_price3 = "₱ 2,190"
       #cebu_june6_price4 = "₱ 2,123"
       #cebu_june6_price5 = "₱ 2,061"
       #cebu_june6_price6 = "₱ 4,180"
       print(cebu_june6)
   elif choice == "1" and departure_date == "06/07/2022" and destination == "Cebu":
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june7_price = "₱ 1,600"
       #cebu_june7_price2 = "₱ 1,740"
       #cebu_june7_price3 = "₱ 2,190"
       #cebu_june7_price4 = "₱ 2,123"
       #cebu_june7_price5 = "₱ 2,061"
       #cebu_june7_price6 = "₱ 4,180"
       print(cebu_june7)
   elif choice == "1" and departure_date == "06/08/2022" and destination == "Cebu":
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june8)
   elif choice == "1" and departuredate == "06/09/2022" and destination == "Cebu":
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june9)
   elif choice == "1" and departure_date == "06/10/2022" and destination == "Cebu":
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june10_price = "₱ 1,500"
       #cebu_june10_price2 = "₱ 3,890"
       #cebu_june10_price3 = "₱ 4,010"
       #cebu_june10_price4 = "₱ 4,501"
       #cebu_june10_price5 = "₱ 5,109"
       #cebu_june10_price6 = "₱ 6,728"
       print(cebu_june10)
   elif choice == "1" and departure_date == "06/11/2022" and destination == "Cebu":
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june11_price = "₱ 1,500"
       #cebu_june11_price2 = "₱ 3,890"
       #cebu_june11_price3 = "₱ 4,010"
       #cebu_june11_price4 = "₱ 4,501"
       #cebu_june11_price5 = "₱ 5,109"
       #cebu_june11_price6 = "₱ 6,728"
       print(cebu_june11)
   elif (choice == "1" and departure_date == "06/12/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june12_price = "₱ 1,500"
       #cebu_june12_price2 = "₱ 3,890"
       #cebu_june12_price3 = "₱ 4,010"
       #cebu_june12_price4 = "₱ 4,501"
       #cebu_june12_price5 = "₱ 5,109"
       #cebu_june12_price6 = "₱ 6,721"
       print(cebu_june12)
   elif (choice == "1" and departure_date == "06/13/2022" and destination == "Cebu"):
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june13)
   elif (choice == "1" and departure_date == "06/14/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june14_price = "₱ 1,500"
       #cebu_june14_price2 = "₱ 3,890"
       #cebu_june14_price3 = "₱ 4,010"
       #cebu_june14_price4 = "₱ 4,501"
       #cebu_june14_price5 = "₱ 5,109"
       #cebu_june14_price6 = "₱ 6,721"
       print(cebu_june14)
   elif (choice == "1" and departure_date == "06/15/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june15_price = "₱ 1,500"
       #cebu_june15_price2 = "₱ 3,890"
       #cebu_june15_price3 = "₱ 4,010"
       #cebu_june15_price4 = "₱ 4,601"
       #cebu_june15_price5 = "₱ 5,102"
       #cebu_june15_price6 = "₱ 6,721"
       print(cebu_june15)
   elif (choice == "1" and departure_date == "06/16/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june16_price = "₱ 1,500"
       #cebu_june16_price2 = "₱ 3,890"
       #cebu_june16_price3 = "₱ 4,010"
       #cebu_june16_price4 = "₱ 4,601"
       #cebu_june16_price5 = "₱ 5,102"
       #cebu_june16_price6 = "₱ 6,721"
       print(cebu_june16)
   elif (choice == "1" and departure_date == "06/17/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june17_price = "₱ 1,500"
       #cebu_june17_price2 = "₱ 3,890"
       #cebu_june17_price3 = "₱ 4,010"
       #cebu_june17_price4 = "₱ 4,601"
       #cebu_june17_price5 = "₱ 5,102"
       #cebu_june17_price6 = "₱ 6,721"
       print(cebu_june17)
   elif (choice == "1" and departure_date == "06/18/2022" and destination == "Cebu"):
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june18)
   elif (choice == "1" and departure_date == "06/19/2022" and destination == "Cebu"):
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june19)
   elif (choice == "1" and departure_date == "06/20/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june20_price = "₱ 2,500"
       #cebu_june20_price2 = "₱ 4,890"
       #cebu_june20_price3 = "₱ 2,010"
       #cebu_june20_price4 = "₱ 4,601"
       #cebu_june20_price5 = "₱ 4,102"
       #cebu_june20_price6 = "₱ 9,711"
       print(cebu_june20)
   elif (choice == "1" and departure_date == "06/21/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june21_price = "₱ 3,503"
       #cebu_june21_price2 = "₱ 4,890"
       #cebu_june21_price3 = "₱ 2,010"
       #cebu_june21_price4 = "₱ 4,601"
       #cebu_june21_price5 = "₱ 4,102"
       #cebu_june21_price6 = "₱ 7,711"
       print(cebu_june21)
   elif (choice == "1" and departure_date == "06/22/2022" and destination == "Cebu"):
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june22)
   elif (choice == "1" and departure_date == "06/23/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june23_price = "₱ 3,503"
       #cebu_june23_price2 = "₱ 5,890"
       #cebu_june23_price3 = "₱ 4,892"
       #cebu_june23_price4 = "₱ 3,401"
       #cebu_june23_price5 = "₱ 4,102"
       #cebu_june23_price6 = "₱ 10,711"
       print(cebu_june23)
   elif (choice == "1" and departure_date == "06/24/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june24_price = "₱ 3,503"
       #cebu_june24_price2 = "₱ 5,890"
       #cebu_june24_price3 = "₱ 4,892"
       #cebu_june24_price4 = "₱ 3,401"
       #cebu_june24_price5 = "₱ 4,102"
       #cebu_june24_price6 = "₱ 10,711"
       print(cebu_june24)
   elif (choice == "1" and departure_date == "06/25/2022" and destination == "Cebu"):
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june25)
   elif (choice == "1" and departure_date == "06/26/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june26_price = "₱ 2,389"
       #cebu_june26_price2 = "₱ 3,083"
       #cebu_june26_price3 = "₱ 4,971"
       #cebu_june26_price4 = "₱ 4,827"
       #cebu_june26_price5 = "₱ 5,082"
       #cebu_june26_price6 = "₱ 8,282"
       print(cebu_june26)
   elif (choice == "1" and departure_date == "06/27/2022" and destination == "Cebu"):
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june27)
   elif (departure_date == "06/28/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june28_price = "₱ 2,389"
       #cebu_june28_price2 = "₱ 3,083"
       #cebu_june28_price3 = "₱ 4,971"
       #cebu_june28_price4 = "₱ 4,827"
       #cebu_june28_price5 = "₱ 5,082"
       #cebu_june28_price6 = "₱ 9,282"
       print(cebu_june28)
   elif (choice == "1" and departure_date == "06/29/2022" and destination == "Cebu"):
       print("\nSCHEDULES                     PRICES\n")
       #cebu_june29_price = "₱ 2,389"
       #cebu_june29_price2 = "₱ 3,083"
       #cebu_june29_price3 = "₱ 8,971"
       print(cebu_june29)
   elif (choice == "1" and departure_date == "06/30/2022" and destination == "Cebu"):
       # print("\nSCHEDULES                     PRICES\n")
       print(cebu_june30)
   
   
   # boracay condition
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/01/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june1_price = "₱ 8,500"
       #Bora_june1_price2 = "₱ 2,800"
       #Bora_june1_price3 = "₱ 3,756"
       #Bora_june1_price4 = "₱ 3,500"
       #Bora_june1_price5 = "₱ 1,800"
       #Bora_june1_price6 = "₱ 1,756"
       print(Bora_june1)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/02/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june2_price = "₱ 6,500"
       #Bora_june2_price2 = "₱ 2,800"
       #Bora_june2_price3 = "₱ 3,756"
       #Bora_june2_price4 = "₱ 5,500"
       #Bora_june2_price5 = "₱ 7,800"
       #Bora_june2_price6 = "₱ 8,756"
       print(Bora_june2)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/03/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june3_price = "₱ 4,500"
       #Bora_june3_price2 = "₱ 1,800"
       #Bora_june3_price3 = "₱ 2,756"
       #Bora_june3_price4 = "₱ 5,500"
       #Bora_june3_price5 = "₱ 3,800"
       #Bora_june3_price6 = "₱ 1,756"
       print(Bora_june3)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/04/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Bora_june4)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/05/2022"):
       print("\nSCHEDULES                     PRICES\n")
      #Bora_june5_price = "₱ 2,500"
      #Bora_june5_price2 = "₱ 1,800"
      #Bora_june5_price3 = "₱ 8,000"
      #Bora_june5_price4 = "₱ 3,500"
      #Bora_june5_price5 = "₱ 5,800"
      #Bora_june5_price6 = "₱ 2,756"
       print(Bora_june5)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/06/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june6_price = "₱ 5,500"
       #Bora_june6_price2 = "₱ 1,800"
       #Bora_june6_price3 = "₱ 2,756"
       #Bora_june6_price4 = "₱ 7,500"
       #Bora_june6_price5 = "₱ 2,800"
       #Bora_june6_price6 = "₱ 2,756"
       print(Bora_june6)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/07/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june7_price = "₱ 2,500"
       #Bora_june7_price2 = "₱ 1,800"
       #Bora_june7_price3 = "₱ 6,756"
       #Bora_june7_price4 = "₱ 2,500"
       #Bora_june7_price5 = "₱ 3,800"
       #Bora_june7_price6 = "₱ 5,756"
       print(Bora_june7)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/08/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Bora_june8)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/09/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june9_price = "₱ 1,500"
       #Bora_june9_price2 = "₱ 2,600"
       #Bora_june9_price3 = "₱ 1,756"
       #Bora_june9_price4 = "₱ 3,500"
       #Bora_june9_price5 = "₱ 8,800"
       #Bora_june9_price6 = "₱ 2,000"
       print(Bora_june9)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/10/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june10_price = "₱ 9,500"
       #Bora_june10_price2 = "₱ 2,800"
       #Bora_june10_price3 = "₱ 3,756"
       #Bora_june10_price4 = "₱ 4,500"
       #Bora_june10_price5 = "₱ 5,800"
       #Bora_june10_price6 = "₱ 6,756"
       print(Bora_june10)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/11/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Bora_june11)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/12/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june12_price = "₱ 2,500"
       #Bora_june12_price2 = "₱ 1,800"
       #Bora_june12_price3 = "₱ 3,756"
       #Bora_june12_price4 = "₱ 4,500"
       #Bora_june12_price5 = "₱ 1,800"
       #Bora_june12_price6 = "₱ 3,756"
       print(Bora_june12)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/13/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june13_price = "₱ 3,500"
       #Bora_june13_price2 = "₱ 2,800"
       #Bora_june13_price3 = "₱ 1,756"
       #Bora_june13_price4 = "₱ 4,500"
       #Bora_june13_price5 = "₱ 2,800"
       #Bora_june13_price6 = "₱ 2,756"
       print(Bora_june13)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/14/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june14_price = "₱ 2,500"
       #Bora_june14_price2 = "₱ 8,800"
       #Bora_june14_price3 = "₱ 2,756"
       #Bora_june14_price4 = "₱ 3,500"
       #Bora_june14_price5 = "₱ 6,800"
       #Bora_june14_price6 = "₱ 4,756"
       print(Bora_june14)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/15/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june15_price = "₱ 1,500"
       #Bora_june15_price2 = "₱ 1,800"
       #Bora_june15_price3 = "₱ 1,756"
       #Bora_june15_price4 = "₱ 1,500"
       #Bora_june15_price5 = "₱ 1,800"
       #Bora_june15_price6 = "₱ 1,756"
       print(Bora_june15)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/16/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Bora_june16)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/17/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june17_price = "₱ 3,500"
       #Bora_june17_price2 = "₱ 2,800"
       #Bora_june17_price3 = "₱ 2,000"
       #Bora_june17_price4 = "₱ 4,500"
       #Bora_june17_price5 = "₱ 6,800"
       #Bora_june17_price6 = "₱ 3,756"
       print(Bora_june17)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/18/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june18_price = "₱ 2,500"
       #Bora_june18_price2 = "₱ 2,800"
       #Bora_june18_price3 = "₱ 1,756"
       #Bora_june18_price4 = "₱ 2,500"
       #Bora_june18_price5 = "₱ 1,800"
       #Bora_june18_price6 = "₱ 6,756"
       print(Bora_june18)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/19/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june19_price = "₱ 3,500"
       #Bora_june19_price2 = "₱ 3,000"
       #Bora_june19_price3 = "₱ 3,300"
       #Bora_june19_price4 = "₱ 1,500"
       #Bora_june19_price5 = "₱ 2,800"
       #Bora_june19_price6 = "₱ 2,756"
       print(Bora_june19)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/20/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Bora_june20)
   elif (destination == "Boracay" and departure_date == "06/21/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Bora_june21)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/22/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june22_price = "₱ 1,500"
       #Bora_june22_price2 = "₱ 4,800"
       #Bora_june22_price3 = "₱ 3,756"
       #Bora_june22_price4 = "₱ 8,500"
       #Bora_june22_price5 = "₱ 6,800"
       #Bora_june22_price6 = "₱ 3,756"
       print(Bora_june22)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/23/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june23_price = "₱ 1,500"
       #Bora_june23_price2 = "₱ 4,800"
       #Bora_june23_price3 = "₱ 5,000"
       #Bora_june23_price4 = "₱ 3,500"
       #Bora_june23_price5 = "₱ 4,800"
       #Bora_june23_price6 = "₱ 5,756"
       print(Bora_june23)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/24/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june24_price = "₱ 5,540"
       #Bora_june24_price2 = "₱ 4,830"
       #Bora_june24_price3 = "₱ 9,756"
       #Bora_june24_price4 = "₱ 7,500"
       #Bora_june24_price5 = "₱ 2,800"
       #Bora_june24_price6 = "₱ 4,756"
       print(Bora_june24)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/25/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june25_price = "₱ 6,500"
       #Bora_june25_price2 = "₱ 3,800"
       #Bora_june25_price3 = "₱ 4,756"
       #Bora_june25_price4 = "₱ 7,500"
       #Bora_june25_price5 = "₱ 4,800"
       #Bora_june25_price6 = "₱ 3,756"
       print(Bora_june25)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/26/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june26_price = "₱ 7,560"
       #Bora_june26_price2 = "₱ 2,850"
       #Bora_june26_price3 = "₱ 8,756"
       #Bora_june26_price4 = "₱ 5,500"
       #Bora_june26_price5 = "₱ 9,830"
       #Bora_june26_price6 = "₱ 10,756"
       print(Bora_june26)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/27/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june27_price = "₱ 6,500"
       #Bora_june27_price2 = "₱ 3,800"
       #Bora_june27_price3 = "₱ 7,756"
       #Bora_june27_price4 = "₱ 9,500"
       #Bora_june27_price5 = "₱ 3,800"
       #Bora_june27_price6 = "₱ 10,756"
       print(Bora_june27)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/28/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Bora_june28)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/29/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Bora_june29)
   elif (choice == "1" and destination == "Boracay" and departure_date == "06/30/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Bora_june30_price = "₱ 5,500"
       #Bora_june30_price2 = "₱ 6,800"
       #Bora_june30_price3 = "₱ 7,756"
       #Bora_june30_price4 = "₱ 5,500"
       #Bora_june30_price5 = "₱ 4,800"
       #Bora_june30_price6 = "₱ 4,756"
       print(Bora_june30)
   
   
   # BOHOL CONDITIONS
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/01/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(BOHOL_june1)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/02/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Bora_june2)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/03/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june3_price = "₱ 4,500"
       #BOHOL_june3_price2 = "₱ 6,800"
       #BOHOL_june3_price3 = "₱ 2,756"
       #BOHOL_june3_price4 = "₱ 5,500"
       print(BOHOL_june3)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/04/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june4_price = "₱ 3,500"
       #BOHOL_june4_price2 = "₱ 2,800"
       #BOHOL_june4_price3 = "₱ 4,756"
       print(BOHOL_june4)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/05/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june5_price = "₱ 2,500"
       #BOHOL_june5_price2 = "₱ 4,800"
       #BOHOL_june5_price3 = "₱ 5,030"
       print(BOHOL_june5)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/06/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june6_price = "₱ 2,540"
       #BOHOL_june6_price2 = "₱ 3,800"
       #BOHOL_june6_price3 = "₱ 4,756"
       print(BOHOL_june6)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/07/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june7_price = "₱ 2,500"
       #BOHOL_june7_price2 = "₱ 3,800"
       #BOHOL_june7_price3 = "₱ 4,756"
       #BOHOL_june7_price4 = "₱ 2,500"
       print(BOHOL_june7)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/08/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june8_price = "₱ 3,500"
       #BOHOL_june8_price2 = "₱ 2,800"
       #BOHOL_june8_price3 = "₱ 6,756"
       #BOHOL_june8_price4 = "₱ 3,500"
       #BOHOL_june8_price5 = "₱ 3,800"
       #BOHOL_june8_price6 = "₱ 4,756"
       print(BOHOL_june8)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/09/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june9_price = "₱ 4,500"
       #BOHOL_june9_price2 = "₱ 2,600"
       #BOHOL_june9_price3 = "₱ 3,756"
       #BOHOL_june9_price4 = "₱ 3,500"
       #BOHOL_june9_price5 = "₱ 2,800"
       print(BOHOL_june9)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/10/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june10_price = "₱ 5,520"
       #BOHOL_june10_price2 = "₱ 2,800"
       #BOHOL_june10_price3 = "₱ 3,756"
       #BOHOL_june10_price4 = "₱ 4,500"
       print(BOHOL_june10)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/11/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june11_price = "₱ 4,520"
       #BOHOL_june11_price2 = "₱ 2,840"
       #BOHOL_june11_price3 = "₱ 4,600"
       print(BOHOL_june11)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/12/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june12_price = "₱ 1,500"
       #BOHOL_june12_price2 = "₱ 1,800"
       print(BOHOL_june12)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/13/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june13_price = "₱ 3,500"
       #BOHOL_june13_price2 = "₱ 3,800"
       #BOHOL_june13_price3 = "₱ 4,756"
       #BOHOL_june13_price4 = "₱ 4,500"
       print(BOHOL_june13)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/14/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june14_price = "₱ 2,500"
       #BOHOL_june14_price2 = "₱ 3,800"
       #BOHOL_june14_price3 = "₱ 2,756"
       #BOHOL_june14_price4 = "₱ 3,500"
       #BOHOL_june14_price5 = "₱ 4,800"
       print(BOHOL_june14)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/15/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(BOHOL_june15)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/16/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(BOHOL_june16)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/17/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june17_price = "₱ 3,500"
       #BOHOL_june17_price2 = "₱ 2,800"
       #BOHOL_june17_price3 = "₱ 3,000"
       #BOHOL_june17_price4 = "₱ 4,500"
       print(BOHOL_june17)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/18/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june18_price = "₱ 3,500"
       #BOHOL_june18_price2 = "₱ 2,800"
       #BOHOL_june18_price3 = "₱ 4,756"
       #BOHOL_june18_price4 = "₱ 2,530"
       print(BOHOL_june18)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/19/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june19_price = "₱ 3,500"
       #BOHOL_june19_price2 = "₱ 4,040"
       #BOHOL_june19_price3 = "₱ 3,300"
       #BOHOL_june19_price4 = "₱ 3,500"
       #BOHOL_june19_price5 = "₱ 3,800"
       #BOHOL_june19_price6 = "₱ 2,756"
       print(BOHOL_june19)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/20/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june20_price = "₱ 5,500"
       #BOHOL_june20_price2 = "₱ 3,800"
       #BOHOL_june20_price3 = "₱ 3,756"
       #BOHOL_june20_price4 = "₱ 5,560"
       #BOHOL_june20_price5 = "₱ 4,800"
       print(BOHOL_june20)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/21/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(BOHOL_june21)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/22/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(BOHOL_june22)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/23/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june23_price = "₱ 2,510"
       #BOHOL_june23_price2 = "₱ 4,800"
       #BOHOL_june23_price3 = "₱ 5,000"
       #BOHOL_june23_price4 = "₱ 3,500"
       print(BOHOL_june23)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/24/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june24_price = "₱ 5,540"
       #BOHOL_june24_price2 = "₱ 4,830"
       #BOHOL_june24_price3 = "₱ 3,756"
       print(BOHOL_june24)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/25/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june25_price = "₱ 3,500"
       #BOHOL_june25_price2 = "₱ 4,800"
       #BOHOL_june25_price3 = "₱ 2,756"
       #BOHOL_june25_price4 = "₱ 3,500"
       print(BOHOL_june25)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/26/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june26_price = "₱ 4,560"
       #BOHOL_june26_price2 = "₱ 2,850"
       #BOHOL_june26_price3 = "₱ 4,756"
       #BOHOL_june26_price4 = "₱ 5,500"
       print(BOHOL_june26)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/27/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(BOHOL_june27)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/28/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june28_price = "₱ 6,500"
       #BOHOL_june28_price2 = "₱ 4,800"
       #BOHOL_june28_price3 = "₱ 3,756"
       #BOHOL_june28_price4 = "₱ 5,500"
       print(BOHOL_june28)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/29/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(BOHOL_june29)
   elif (choice == "1" and destination == "Bohol" and departure_date == "06/30/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #BOHOL_june26_price = "₱ 5,500"
       #BOHOL_june26_price2 = "₱ 3,800"
       #BOHOL_june26_price3 = "₱ 6,756"
       #BOHOL_june26_price4 = "₱ 4,500"
       print(BOHOL_june30)
   
   
   # PALAWAN SCHEDULES
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/01/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june1_price = "₱ 3,500"
       #Pal_june1_price2 = "₱ 4,040"
       #Pal_june1_price3 = "₱ 3,300"
       #Pal_june1_price4 = "₱ 3,500"
       print(Pal_june1)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/02/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june2_price = "₱ 5,500"
       #Pal_june2_price2 = "₱ 3,800"
       #Pal_june2_price3 = "₱ 3,756"
       #Pal_june2_price4 = "₱ 5,560"
       #Pal_june2_price5 = "₱ 4,800"
       print(Pal_june2)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/03/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june3_price = "₱ 6,489"
       #Pal_june3_price2 = "₱ 8,902"
       print(Pal_june3)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/04/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june4)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/05/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june5_price = "₱ 3,500"
       #Pal_june5_price2 = "₱ 4,040"
       #Pal_june5_price3 = "₱ 3,300"
       #Pal_june5_price4 = "₱ 3,500"
       print(Pal_june5)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/06/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june6_price = "₱ 5,500"
       #Pal_june6_price2 = "₱ 3,800"
       #Pal_june6_price3 = "₱ 3,756"
       #Pal_june6_price4 = "₱ 5,560"
       #Pal_june6_price5 = "₱ 4,800"
       print(Pal_june6)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/07/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june7_price = "₱ 5,500"
       #Pal_june7_price2 = "₱ 3,800"
       #Pal_june7_price3 = "₱ 3,756"
       #Pal_june7_price4 = "₱ 5,560"
       #Pal_june7_price5 = "₱ 4,800"
       print(Pal_june7)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/08/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june8)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/09/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june9)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/10/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june10_price = "₱ 5,500"
       #Pal_june10_price2 = "₱ 3,800"
       #Pal_june10_price3 = "₱ 3,756"
       #Pal_june10_price4 = "₱ 5,560"
       #Pal_june10_price5 = "₱ 4,800"
       print(Pal_june10)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/11/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june11_price = "₱ 6,489"
       #Pal_june11_price2 = "₱ 8,902"
       print(Pal_june11)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/12/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june12_price = "₱ 5,500"
       #Pal_june12_price2 = "₱ 3,800"
       #Pal_june12_price3 = "₱ 3,756"
       #Pal_june12_price4 = "₱ 5,560"
       #Pal_june12_price5 = "₱ 4,800"
       print(Pal_june12)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/13/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june13_price = "₱ 5,500"
       #Pal_june13_price2 = "₱ 3,800"
       #Pal_june13_price3 = "₱ 3,756"
       #Pal_june13_price4 = "₱ 5,560"
       #Pal_june13_price5 = "₱ 4,800"
       print(Pal_june13)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/14/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june14)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/15/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june15)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/16/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june16_price = "₱ 5,500"
       #Pal_june16_price2 = "₱ 3,800"
       #Pal_june16_price3 = "₱ 3,756"
       #Pal_june16_price4 = "₱ 5,560"
       #Pal_june16_price5 = "₱ 4,800"
       print(Pal_june16)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/17/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june17_price = "₱ 5,500"
       #Pal_june17_price2 = "₱ 3,800"
       #Pal_june17_price3 = "₱ 3,756"
       #Pal_june17_price4 = "₱ 5,560"
       #Pal_june17_price5 = "₱ 4,800"
       print(Pal_june17)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/18/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june18_price = "₱ 5,500"
       #Pal_june18_price2 = "₱ 3,800"
       #Pal_june18_price3 = "₱ 3,756"
       #Pal_june18_price4 = "₱ 5,560"
       #Pal_june18_price5 = "₱ 4,800"
       print(Pal_june18)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/19/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june19_price = "₱ 2,389"
       #Pal_june19_price2 = "₱ 3,083"
       #Pal_june19_price3 = "₱ 4,971"
       #Pal_june19_price4 = "₱ 4,827"
       #Pal_june19_price5 = "₱ 5,082"
       #Pal_june19_price6 = "₱ 8,282"
       print(Pal_june19)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/20/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june20)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/21/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june21)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/22/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june22_price = "₱ 3,500"
       #Pal_june22_price2 = "₱ 4,800"
       #Pal_june22_price3 = "₱ 2,756"
       #Pal_june22_price4 = "₱ 3,500"
       print(Pal_june22)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/23/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june23_price = "₱ 1,500"
       #Pal_june23_price2 = "₱ 2,600"
       #Pal_june23_price3 = "₱ 1,756"
       #Pal_june23_price4 = "₱ 3,500"
       #Pal_june23_price5 = "₱ 8,800"
       #Pal_june23_price6 = "₱ 2,000"
       print(Pal_june23)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/24/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june24_price = "₱ 3,500"
       #Pal_june24_price2 = "₱ 3,800"
       #Pal_june24_price3 = "₱ 4,756"
       #Pal_june24_price4 = "₱ 4,500"
       print(Pal_june24)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/25/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june25_price = "₱ 3,503"
       #Pal_june25_price2 = "₱ 5,890"
       #Pal_june25_price3 = "₱ 4,892"
       #Pal_june25_price4 = "₱ 3,401"
       #Pal_june25_price5 = "₱ 4,102"
       #Pal_june25_price6 = "₱ 10,711"
       print(Pal_june25)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/26/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june26)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/27/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june27)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/28/2022"):
       print("\nSCHEDULES                     PRICES\n")
      #Pal_june28_price = "₱ 3,500"
      #Pal_june28_price = "₱ 4,040"
      #Pal_june28_price = "₱ 3,300"
      #Pal_june28_price = "₱ 3,500"
       print(Pal_june28)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/29/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #Pal_june29_price = "₱ 5,500"
       #Pal_june29_price = "₱ 3,800"
       #Pal_june29_price = "₱ 3,756"
       #Pal_june29_price = "₱ 5,560"
       #Pal_june29_price = "₱ 4,800"
       print(Pal_june29)
   elif (choice == "1" and destination == "Palawan" and departure_date == "06/30/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(Pal_june30)
   
   # SIARGAO SCHEDULES
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/01/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june1_price = "₱ 1,600"
       #sia_june1_price = "₱ 1,740"
       #sia_june1_price = "₱ 2,190"
       #sia_june1_price = "₱ 2,123"
       #sia_june1_price = "₱ 2,061"
       #sia_june1_price = "₱ 4,180"
       print(sia_june1)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/02/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june2_price = "₱ 1,600"
       #sia_june2_price = "₱ 1,740"
       #sia_june2_price = "₱ 2,190"
       #sia_june2_price = "₱ 2,123"
       #sia_june2_price = "₱ 2,061"
       #sia_june2_price = "₱ 4,180"
       print(sia_june2)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/03/2022"):
       print("\nSCHEDULES                     PRICES\n")
      #sia_june3_price = "₱ 1,600"
      #sia_june3_price = "₱ 1,740"
      #sia_june3_price = "₱ 2,190"
      #sia_june3_price = "₱ 2,123"
       print(sia_june3)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/04/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june4_price = "₱ 1,600"
       #sia_june4_price = "₱ 1,740"
       #sia_june4_price = "₱ 2,190"
       #sia_june4_price = "₱ 2,123"
       #sia_june4_price = "₱ 2,061"
       #sia_june4_price = "₱ 4,180"
       print(sia_june4)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/05/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june5)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/06/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june6)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/07/2022"):
       print("\nSCHEDULES                     PRICES\n")
       sia_june7_price = "₱ 1,600"
       sia_june7_price = "₱ 1,740"
       print(sia_june7)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/08/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june8_price = "₱ 1,600"
       #sia_june8_price = "₱ 1,740"
       #sia_june8_price = "₱ 2,190"
       #sia_june8_price = "₱ 2,123"
       #sia_june8_price = "₱ 2,061"
       #sia_june8_price = "₱ 4,180"
       print(sia_june8)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/09/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june9_price = "₱ 3,600"
       #sia_june9_price = "₱ 4,740"
       #sia_june9_price = "₱ 4,190"
       #sia_june9_price = "₱ 5,123"
       #sia_june9_price = "₱ 5,061"
       #sia_june9_price = "₱ 6,180"
       print(sia_june9)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/10/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june10_price = "₱ 1,600"
       #sia_june10_price = "₱ 1,740"
       #sia_june10_price = "₱ 2,190"
       #sia_june10_price = "₱ 2,123"
       #sia_june10_price = "₱ 2,061"
       #sia_june10_price = "₱ 4,180"
       print(sia_june10)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/11/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june11_price = "₱ 4,600"
       #sia_june11_price = "₱ 4,740"
       #sia_june11_price = "₱ 4,190"
       #sia_june11_price = "₱ 5,123"
       #sia_june11_price = "₱ 5,061"
       #sia_june11_price = "₱ 6,180"
       print(sia_june11)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/12/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june12)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/13/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june13)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/14/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june14_price = "₱ 3,600"
       #sia_june14_price = "₱ 4,740"
       #sia_june14_price = "₱ 4,190"
       print(sia_june14)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/15/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june15_price = "₱ 3,600"
       #sia_june15_price = "₱ 4,740"
       print(sia_june15)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/16/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june16_price = "₱ 4,600"
       #sia_june16_price = "₱ 4,740"
       #sia_june16_price = "₱ 4,190"
       #sia_june16_price = "₱ 5,123"
       print(sia_june16)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/17/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june17)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/18/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june18_price = "₱ 4,600"
       #sia_june18_price = "₱ 4,740"
       #sia_june18_price = "₱ 4,190"
       #sia_june18_price = "₱ 5,123"
       #sia_june18_price = "₱ 5,061"
       #sia_june18_price = "₱ 6,180"
       print(sia_june18)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/19/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june19_price = "₱ 4,600"
       #sia_june19_price = "₱ 4,740"
       #sia_june19_price = "₱ 4,190"
       #sia_june19_price = "₱ 5,123"
       #sia_june19_price = "₱ 5,061"
       #sia_june19_price = "₱ 6,180"
       print(sia_june19)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/20/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june20_price = "₱ 7,123"
       #sia_june20_price = "₱ 8,061"
       #sia_june20_price = "₱ 9,180"
       print(sia_june20)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/21/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june21)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/22/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june22_price = "₱ 7,123"
       #sia_june22_price = "₱ 11,092"
       #sia_june22_price = "₱ 10,289"
       print(sia_june22)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/23/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june23)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/24/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june24)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/25/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june25_price = "₱ 7,829"
       #sia_june25_price = "₱ 10,092"
       print(sia_june25)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/26/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june26_price = "₱ 7,123"
       #sia_june26_price = "₱ 11,092"
       #sia_june26_price = "₱ 10,289"
       print(sia_june26)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/27/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june27)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/28/2022"):
       # print("\nSCHEDULES                     PRICES\n")
       print(sia_june28)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/29/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june29_price = "₱ 5,600"
       #sia_june29_price = "₱ 4,740"
       #sia_june29_price = "₱ 4,190"
       #sia_june29_price = "₱ 5,123"
       #sia_june29_price = "₱ 7,061"
       #sia_june29_price = "₱ 6,180"
       print(sia_june29)
   elif (choice == "1" and destination == "Siargao" and departure_date == "06/30/2022"):
       print("\nSCHEDULES                     PRICES\n")
       #sia_june30_price = "₱ 5,600"
       #sia_june30_price = "₱ 4,740"
       #sia_june30_price = "₱ 4,190"
       print(sia_june30)
decision_oneway()





# Roundtrip Condition
def roundtrip():
   if (choice == "2" and destination == "Cebu" and departure_date == "06/01/2022"):
      print("\nSCHEDULES                                            PRICES\n")
      print(cebutomanilajune1)
   elif (choice == "2" and destination == "Cebu" and departure_date == "06/02/2022"):
      print("\nSCHEDULES                                            PRICES\n")
      print(cebutomanilajune2)
   elif (choice == "2" and destination == "Cebu" and departure_date == "06/03/2022"):
      #print("\nSCHEDULES                     PRICES\n")
      print(cebutomanilajune3)
   elif (choice == "2" and destination == "Cebu" and departure_date == "06/04/2022"):
      #print("\nSCHEDULES                     PRICES\n")
      print(cebutomanilajune4)
   elif (choice == "2" and destination == "Cebu" and departure_date == "06/05/2022"):
      print("\nSCHEDULES                                            PRICES\n")
      print(cebutomanilajune5)
   elif (choice == "2" and destination == "Cebu" and departure_date == "06/06/2022"):
      print("\nSCHEDULES                                            PRICES\n")
      print(cebutomanilajune6)
   elif (choice == "2" and destination == "Cebu" and departure_date == "06/07/2022"):
      print("\nSCHEDULES                                            PRICES\n")
      print(cebutomanilajune7)
   elif (choice == "2" and destination == "Cebu" and departure_date == "06/08/2022"):
      #print("\nSCHEDULES                     PRICES\n")
      print(cebutomanilajune8)
   elif (choice == "2" and destination == "Cebu" and departure_date == "06/09/2022"):
      #print("\nSCHEDULES                     PRICES\n")
      print(cebutomanilajune9)
   elif (choice == "2" and destination == "Cebu" and departure_date == "06/10/2022"):
      print("\nSCHEDULES                                            PRICES\n")
      print(cebutomanilajune10)








































roundtrip()

















schedule_choose = input("Choose a flight schedule: ")
print("\n\n--------------------------------------------------------------------------")
print("\nPASSENGER INFORMATION\n")

if total_guest == 1:
      fname = input("First Name: ")
      lname = input("Last Name: ")
      birthdate = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality = input("Nationality: ")
      pwd = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number = input("Mobile Number: ")
      email = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number2 = input("Mobile Number: ")
      email_2 = input("Email Address: ")
elif total_guest == 2:
      fname = input("First Name: ")
      lname = input("Last Name: ")
      birthdate = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality = input("Nationality: ")
      pwd = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number = input("Mobile Number: ")
      email = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number2 = input("Mobile Number: ")
      email_2 = input("Email Address: ")

      print("\n\n--------------------------------------------------------------------------")
      print("\nSECOND PASSENGERS\n")

      fname_2 = input("First Name: ")
      lname_2 = input("Last Name: ")
      birthdate_2 = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date_2 = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality_2 = input("Nationality: ")
      pwd_2 = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number_2 = input("Mobile Number: ")
      email_2_2 = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number_2_2 = input("Mobile Number: ")
      email2_2 = input("Email Address: ")
elif total_guest == 3:
      fname = input("First Name: ")
      lname = input("Last Name: ")
      birthdate = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality = input("Nationality: ")
      pwd = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number = input("Mobile Number: ")
      email = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number2 = input("Mobile Number: ")
      email_2 = input("Email Address: ")


      print("\n\n--------------------------------------------------------------------------")
      print("\nSECOND PASSENGERS\n")

      fname_2 = input("First Name: ")
      lname_2 = input("Last Name: ")
      birthdate_2 = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date_2 = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality_2 = input("Nationality: ")
      pwd_2 = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number_2 = input("Mobile Number: ")
      email_2_2 = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number_2_2 = input("Mobile Number: ")
      email2_2 = input("Email Address: ")

#THIRD
      print("\n\n--------------------------------------------------------------------------")
      print("\nTHIRD PASSENGERS\n")

      fname_3 = input("First Name: ")
      lname_3 = input("Last Name: ")
      birthdate_3 = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date_3 = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality_3 = input("Nationality: ")
      pwd_3 = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number_3 = input("Mobile Number: ")
      email_3_3 = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number_3_3 = input("Mobile Number: ")
      email3_3 = input("Email Address: ")
elif total_guest == 4:
      fname = input("First Name: ")
      lname = input("Last Name: ")
      birthdate = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality = input("Nationality: ")
      pwd = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number = input("Mobile Number: ")
      email = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number2 = input("Mobile Number: ")
      email_2 = input("Email Address: ")

      print("\n\n--------------------------------------------------------------------------")
      print("\nSECOND PASSENGERS\n")

      fname_2 = input("First Name: ")
      lname_2 = input("Last Name: ")
      birthdate_2 = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date_2 = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality_2 = input("Nationality: ")
      pwd_2 = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number_2 = input("Mobile Number: ")
      email_2_2 = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number_2_2 = input("Mobile Number: ")
      email2_2 = input("Email Address: ")

#THIRD
      print("\n\n--------------------------------------------------------------------------")
      print("\nTHIRD PASSENGERS\n")

      fname_3 = input("First Name: ")
      lname_3 = input("Last Name: ")
      birthdate_3 = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date_3 = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality_3 = input("Nationality: ")
      pwd_3 = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number_3 = input("Mobile Number: ")
      email_3_3 = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number_3_3 = input("Mobile Number: ")
      email3_3 = input("Email Address: ")


#FOURTH
      print("\n\n--------------------------------------------------------------------------")
      print("\nFOURTH PASSENGERS\n")
      fname_4 = input("First Name: ")
      lname_4 = input("Last Name: ")
      birthdate_4 = str(input("Birthdate: (in MM/DD/YYYY): "))
      birth_date_4 = datetime.datetime.strptime(departure_date, "%m/%d/%Y").date()
      nationality_4 = input("Nationality: ")
      pwd_4 = input("I am a Person with Disability (Y/N): ")

      print("\nCONTACT INFORMATION\n")
      mobile_number_4 = input("Mobile Number: ")
      email_4_4 = input("Email Address: ")

      print("\nAlternate Contact Number(OPTIONAL)\n")
      mobile_number_4_4 = input("Mobile Number: ")
      email4_4 = input("Email Address: ")

print()
done = False
#here is the animation
def animate2():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate2)
t.start()

#long process here
time.sleep(6)
done = True
print("\n--------------------------------------------------------------------------")
p_option= input("Do you want to proceed to payment?(Y/N): ")
print("\n--------------------------------------------------------------------------")
if p_option == "Y":
 print("\n                 PAYMENT\n")
else:
 quit()

