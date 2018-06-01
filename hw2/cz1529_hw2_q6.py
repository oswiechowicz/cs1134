def two_sum(srt_lst,target):
    dic={} #store the compliments
    for i in range(len(srt_lst)):
        compliment=target-srt_lst[i] #for lst[i]=target, then compliment=target-lst[i]
        if compliment in dic: #store position and compliment into dic if not already in
            return tuple([dic[compliment],i]) #returns answer :))
        else:
            dic[srt_lst[i]]=i #add to dic
    return None #if nothing

def main():
    lst=[-2,7,11,15,20,21]
    print(two_sum(lst,22))

