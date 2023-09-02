from tkinter import * 
import phonenumbers
import folium 
import random
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz


root=Tk()
root.title("Phone Number Tracker")
root.geometry("999x509")
#icon
root.iconbitmap(r'C:\Users\buidu\OneDrive\Máy tính\code2\PYthon_only\project1\track.ico')
#root.resizable(False,False)

def Track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)
    

    #country
    locate=geocoder.description_for_number(number, 'en')
    country.config(text=locate)

    #operator like idea, airtel, jio
    operator=carrier.name_for_number(number, 'en')
    sim.config(text=operator)

    #phone timezon(khu vuc)
    time=timezone.time_zones_for_number(number)
    zone.config(text=time)
    
    #longtitude vs latitude
    geolocator= Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(locate)

    lng=location.longitude
    lat=location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)

    #time showing in phone
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    


def vitri4():
    #test code
    from phonenumbers import geocoder
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)
    Key= "43586076b60a425fa59e4fa5e35062da"
    from opencage.geocoder import OpenCageGeocode
    yourlocation = geocoder.description_for_number(number, 'en')
    geocoder = OpenCageGeocode(Key)

    query=str(yourlocation)
    results=geocoder.geocode(query)
    # print(results)

    lat=results[0]['geometry']['lat']
    lng=results[0]['geometry']['lng']
    print("VĨ ĐỘ: ",lat)
    print("KINH ĐỘ: ",lng)
    print("Đã lưu thông tin vị trí vào file myLocation.html!!!")
    
    #get location save html
    myMapp = folium.Map(location=[lat,lng],zoom_start=9)
    folium.Marker([lat,lng],popup=yourlocation).add_to((myMapp))
    #save map in html
    myMapp.save('myLocation.html')

#local button test
def infobox():
    import requests
    import argparse
    import json
    import folium
    if __name__ == "__main__":
        parser=argparse.ArgumentParser()
        parser.add_argument("-i","--ipaddress",help="Enter IP Address TO Track")
        args=parser.parse_args()
        ip=args.ipaddress
        ip=input(str("NHAP IP: "))
        url="http://ip-api.com/json/"+str(ip)
        res=requests.get(url)
        data=json.loads(res.content)
    #interface secondwindow
    global counter
    counter=1
    if counter<2:
        top = Toplevel()
        top.geometry("650x400")
        top.configure(bg="#AF601A")
        top.title("THÔNG TIN")
        my_label=Label(top,text="THÔNG TIN VỊ TRÍ",font=('Cascadia Code',20))
        my_label.pack()
    
        #IP vs IPinfor
        lbIP=Label(top,text="IP:",bg="#EFF213",fg='black',bd=5,font=('Cascadia Code',10,'bold'))
        lbIP.place(x=50,y=90)
        lbIP_infor=Label(top,text=False,bg="#EFF213",fg='black',bd=5,font=('Candara',10,'bold'))
        lbIP_infor.config(text=data['query'])
        lbIP_infor.place(x=150,y=90)

        
        #city vs cityinfor 
        lbCty=Label(top,text="Thành phố:",bg="#EFF213",fg='black',bd=5,font=('Cascadia Code',10,'bold'))
        lbCty.place(x=50,y=150)
        lbCty_infor=Label(top,text=False,bg="#EFF213",fg='black',bd=5,font=('Candara',10,'bold'))
        lbCty_infor.config(text=data['city'])
        lbCty_infor.place(x=150,y=150)

        #country vs infor
        lbCtry=Label(top,text="Đất Nước:",bg="#EFF213",fg='black',bd=5,font=('Cascadia Code',10,'bold'))
        lbCtry.place(x=50,y=200)
        lbCtry_infor=Label(top,text=False,bg="#EFF213",fg='black',bd=5,font=('Candara',10,'bold'))
        lbCtry_infor.config(text=data['countryCode'])
        lbCtry_infor.place(x=150,y=200)

        #region vs infor
        lbRe=Label(top,text="Khu vực:",bg="#EFF213",fg='black',bd=5,font=('Cascadia Code',10,'bold'))
        lbRe.place(x=50,y=250)
        lbRe_infor=Label(top,text=False,bg="#EFF213",fg='black',bd=5,font=('Candara',10,'bold'))
        lbRe_infor.config(text=data['regionName'])
        lbRe_infor.place(x=150,y=250)

        #ips vs infor
        lbIps=Label(top,text="IPS:",bg="#EFF213",fg='black',bd=5,font=('Cascadia Code',10,'bold'))
        lbIps.place(x=300,y=90)
        lbIps_infor=Label(top,text=False,bg="#EFF213",fg='black',bd=5,font=('Candara',10,'bold'))
        lbIps_infor.config(text=data['isp'])
        lbIps_infor.place(x=425,y=90)

        #ZIP vs infor
        lbZip=Label(top,text="ZIP:",bg="#EFF213",fg='black',bd=5,font=('Cascadia Code',10,'bold'))
        lbZip.place(x=300,y=150)
        lbZip_infor=Label(top,text=False,bg="#EFF213",fg='black',bd=5,font=('Candara',10,'bold'))
        lbZip_infor.config(text=data['zip'])
        lbZip_infor.place(x=425,y=150)

        #latitude(vi do) vs infor
        lbLa=Label(top,text="Latitude:",bg="#EFF213",fg='black',bd=5,font=('Cascadia Code',10,'bold'))
        lbLa.place(x=300,y=200)
        lbLa_infor=Label(top,text=False,bg="#EFF213",fg='black',bd=5,font=('Candara',10,'bold'))
        lbLa_infor.config(text=data['lat'])
        lbLa_infor.place(x=425,y=200)

        #longtitude(kinh do)
        lbLng=Label(top,text="Longtitude:",bg="#EFF213",fg='black',bd=5,font=('Cascadia Code',10,'bold'))
        lbLng.place(x=300,y=250)
        lbLng_infor=Label(top,text=False,bg="#EFF213",fg='black',bd=5,font=('Candara',10,'bold'))
        lbLng_infor.config(text=data['lon'])
        lbLng_infor.place(x=425,y=250)

        # #input ip button
        # lbinputIP=Label(top,text="Nhập ip: ",bg='red',font=('arial',17))
        # lbinputIP.place(x=50,y=40)
        # #input text
        # e=StringVar()
        # txtinputIP=Entry(top,textvariable=e,bg='blue',width=17,justify="left",bd=0,font=('arial',17))
        # txtinputIP.place(x=130,y=40)
        # txtinputIP.config(text=ip)
        #exit button
        my_butt=Button(top,text="Thoát",font=('arial',17),command=top.destroy)
        my_butt.pack(side=BOTTOM)
        counter +=1




#back ground
bg=PhotoImage(file=r'C:\Users\buidu\OneDrive\Máy tính\code2\PYthon_only\project1\background.png')
label1 = Label(root, image = bg)
label1.place(x = 0,y = 0)

#heading

'''Heading=Label(root,text="TÌM KIẾM GPS BẰNG SĐT!!",font=('arial',30,'bold'),compound=)
Heading.pack(side=TOP)'''
colors=['red','green','blue','yellow','pink','red2','gold2','gray','brown']
def introcolor():
    fg= random.choice(colors)
    sliderLaber.config(fg=fg)
    sliderLaber.after(20,introcolor)
def IntroLabelTick():
    global count,text
    if(count>=len(aa)):
        count =-1
        text=''
        sliderLaber.config(text=text)
    else:
        text = text + aa[count]
        sliderLaber.config(text=text)
        count +=1
    sliderLaber.after(100,IntroLabelTick)
#====================================
# Tao Thanh tieu de
aa=' TRACKING GPS BẰNG SỐ ĐIỆN THOẠI!! '
count =0
text =''
sliderLaber = Label(root,text=aa,font=('ROG Fonts',25,'italic bold'))
sliderLaber.pack(side=TOP)
IntroLabelTick()
introcolor()

#search text
Eback=PhotoImage(file=r"C:\Users\buidu\OneDrive\Máy tính\code2\PYthon_only\project1\sreach.png")
Label(root,image=Eback).place(x=50,y=80)

#entry/ghi so dien thoai
entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,justify="left",bd=0,font=('arial',17))
enter_number.place(x=80,y=93)

#search button
Search_image=PhotoImage(file=r"C:\Users\buidu\OneDrive\Máy tính\code2\PYthon_only\project1\search_btt.png")
search=Button(root,image=Search_image,bd=5,command=Track)
search.place(x=65,y=150)


#local button phones number
#local_image=PhotoImage(file='located.png')
findLocal=Button(root,text="VỊ TRÍ HIỆN TẠI",bg='red',bd=5,font=('arial',15),command=vitri4)
findLocal.place(x=400,y=350)
#label(imfomation)

#local button ipADDRESS
findIP=Button(root,text='TÌM KIẾM BẰNG IP',bg='red',bd=5,font=('arial',15),command=infobox)
findIP.place(x=650,y=350)
#country
country=Label(root,text="Đất Nước:",bg="#EFF213",fg='black',bd=5,font=('arial',20,'bold'))
country.place(x=400,y=90)
#sim
sim=Label(root,text="SIM:",bg="#EFF213",fg='black',bd=5,font=('arial',20,'bold'))
sim.place(x=400,y=170)
#timezone
zone=Label(root,text="Khu vực:",bg="#EFF213",fg='black',bd=5,font=('arial',20,'bold'))
zone.place(x=400,y=250)
#time
clock=Label(root,text="Thời gian:",bg="#EFF213",fg='black',bd=5,font=('arial',20,'bold'))
clock.place(x=650,y=90)
#longtiude
longitude=Label(root,text="Kinh độ:",bg="#EFF213",fg='black',bd=5,font=('arial',20,'bold'))
longitude.place(x=650,y=170)
#latitude
latitude=Label(root,text="Vĩ độ:",bg="#EFF213",fg='black',bd=5,font=('arial',20,'bold'))
latitude.place(x=650,y=250)


# map_widget=tkintermapview.TkinterMapView(my_label,width=450,height=450,corner_radius=0)
# map_widget.set_position(lat, lng)
# map_widget.set_marker(lat, lng, text="phone location")
# map_widget.set_zoom(10)
# map_widget.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
# map_widget.pack()

root.mainloop()