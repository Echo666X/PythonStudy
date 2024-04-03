#curdate.py
import datetime
curDate = datetime.datetime.now()
print(curDate.year,"-",curDate.month,"-",curDate.day,"\n",\
    curDate.hour,":",curDate.minute,":",curDate.second)
print(type(curDate))

#"对象名.属性名"  获取对象的属性值