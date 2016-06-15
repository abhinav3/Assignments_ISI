from __future__ import division
from optparse import OptionParser
import sys

def main():
	
	parser = OptionParser()
	parser.add_option("--f1", dest = "file1", help = "tagged training file" ,default = "train_data.txt")
	parser.add_option("--f2", dest = "file2", help = "untagged test file", default = "res.txt" )
	(options, args) = parser.parse_args()
	
	TAGCOUNT = 14
	resmatrix=[[0 for j in range(TAGCOUNT)]for i in range(TAGCOUNT)]

	# TP:0 FN:1 FP:2
	resStat=[[0 for j in range(0,3) ] for i in range (TAGCOUNT)]

	#Pre Recall F1measure
	result=[[0 for j in range(0,3) ] for i in range (TAGCOUNT)]
	tag_dict = {'NUM' : 0, 'X' : 1, 'VERB' : 2, 'DET' : 3, 'NOUN':4, 'CONJ':5, 'PRT':6, 'ADP':7,'ADV':8,'PRON':9,'ADJ':10,'.':11,'$':12,'*':13}
	#trainfile = sys.argv[1]?
	trainf = open(options.file1,"r").readlines()
	resf = open(options.file2,"r").readlines()
	if(not((len(trainf)-1)  == len(resf))):
		print("Incompatible erroneous files are input")
		sys.exit()
	
	for i in range(len(trainf)-2):
		line1=trainf[i].strip('\n')
		line2=resf[i].strip('\n')
		if len(line1) > 0 and len(line2)>0:
		   wt1 = line1.split('/')
		   wt2 = line2.split('/')
		   resmatrix[tag_dict[wt1[-1]]][tag_dict[wt2[-1]]]+=1
		    	
	print(resmatrix)

	for i in range (TAGCOUNT):
		# filling TP in resStat
		resStat[i][0] = resmatrix[i][i];
		# filling FN and FP in resStat
		FNfrq=0
		FPfrq=0
		for j in range(TAGCOUNT):
			if not (j == i):
				FNfrq += resmatrix[i][j]
				FPfrq += resmatrix[j][i] 
		resStat[i][1] = FNfrq
		resStat[i][2] = FPfrq

	print("\nRESTAT")
	print(resStat)	 
	for i in range(TAGCOUNT):
	
		print(list(tag_dict.keys())[list(tag_dict.values()).index(i)]) # Prints key
		print(" \n HAS Precision: ")
		result[i][0]=(resStat[i][0])/(resStat[i][0]+resStat[i][2]+1)
		print(result[i][0])
		print(" \n HAS Recall: ")
		result[i][1]=(resStat[i][0])/(resStat[i][0]+resStat[i][1]+1)
		print(result[i][1])
		print(" \n HAS F1-measure: ")
		result[i][2]=(2*result[i][0]*result[i][1])/(result[i][0]+result[i][1]+1)
		print(result[i][2])

	f=open("stat.txt","w")
	num=0
	denumP=0
	denumR=0
	preAdd=0
	recAdd=0
	for i in range(TAGCOUNT):
		num+=  resStat[i][0]
		denumP+= resStat[i][0]+resStat[i][2]
		denumR+= resStat[i][0]+resStat[i][1]
		preAdd+= result[i][0]
		recAdd+= result[i][1]
	preMicro= num/denumP
	preMacro=preAdd/TAGCOUNT
	recMicro=num/denumR
	recMacro=recAdd/TAGCOUNT
	f1Micro=(2*preMicro*recMicro)/(preMicro+recMicro)
	f1Macro=(2*preMacro*recMacro)/(preMacro+recMacro)
	f.write("PRE_micro= ")
	f.write(str(preMicro))
	f.write("\n")
	f.write("PRE_macro= ")
	f.write(str(preMacro))
	f.write("\n")
	f.write("REC_micro= ")
	f.write( str(recMicro))
	f.write("\n")
	f.write("REC_macro= ")
	f.write(str(recMacro))
	f.write("\n")
	f.write("F1_micro= ")
	f.write(str(f1Micro))
	f.write("\n")
	f.write("F1_macro= ")
	f.write(str(f1Macro))
	f.close()


if __name__ == "__main__":
	main()
	  
