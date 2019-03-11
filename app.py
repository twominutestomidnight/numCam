from getCamNum import getStartPeopleValue
from printResult import printRes
import datetime
import pandas
from camera import Camera
df = pandas.read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name shop'])
camerasArray = []
for index in range(len(df)):
    camerasArray.append(Camera(ip=df.iloc[index][0],port=df.iloc[index][1],
                               login = df.iloc[index][2],password = df.iloc[index][3],
                               desc=df.iloc[index][4]))
'''
result = open("test.csv", "w")
result.write("Time perion\t00:00-01:00\t01:00-02:00\t02:00-03:00\t03:00-04:00\t04:00-05:00\t05:00-06:00\t"
             "06:00-07:00\t07:00-08:00\t08:00-09:00\t09:00-10:00\t10:00-11:00\t"
             "11:00-12:00\t12:00-13:00\t13:00-14:00\t14:00-15:00\t15:00-16:00\t16:00-17:00\t17:00-18:00\t"
             "18:00-19:00\t19:00-20:00\t20:00-21:00\t21:00-22:00\t22:00-23:00\t23:00-24:00\n")
'''
st = "{}-{}-{}.csv".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
result = open(st, "w")
result.write("{}-{}-{} \n".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
result.write("Time perion\t00:00-01:00\t01:00-02:00\t02:00-03:00\t03:00-04:00\t04:00-05:00\t05:00-06:00\t"
             "06:00-07:00\t07:00-08:00\t08:00-09:00\t09:00-10:00\t10:00-11:00\t"
             "11:00-12:00\t12:00-13:00\t13:00-14:00\t14:00-15:00\t15:00-16:00\t16:00-17:00\t17:00-18:00\t"
             "18:00-19:00\t19:00-20:00\t20:00-21:00\t21:00-22:00\t22:00-23:00\t23:00-24:00\n")
for camer in camerasArray:

    result.write("ip : {}\tname shop : {}\n".format(camer.ip,camer.desc))
    try:
        enter, exit = getStartPeopleValue(camer.ip, camer.port, camer.login, camer.password)

        printRes(enter, exit)
    except:
        result.write("error in data")
        print("error in data")
#print(camerasArray[1])
#for index, row in df.iterrows():
    #print(row['ip'])

#print(df.iloc[0],df.iloc[1])
#for i in range(0, len(df)):
 #   print(df.iloc[i]['ip'], df.iloc[i]['port'])
#get the values for a given column
#values = df['ip'].values
#print(values)
#get a data frame with selected columns

