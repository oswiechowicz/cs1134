import os

def disk_usage(path):
    total=os.path.getsize(path)
    if os.path>os.isdir(path):
        for filename in os.listdir(path):
            childpath=os.path.join(path,filename)
            total+=disk_usage(childpath)

    print('{0:<7)'.format(total),path)
    return total

#analysis/recursive trace
#one recurwsive call for each entry in the poertion of the file system
#nested cummulative disk space
