

def process_user_query(query_string):


    import math


    #query_string = ('18 85 m 18 10')
    value = query_string.split(' ')
    info = [ ]
    for i in query_string.split():
        info.append(i)


    #INFO
    age = int(info[0])
    W = int(info[1])
    rhr =  ( 6 * int(info[3]) )
    mhr = ( 208 - (0.7*age))
    TotalCalsToLose = int(info[4]) * 7716
    VO2max = mhr/rhr * 15.3


    #Formula
    LeastTimeMale = ((( -95.7735 + (0.634 * 165) + (0.404 * VO2max) + (0.394 * W) + (0.271 * age )) / 4.184) * 20)**1.13621
    #print(LeastTimeMale)
    MostTimeMale = ((( -95.7735 + (0.634 * 120) + (0.404 * VO2max) + (0.394 * W) + (0.271 * age )) / 4.184) * 50)**1.019
    #print(MostTimeMale)
    LeastTimeFemale = ((( -59.3954 + (0.45 * 165) + (0.380 * VO2max) + (0.103 * W) + (0.274 * age )) / 4.184) * 20)**1.12521
    MostTimeFemale = ((( -59.3954 + (0.45 * 120) + (0.380 * VO2max) + (0.103 * W) + (0.274 * age )) / 4.184) * 50)**1.016


    #Male
    MostMaleTotalDays = math.ceil(TotalCalsToLose / MostTimeMale)
    #print(MostMaleTotalDays)
    LeastMaleTotalDays = math.ceil( (TotalCalsToLose / LeastTimeMale) *.654 )
    #print(LeastMaleTotalDays)


    #Female
    MostFemaleTotalDays = math.ceil(TotalCalsToLose / MostTimeFemale)
    LeastFemaleTotalDays = math.ceil((TotalCalsToLose / LeastTimeFemale) *.654 )


    if str(info[2]) == 'M' or 'm':
    #    print(f'M - With 45 minute workout/day: You must exercise {MostMaleTotalDays} days with a heart rate of at least 120 to reach your goal.\n With 15 minute workout/day: You must exercise {LeastMaleTotalDays} days with a heart rate of at least 165 to reach your goal')
        a = f'With 45 minute workout/day: You must exercise {MostMaleTotalDays} days with a heart rate of at least 120 to reach your goal.\n With 15 minute workout/day: You must exercise {LeastMaleTotalDays} days with a heart rate of at least 165 to reach your goal'
    else:
    #    print(f'F - With 45 minute workout/day: You must exercise {LeastFemaleTotalDays} days with a heart rate of at least 120 to reach your goal.\n With 15 minute workout/day: You must exercise {LeastFemaleTotalDays} days with a heart rate of at least 165 to reach your goal')
        a = f'With 45 minute workout/day: You must exercise {LeastFemaleTotalDays} days with a heart rate of at least 120 to reach your goal.\n With 15 minute workout/day: You must exercise {LeastFemaleTotalDays} days with a heart rate of at least 165 to reach your goal'

    return a
