from getCamNum import getStartPeopleValue
from printResult import printRes
import datetime
import time
import threading
from datetime import timedelta
from pandas import read_excel
from camera import Camera
import argparse
import os.path
import itertools
import time
import sys
import configparser
import locale

'''

import json
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='config.json')
    return parser

parser = createParser()
namespace = parser.parse_args (sys.argv[1:])


with open(namespace.config) as config_file:
    config = json.load(config_file)

#save_path = config['path_to_save_file']
'''
if __name__ == '__main__':
    #while True:
        #config_ini = configparser.ConfigParser()
        #config_ini.read('config.ini')
        #if str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) == str(
                #datetime.datetime(config_ini['DEFAULT']['year'], config_ini['DEFAULT']['month'], config_ini['DEFAULT']['day'], 23, 59, 58).strftime("%Y-%m-%d %H:%M:%S")):
            #print("ewqdr")

        while True:
            print('\n')
            config_ini = configparser.ConfigParser()
            config_ini.read('config.ini')
            #print(config_ini['DEFAULT']['program_mode'])
            if int(config_ini['DEFAULT']['program_mode']) == 1:

                #df = pandas.read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
                #df = read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
                print("trying read file with input data")
                it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
                for x in range(6):
                    time.sleep(.3)  # выполнение функции
                    print(next(it), end='', flush=True)

                #df = read_excel(config['path_to_read_file'], index = ['ip', 'port', 'login', 'password','name'])
                df = read_excel(config_ini['DEFAULT']['read_file'], index = ['ip', 'port', 'login', 'password','name'],
                                encoding='sys.getfilesystemencoding()')
                print('Reading to file was successful.')
                #print(df)
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

                #st = "{}.csv".format(datetime.datetime.now())
                save_path = config_ini['DEFAULT']['path_to_save_file']
                #dtime = datetime.datetime.strptime("{}", "%y-%m-%d-H-%M")
                if datetime.datetime.now().month<10:
                    month = "0"+str(datetime.datetime.now().month)
                else:
                    month = str(datetime.datetime.now().month)


                if int(datetime.datetime.now().day)<10:
                    day = "0"+str(datetime.datetime.now().day)
                else:
                    day = str(datetime.datetime.now().day)

                if int(datetime.datetime.now().hour) < 10:
                    hour = "0" + str(datetime.datetime.now().hour)
                else:
                    hour = str(datetime.datetime.now().hour)


                if int(datetime.datetime.now().hour) < 10:
                    hour = "0" + str(datetime.datetime.now().hour)
                else:
                    hour = str(datetime.datetime.now().hour)

                if int(datetime.datetime.now().minute) < 10:
                    minute = "0" + str(datetime.datetime.now().minute)
                else:
                    minute = str(datetime.datetime.now().minute)
                #print(datetime.datetime.now().day)
                if int(datetime.datetime.now().second) < 10:
                    second = "0" + str(datetime.datetime.now().second)
                else:
                    second = str(datetime.datetime.now().second)
                #print(datetime.datetime.now().day)

                stri = "{}-{}-{}-{}-{}-{}.csv".format(datetime.datetime.now().year,month,
                                               day,hour,minute,second)


                completeName = os.path.join(save_path, stri)
                result = open(completeName, "w", encoding='utf8')
                #date_format = '%Y-%m-%d %H:%M:%S'
                date_format = '%Y-%m-%d'
                today = datetime.datetime.now()
                yesterday = today + timedelta(days=-1)
                yesterday = yesterday.strftime(date_format)
                #result.write("{}-{}-{} \n".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
                result.write(str(yesterday)+"\t\t\t\t00:00-01:00\t01:00-02:00\t02:00-03:00\t03:00-04:00\t04:00-05:00\t05:00-06:00\t"
                             "06:00-07:00\t07:00-08:00\t08:00-09:00\t09:00-10:00\t10:00-11:00\t"
                             "11:00-12:00\t12:00-13:00\t13:00-14:00\t14:00-15:00\t15:00-16:00\t16:00-17:00\t17:00-18:00\t"
                             "18:00-19:00\t19:00-20:00\t20:00-21:00\t21:00-22:00\t22:00-23:00\t23:00-24:00\n")
                #result.write(str(datetime.datetime.now())+"\n")
                result.write("""IP\tName\tDirections\tStatus\n""")
                print(len(camerasArray))
                i = 1
                for camer in camerasArray:
                    print("start work with camera, ip : {}".format(camer.ip))
                    it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
                    for x in range(6):
                        time.sleep(.3)  # выполнение функции
                        print(next(it), end='', flush=True)

                    #print("Staring work with {} camera".format(i))
                    #result = open(st, "a")

                    #result.write("ip : {}\tname shop : {}\n".format(camer.ip,camer.desc))

                    #enter, exit = getStartPeopleValue(camer.ip, camer.port, camer.login, camer.password)
                    '''
                    result.write("Time perion\t00:00-01:00\t01:00-02:00\t02:00-03:00\t03:00-04:00\t04:00-05:00\t05:00-06:00\t"
                                 "06:00-07:00\t07:00-08:00\t08:00-09:00\t09:00-10:00\t10:00-11:00\t"
                                 "11:00-12:00\t12:00-13:00\t13:00-14:00\t14:00-15:00\t15:00-16:00\t16:00-17:00\t17:00-18:00\t"
                                 "18:00-19:00\t19:00-20:00\t20:00-21:00\t21:00-22:00\t22:00-23:00\t23:00-24:00\n")
                    result.write("{}-{}-{} \n".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
                    result.write("ip\tname shop\n")
                    '''
                    string = 'daily'
                    # enter, exit = getStartPeopleValue()
                    enter, exit, status = getStartPeopleValue(camer.ip, camer.port, camer.login, camer.password, string)

                    #print(enter)
                    #print(exit)
                    #print(status)
                    #print(camer.desc)
                    #print(type(camer.desc))    #= camer.desc.replace("'", "''")
                    #camer.desc = camer.desc.replace('"', '""')
                    #result.write(u"{}\t{}\t\t{}\n".format(camer.ip,camer.desc,status))
                    result.write(u"{}\t{}\t\t{}\n".format(camer.ip,camer.desc,status))

                    result.write('\t\tEnter')
                    result.write("\t\t")
                    for i in range(len(enter)):
                        '''
                        result.write("ip:\n00:00-01:00\n01:00-02:00\n02:00-03:00\n03:00-04:00\n04:00-05:00\n05:00-06:00\n"
                                     "06:00-07:00\n07:00-08:00\n08:00-09:00\n09:00-10:00\n10:00-11:00\n"
                                     "11:00-12:00\n12:00-13:00\n13:00-14:00\n14:00-15:00\n15:00-16:00\n16:00-17:00\n17:00-18:00\n"
                                     "18:00-19:00\n19:00-20:00\n20:00-21:00\n21:00-22:00\n22:00-23:00\n23:00-24:00\n")
                        '''

                        result.write(enter[i] + "\t")
                    result.write('\n')
                    result.write('\t\tExit')
                    result.write("\t\t")
                    for i in range(len(enter)):
                        '''
                        result.write("ip:\n00:00-01:00\n01:00-02:00\n02:00-03:00\n03:00-04:00\n04:00-05:00\n05:00-06:00\n"
                                     "06:00-07:00\n07:00-08:00\n08:00-09:00\n09:00-10:00\n10:00-11:00\n"
                                     "11:00-12:00\n12:00-13:00\n13:00-14:00\n14:00-15:00\n15:00-16:00\n16:00-17:00\n17:00-18:00\n"
                                     "18:00-19:00\n19:00-20:00\n20:00-21:00\n21:00-22:00\n22:00-23:00\n23:00-24:00\n")
                        '''
                        result.write(exit[i] + "\t")
                    result.write('\n')


                        #printRes(st,enter, exit)

                    print('finish work with this camera.')
                #print(end_date)
                #print("Next report will be create in : " + end_date)

                result.close()
                print("Today report : " +str(datetime.datetime.now()))


                done = False


                # here is the animation
                def animate():
                    for c in itertools.cycle(['|', '/', '-', '\\']):
                        if done:
                            break
                        sys.stdout.write('\rwaiting ' + c + c + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    sys.stdout.write('\n')



                t = threading.Thread(target=animate)
                t.start()

                # long process here
                #time.sleep(config['time_sleep'])
                time.sleep(int(config_ini['DEFAULT']['time_sleep']))
                #time.sleep(10)
                done = True

        '''
        if config_ini['DEFAULT']['program_mode'] == 2:
            # df = pandas.read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
            # df = read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
            df = read_excel(config['path_to_read_file'], index=['ip', 'port', 'login', 'password', 'name'])

            camerasArray = []
            for index in range(len(df)):
                camerasArray.append(Camera(ip=df.iloc[index][0], port=df.iloc[index][1],
                                           login=df.iloc[index][2], password=df.iloc[index][3],
            
                                           desc=df.iloc[index][4]))
            

            st = "{}-{}-{}.csv".format(datetime.datetime.now().year, datetime.datetime.now().month,
                                       datetime.datetime.now().day)
            result = open(st, "w")
            # result.write("{}-{}-{} \n".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
            result.write("\t\t\t\tПонедельник\tВторник\tСреда\tЧетверг\tПятница\tСуббота\t"
                         "Воскресенье\n")
            result.write("IP\tName\tDirections\tStatus\n")

            print(len(camerasArray))
            for camer in camerasArray:
                string = 'weekly'
                # enter, exit = getStartPeopleValue()
                enter, exit, status = getStartPeopleValue(camer.ip, camer.port, camer.login, camer.password,string)

                # print(enter)
                # print(exit)
                # print(status)

                result.write("{}\t{}\t\t{}\n".format(camer.ip, camer.desc, status))
                result.write('\t\tEnter')
                result.write("\t\t")
                for i in range(len(enter)):


                    result.write(enter[i] + "\t")
                result.write('\n')
                result.write('\t\tExit')
                result.write("\t\t")
                for i in range(len(enter)):

                    result.write(exit[i] + "\t")
                result.write('\n')
                # printRes(st,enter, exit)

            time.sleep(10)

        '''
