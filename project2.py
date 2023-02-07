import pandas as pd
import requests
import re
from csv import writer
# from docx import Document

from bs4 import BeautifulSoup
full_name=[]
designation=[]
email_id=[]
contact=[]
area=[]
all=[]

# *********************NIT Kkr************************

r=requests.get("https://nitkkr.ac.in/?page_id=791")
soup = BeautifulSoup(r.content, 'html.parser')
# box=soup.find_all("section",class_ ="annoucements_sec")

tag=soup.find_all("div",class_ ="ans_block")
# print(tag)
for i in tag:
    name=i.h3.text
    full_name.append(name)
    des=i.find("div",class_ ="left-sec").text.split(':')[1].split('\n')[0]
    designation.append(des)
    email=i.find("div",class_ ="left-sec").text.split(':')[3].split('\n')[0]
    email_id.append(email)
    con=i.find("div",class_ ="left-sec").text.split(':')[4].split('\n')[0]
    contact.append(con)
    interest=i.find("div",class_ ="left-sec").p.text
    area.append(interest)


# print(full_name)



# *********************NIT Trichy****************************
r1=requests.get("https://www.nitt.edu/home/academics/departments/cse/faculty/")
soup1 = BeautifulSoup(r1.content, 'html.parser')
box1=soup1.find("div",id="contentcontainer")

n=box1.find_all('h2')
# print(n)
for i in n:
    if "Head of the Department" in i.text:
        designation.append("Head of the Department")
    elif "Professor (HAG)" in i.text:
        designation.append("Professor (HAG)")
    elif "Associate Professors" in i.text:
        for j in range(5):
            designation.append("Associate Professor")

    elif "Assistant Professors" in i.text:
        for j in range(14):
            designation.append("Assistant Professor")

    elif "Professors" in i.text:
        for j in range(4):
            designation.append("Professor")




tag1=soup1.find_all("div",class_="facitem left")
# print(tag1)
for i in tag1:
    name=i.h1.text
    full_name.append(name)
    interest=i.p.text
    area.append(interest)
    contact.append("0431-2503204")


email_id.append("-")
for link in box1.find_all('a'):
    l=link.get('href')       
    cl=l[0:len(l)-1]+ "@nitt.edu"
    if email_id.count(cl)==0:
        email_id.append(cl)

# email_id.append("-")
# print(email_id) 
# print(full_name)
# print(len(full_name))
# print(len(designation))
# print(len(area))
# print(len(contact))
# print(len(email_id))

# *******************NIT Rourkela******************
r2=requests.get("https://website.nitrkl.ac.in/Academics/AcademicDepartments/Faculty.aspx?fgdhwe34=Q1M6Q29tcHV0ZXIgU2NpZW5jZSBhbmQgRW5naW5lZXJpbmc%3d-MBb7wMG%2fNVo%3d")
soup2 = BeautifulSoup(r2.content, 'html.parser')
box2=soup2.find("div",class_ ="blog-page-area sec-spacer")
tag2=box2.find_all("div",class_ ="blog-content-faculty")
# print(tag2)
for i in tag2:
    name=i.h4.text
    full_name.append(name)
    des=i.find("div",class_ ="col-md-8").p.text
    designation.append(des)
    email=i.find("div",class_ ="col-md-6").text.split()[0]
    email_id.append(email)
    con=i.find("div",class_ ="col-md-6").text.split()[1]
    contact.append(con)
    interest=i.select_one('p[style="text-align:justify;"]').text
    area.append(interest)

# print(contact)




# **********************NIT Wrangal***********************
r3=requests.get("https://wsdc.nitw.ac.in/facultynew/dept/faculty_profiles/cse")
soup3 = BeautifulSoup(r3.content, 'html.parser')
box3=soup3.find("div",class_ ="col-lg-9 col-sm-9")
# print(box3)
tag3=box3.find_all("div",class_ ="cardm")
for i in tag3:
    name=i.strong.text
    full_name.append(name)
    des=i.b.text
    designation.append(des)
    email=i.find_all('a')[1].text
    email_id.append(email)
    con=i.find_all('p')[2].text
    contact.append(con)
    interest=i.find_all('p')
    if len(interest)>4:
       area.append(interest[4].text)
    else:
        area.append("-")

   

# for i in box3.find_all('a'):
#     email=''.join(i.find_all(text=True)).split()[0]
#     if "@nitw.ac.in" in email:
#        email_id.append(email)



# **********************NIT NAGPUR************************

r4 = requests.get("https://vnit.ac.in/cse/index.php/faculty/")   
soup4 = BeautifulSoup(r4.content, 'html.parser')

profs=soup4.find_all("tbody")

for prof in profs:
    ptags=prof.find_all("td")
    for ps in ptags:
        info=ps.text
        if(info.find("Name")>=0):
            lst=info.split(':')
            name=ps.text.split(":")[1].split("\n")[0]
            des=ps.text.split(":")[2].split("\n")[0]
            con=ps.text.split(":")[5].split("\n")[0]
            email= ps.text.split(":")[6].split("\n")[0].replace("[at]","@").replace("[dot]",".")
            interest= ps.text.split(":")[4].split("\n")[0]
            full_name.append(name)
            designation.append(des)
            contact.append(con)
            email_id.append(email)
            area.append(interest)
           
    

# print(len(email_id))
# print(len(designation))

# *********************NIT ALLAHABAD****************************
r5=requests.get("http://www.mnnit.ac.in/index.php/department/engineering/cm/cmfp")
soup5 = BeautifulSoup(r5.content, 'html.parser')
# box5=soup5.find('"div",class_ ="item-page"')
box5=soup5.find('tbody')
ids=['48','49','41','37']

for i in box5.find_all("p",class_ ="MsoNormal"):
    name=i.text
    full_name.append(name)


count=0
for i in ids:
 num=str(i)
 tag5=box5.find_all("table",id="table"+num)
 for j in tag5:
    # print(j.text)
    # des=j.select_one('span[style="color: #000000; font-family: verdana, geneva; font-size: 13.3333px;"]')
    des=j.find_all('tr')[0].text.split('\n')[2]
    designation.append(des)
    email=j.find_all('tr')[4].text.split('\n')[2]
    email_id.append(email)
    con=j.find_all('tr')[3].text.split('\n')[2]
    contact.append(con)
    interest=j.find_all('tr')[2].text.split('\n')[2]
    area.append(interest)



# print(len(full_name))
# print(len(designation))
# print(len(area))
# print(len(contact))
# print(len(email_id))

# ********************NIT SURAT***********************

# urls=["https://www.svnit.ac.in/web/department/chemical/faculty.php","https://www.svnit.ac.in/web/department/computer/faculty.php"]



# # for url in urls:
# r6=requests.get("https://www.svnit.ac.in/web/department/computer/faculty.php")
# #  r6=requests.get(url)
# soup6 = BeautifulSoup(r6.content, 'html.parser')
 
# box6=soup6.find("main",id="main")
# tag6=box6.find_all("div",class_ ="col-xs-12 col-sm-8 col-lg-10 remove_space")
# for i in tag6:
#      name=i.h4.text
#      full_name.append(name)
#      con=i.find('strong').text
#      contact.append(con)
#      des=i.find('p').text.split('\n')[0]
#      interest=i.find('p').text.split('\n')[1]
#      designation.append(des)
#      area.append(interest)
#      email=i.find("div",class_ ="col-lg-8 col-xs-12 col-sm-12").text
#      email_id.append(email)






# r6_1=requests.get("https://www.svnit.ac.in/web/department/chemical/faculty.php")
# #  r6=requests.get(url)
# soup6_1 = BeautifulSoup(r6_1.content, 'html.parser')
 
# box6_1=soup6_1.find("main",id="main")
# tag6_1=box6_1.find_all("div",class_ ="col-xs-12 col-sm-8 col-lg-10 remove_space")
# for i in tag6_1:
#      name=i.h4.text
#      full_name.append(name)
#      con=i.find('strong').text
#      contact.append(con)
#      des=i.find('p').text.split('\n')[0]
#      interest=i.find('p').text.split('\n')[1]
#      designation.append(des)
#      area.append(interest)
#      email=i.find("div",class_ ="col-lg-8 col-xs-12 col-sm-12").text
#      email_id.append(email)
    


# print(full_name)
# print(len(full_name))
# print(len(designation))
# print(len(area))
# print(len(contact))
# print(len(email_id))


# *********************NIT RAIPUR*******************************
# r7=requests.get("http://www.nitrr.ac.in/aboutcse.php")
# soup7 = BeautifulSoup(r7.content, 'html.parser')
# box7=soup7.find("div",id="menu3")
# # print(box7)
# box7_1=box7.find("div",class_ ="container hidden-sm hidden-md hidden-lg")
# # print(box7_1)
# tag7=box7_1.find_all('tbody')[1]
# name=tag7.find_all('a')
# for i in name:
#     full_name.append(i.text)

# des=tag7.find_all('td')[2]
# # print(des)

r7=requests.get("http://www.nitrr.ac.in/aboutcse.php")
soup7 = BeautifulSoup(r7.content, 'html.parser')
box7=soup7.find("div",id="menu3")
box7_1=box7.find_all("tbody")


# print(box7_1[1].text)

rows=box7_1[1].find_all("tr")
count=0
for row in rows:
    count+=1
    if count<3:
        continue
    # print("Row: "+row.text)
    tds=row.find_all("td")
    full_name.append(tds[0].text.strip())
    designation.append(tds[2].text.strip())
    contact.append(tds[3].text)
    area.append(tds[4].text)
    # print(area)
    email_id.append("")

    


# print(len(full_name))
# print(len(designation))
# print(len(area))
# print(len(contact))
# print(len(email_id))




# ******************NIT SRINAGAR********************
r8=requests.get("https://nitsri.ac.in/Pages/FacultyList.aspx?nDeptID=cs")
soup8 = BeautifulSoup(r8.content, 'html.parser')
box8=soup8.find("div",class_ ="gdlr-core-pbf-element")
# print(box8)
tag8=box8.find_all("div",class_ ="gdlr-core-personnel-list-content-wrap")
for i in tag8:
    name=i.find('a').text
    full_name.append(name)
    des=i.find("div",class_ ="gdlr-core-personnel-list-position gdlr-core-info-font gdlr-core-skin-caption").text
    designation.append(des)
    email=i.find("div",class_ ="kingster-personnel-info-list kingster-type-email").text
    email_id.append(email)
    con=i.find("div",class_ ="kingster-personnel-info-list kingster-type-phone").text
    contact.append(con)
    interest=i.find("div",class_ ="gdlr-core-personnel-list-content").text
    area.append(interest)



# print(len(full_name))
# print(len(designation))
# print(len(area))
# print(len(contact))
# print(len(email_id))


# ********************NIT MEGHALAYA**********************
num=0
r9=requests.get("http://www.manit.ac.in/faculty-information")
soup9 = BeautifulSoup(r9.content, 'html.parser')
box9=soup9.find("div",id="accordion")

box9_1=box9.find("div",id="collapse6")
tag9_1=box9_1.find_all("div",class_ ="col-xs-12 col-sm-9 col-md-9 pdleft")
for i in tag9_1:
    #  d=i.find_all('p')
    #  if(len(d)==7):
    #   name=i.find('strong').text
    #   full_name.append(name)
    #   des=i.find_all('p')[1].text
    #   designation.append(des)
    #   email=i.find_all('p')[3].text
    #   print(interest)
    a=i.text
    all.append(a)
    


print(len(full_name))
print(len(designation))
print(len(area))
print(len(contact))
print(len(email_id))



# ************************MNNIT*******************************
import requests
from bs4 import BeautifulSoup
url10 = "http://www.mnnit.ac.in/"

r10 = requests.get(url10)

htmlcontent = r10.content

soup10 = BeautifulSoup(htmlcontent,'html.parser')

navitems = soup10.find('li',class_='item-669')
print(navitems.find('a').text)
eng = navitems.find('li',class_='item-695')
print(eng.find('a').text)
departments = eng.find_all('li',class_='parent')
for dept in departments:
    # print(dept.find('a').text)
    allmenu = dept.find_all('a')
    for opt in allmenu:
        facul = opt.text
        if(facul=='Faculty Profile'):
            facultyurl = opt.get('href')
            faculurl = "http://www.mnnit.ac.in"+facultyurl
            facultyreq = requests.get(faculurl)
            facultycontent = facultyreq.content
            faculsoup = BeautifulSoup(facultycontent,'html.parser')
            
            teachtable = faculsoup.find('table')
            teachrow = teachtable.find_all('tr')
            for teachers in teachrow:
                # print(teachers.text.strip())
                a=teachers.text.strip()
                all.append(a)
                print('')































df=pd.DataFrame({"Full Name": full_name,"Designation":designation,"Email Id":email_id,"Contact":contact,"Area of Interest":area})
df1=pd.DataFrame({"INFOr": all})
# df1.to_csv("all.csv")
# # # df=pd.DataFrame({"Designation":designation})
df.to_excel("nit_all.xlsx")



    
    


    


