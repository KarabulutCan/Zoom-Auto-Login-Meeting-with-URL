# Created by Can Karabulut & Çağrı Kuzulu
# https://github.com/KarabulutCan
# https://github.com/kuzulucagri

import webbrowser
from keyboard import press
import datetime,time
from datetime import datetime

dersListesi="Foreign Lang., Pazartesi 17:00,17:50",\
            "Grafik, SAL 17:00/17:50/18:40,17:00,17:50,18",\
            "Data Mining,""ÇAR 17:00/17:50",\
            "Sistem Kimliklendirme,ÇAR 18:40/19:30", \
            "Pattern Recog,""ÇAR 20:20/21:10.",\
            "Mikro,PER 17:00/17:50/18:40/19:30",\
            "Scientific,CUM 17:00/17:50",\


print("Listede ki ders sayısı: ",len(dersListesi))

x=1
i=0
while x<= len(dersListesi) and i<=len(dersListesi):
    print(f"{x}: {dersListesi[i]}",end="\n *********** \n")
    x+=1
    i+=1


class autoLogin():
    counter = 0
    while counter<=1000000000000:
        def zamanTespit():
            bugun=datetime.today().strftime('%A')

            zaman = datetime.today()

            saatNow = zaman.hour

            dakikaNow = zaman.minute

            saniyeNow = zaman.second

            print(f"Bugün : {bugun}, Saat: {saatNow}, Dakika: {dakikaNow} Saniye: {saniyeNow}")


            if bugun==("Monday") and saatNow==17 and (dakikaNow==00 or dakikaNow==50) and (saniyeNow==00 or saniyeNow==1):
                webbrowser.open('https://erciyes-edu-tr.zoom.us/j/97102730671?pwd=MTkzVGpSaE9CN2Mxb09jeFNEOTFSdz09') #FOREIGN LANGUAGE FOR BUSINESS I
                time.sleep(5)
                press("ENTER")
                print("Join with Audiye Tıklanıyor . Bekleyin")
                time.sleep(20)
                press("ENTER"*3)
            elif bugun==("Tuesday") and (saatNow==17 or saatNow==18) and (dakikaNow==00 or dakikaNow==50 or
                                                                          dakikaNow==40) and (saniyeNow==00 or saniyeNow==1):
                webbrowser.open('https://erciyes-edu-tr.zoom.us/j/91529219709?pwd=R0hLTngrakdtbzIwa1IvVEc1dGdIdz09')  #BİLGİSAYAR GRAFİK
                time.sleep(5)
                press("ENTER")
                print("Join with Audiye Tıklanıyor . Bekleyin")
                time.sleep(20)
                press("ENTER"*3)
            elif bugun==("Wednesday") and saatNow==17 and (dakikaNow==00 or dakikaNow==50) and (saniyeNow==00 or saniyeNow==1): #INTRODUCTION TO DATA
                # MINING
                webbrowser.open('https://erciyes-edu-tr.zoom.us/j/91526203306?pwd=YTZObnN5V3ZjT2h1czFFR3RJT2p5QT09')
                time.sleep(5)
                press("ENTER")
                print("Join with Audiye Tıklanıyor . Bekleyin")
                time.sleep(20)
                press("ENTER"*3)
            elif bugun==("Wednesday") and (saatNow==18 or saatNow==19) and (dakikaNow==30 or dakikaNow==40) and (saniyeNow==00 or saniyeNow==1):
                #Sistem Kimliklendirme ve Modelleme
                webbrowser.open('https://erciyes-edu-tr.zoom.us/j/92044131818?pwd=M2tGLzZjblNvelV0RjY4VFdJN3l1UT09')
                time.sleep(5)
                press("ENTER")
                print("Join with Audiye Tıklanıyor . Bekleyin")
                time.sleep(20)
                press("ENTER"*3)
            elif bugun==("Wednesday") and (saatNow==20 or saatNow==21) and (dakikaNow==20 or dakikaNow==10) and (saniyeNow==00 or saniyeNow==1):
                #INTRODUCTION Pattern
                webbrowser.open('https://erciyes-edu-tr.zoom.us/j/98064919497?pwd=aUN1ZmNjY1Fpd3g0aHV4SmdoOUZBUT09')
                time.sleep(5)
                press("ENTER")
                print("Join with Audiye Tıklanıyor . Bekleyin")
                time.sleep(20)
                press("ENTER"*3)
            elif bugun==("Thursday") and (saatNow==17 or saatNow==18 or saatNow==19) and (dakikaNow==00 or dakikaNow==30
                                                                                          or dakikaNow==40 or
                                                                                          dakikaNow==50) and (saniyeNow==00 or saniyeNow==1):
                #MICROPROCESSORS
                webbrowser.open('https://erciyes-edu-tr.zoom.us/j/91317557274?pwd=UEdmSkNzRUhnVlMxWXlRTmhtTW9tQT09')
                time.sleep(5)
                press("ENTER")
                print("Join with Audiye Tıklanıyor . Bekleyin")
                time.sleep(20)
                press("ENTER"*3)
            elif bugun==("Friday") and saatNow==17 and (dakikaNow==00 or dakikaNow==50) and (saniyeNow==00 or saniyeNow==1) :
                webbrowser.open('https://erciyes-edu-tr.zoom.us/j/93601453898?pwd=WWMrREROVm5QN3hjdUFDdEdzVmRnUT09') #	SCIENTIFIC PROGRAMMING
                time.sleep(5)
                press("ENTER")
                print("Join with Audiye Tıklanıyor . Bekleyin")
                time.sleep(20)
                press("ENTER"*3)
            else:
                print(f"Bu saat ve tarihte herhangi bir ders yok")
        counter+=1
        time.sleep(1)



        zamanTespit()


