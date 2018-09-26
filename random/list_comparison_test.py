import random
import time

print("========start=========")

run_time = time.time()

n = 50000000
print("running with n = ",n)

def make_list(n):
    result = random.sample(range(10*n), n)
    # result = []
    # for _ in range(n):
    #     number = random.randint(0, 10*n)
    #     if number not in result:
    #         result.append(number)
    return(result)

start = time.time()
list_1 = make_list(n)
list_2 = make_list(n)
print("Building the lists took {}".format(time.time()-start))

def if_in(list_1, list_2):
    dupe_list = []
    for i in list_1:
        if i in list_2:
            dupe_list.append(i)
    return(dupe_list)

def my_way(list_1, list_2):
    list_1.sort()
    list_2.sort()
    dupe_list = []
    index_1 = 0
    index_2 = 0
    while(index_1<len(list_1) and index_2<len(list_2)):
        if list_1[index_1] == list_2[index_2]:
            dupe_list.append(list_1[index_1])
            index_1 += 1
            index_2 += 1
        elif list_1[index_1] > list_2[index_2]:
            index_2 += 1
        else:
            index_1 += 1
    return(dupe_list)

def union(list_1, list_2):
    list_1 = set(list_1)
    list_2 = set(list_2)
    dupe_list = list_1.union(list_2)
    return(dupe_list)

# start_time = time.time()
# dupe_list = if_in(list_1, list_2)
# #print(dupe_list)
# print("if in took {} seconds".format(time.time()-start_time))

start_time = time.time()
dupe_list = my_way(list_1, list_2)
time_2 = time.time()-start_time
#print(dupe_list)
print("my way took {} seconds".format(time_2))

start_time = time.time()
dupe_list = union(list_1, list_2)
time_3 = time.time()-start_time
#print(dupe_list)
print("union took {} seconds".format(time_3))

print("whole thing took {} seconds".format(time.time()-run_time))
print("ratio of my time/union is {}".format(time_2/time_3))

print("========end=========")
