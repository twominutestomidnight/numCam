import datetime
from getCamNum import getStartPeopleValue



def printRes(st,enter, exit):
    result = open(st, "a")
    '''
    result.write("Time perion\t00:00-01:00\t01:00-02:00\t02:00-03:00\t03:00-04:00\t04:00-05:00\t05:00-06:00\t"
                 "06:00-07:00\t07:00-08:00\t08:00-09:00\t09:00-10:00\t10:00-11:00\t"
                 "11:00-12:00\t12:00-13:00\t13:00-14:00\t14:00-15:00\t15:00-16:00\t16:00-17:00\t17:00-18:00\t"
                 "18:00-19:00\t19:00-20:00\t20:00-21:00\t21:00-22:00\t22:00-23:00\t23:00-24:00\n")
    result.write("{}-{}-{} \n".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
    result.write("ip\tname shop\n")
    '''
    #enter, exit = getStartPeopleValue()
    result.write('Enter\t')
    for i in range(len(enter)):
        '''
        result.write("ip:\n00:00-01:00\n01:00-02:00\n02:00-03:00\n03:00-04:00\n04:00-05:00\n05:00-06:00\n"
                     "06:00-07:00\n07:00-08:00\n08:00-09:00\n09:00-10:00\n10:00-11:00\n"
                     "11:00-12:00\n12:00-13:00\n13:00-14:00\n14:00-15:00\n15:00-16:00\n16:00-17:00\n17:00-18:00\n"
                     "18:00-19:00\n19:00-20:00\n20:00-21:00\n21:00-22:00\n22:00-23:00\n23:00-24:00\n")
        '''

        result.write(enter[i] + "\t")
    result.write('\n')
    result.write('Exit\t')
    for i in range(len(enter)):
        '''
        result.write("ip:\n00:00-01:00\n01:00-02:00\n02:00-03:00\n03:00-04:00\n04:00-05:00\n05:00-06:00\n"
                     "06:00-07:00\n07:00-08:00\n08:00-09:00\n09:00-10:00\n10:00-11:00\n"
                     "11:00-12:00\n12:00-13:00\n13:00-14:00\n14:00-15:00\n15:00-16:00\n16:00-17:00\n17:00-18:00\n"
                     "18:00-19:00\n19:00-20:00\n20:00-21:00\n21:00-22:00\n22:00-23:00\n23:00-24:00\n")
        '''

        result.write(exit[i] + "\t")
    result.write('\n')
