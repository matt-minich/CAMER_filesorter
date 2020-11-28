import pandas as pd
import glob
import bisect
input = [30000,60000,90000,120000,150000,180000,210000,240000]
files = ['Resampled', 'Original']
for file in files:
    path = r'D:\CAMER\COVID\Twitter Data\%s' %file
    tweets = glob.iglob(path + "/*.csv")
    for t in tweets:
        df = pd.read_csv(t)
        for i in range(100):
            d = df.at[i,'Date'].__contains__('Delet')
            if d == False:
                date = df.at[i, 'Date']
                time = (bisect.bisect(input, (int(df.at[i, 'Time'][:-10].replace(':',''))))+1)
        df.to_csv("../Twitter Data/Output/{0} Hour {1} {2}.csv".format(date, time,file))