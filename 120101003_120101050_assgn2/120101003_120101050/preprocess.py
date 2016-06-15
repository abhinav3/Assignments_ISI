#!/usr/bin/var python3
file_path1 = "Brown_tagged_train.txt"
file_path2 = "Brown_train.txt"
outTagged = open("train_data.txt","w")
outUntagged = open("test_data.txt","w")
with open(file_path1) as f1:
    for line_terminated in f1:
        line = line_terminated.rstrip('\n\r')
        outTagged.write("*/*"+"\n"+"*/*")
        if len(line) > 0:
                wt = line.split(' ')
                for i in range(len(wt)):
                	if not (wt[i]==''):
                		wt1 = wt[i].split('/')
                		tm = wt1[:-1]
                		#print (tm)
                		st=tm[0]
                		for j in range(1,len(tm)):
                			st = st +"_"+tm[j]
                	#tm=tm.replace("-","_")
                        	outTagged.write("\n"+st+"/"+wt1[-1])
        outTagged.write("\n"+"$/$"+"\n")
#outTagged.write("$/$")
outTagged.close()

with open(file_path2) as f2:
    for line_terminated in f2:
        line = line_terminated.rstrip('\n\r')
        outUntagged.write("*"+"\n"+"*")
        if len(line) > 0:
                wt = line.split(' ')
                for i in range(len(wt)):
                	wt[i]=wt[i].replace("/","_")
                	#wt[i]=wt[i].replace("-","_")
                        outUntagged.write("\n"+wt[i])
        outUntagged.write("$"+"\n")
#outUntagged.write("$")
outUntagged.close()
