													CS 565: Assignment-2
									Hidden Markov Models (HMMs), Part-of-Speech (PoS) Tagging

									By: 1. Abhinav Ravi(120101003)(r.abhinav@iitg.ernet.in)
										2. Pintu Kumar(120101050)(pintu.kumar@iitg.ernet.in)


A).Important Notes:
-------------------------------------------------------------------------------------------------------------------------------	
	Note 0. If found any dificulty running the codes(errors), please mail us. It might be because of python version problems or file path problems.

	Note 1. 
			a)Brown_train.txt is given untagged file and is used for testing after tagging(actual tags).
			Brown_tagged_train.txt is given tagged file and is used for training and finally used for comparison(as desired tags). 

			b)Brown_train.txt had more number of lines than Brown_tagged_train.txt. So enen after doing the tagging for those extra lines, it was impossible to compare them for correct tags as those lines(with tags) were not present in Brown_tagged_train.txt.

			c)Hence Extra lines from Brown_train.txt(test file/Untagged file) has been removed as they cann't be tested for evaluation.

	Note 2. 
			a)We have preprocessed the Brown_tagged_train.txt and Brown_train.txt to obtain the train_data.txt and test_data.txt respectively.

			b)train_data.txt contains the "word/tag" in the required fromat for our algorithm to read and being trained.
			test_data.txt contains the "word" in the required fromat for our algorithm to read and being tagged for evaluation.

			c)In preprocessing step begining of each sentence is appended with "*/*" and "*/*" while end of each sentence is appended with "$/$" in train_data.txt.

			Similarly, begining of each sentence is appended with "*" and "*" while end of each sentence is appended with "$" in train_data.txt.

			d)Hence format of each sentence(containing word1 to word i) in train_data.txt is as below:

			*/*
			*/*
			word1/tag1
			word2/tag2
			.
			.
			.
			wordi/tagi
			$/$
			....................

			While, format of each sentence (containing word1 to word i) in test_data.txt is as below:

			*
			*
			word1
			word2
			.
			.
			.
			wordi
			$
			....................

	Note 3.
		a)In deliverable1 we have implemented Laplace Smoothing.
		 While in deliverable2 we have implemented "Linear Interpolation Method". 

		Better grouping of words (as discussed in the class) has been implemented for both deliverable1() and deliverable2(Linear Interpolation based method).

		We have defined following extra class lables for RARE occuring words(words with count < 6):

			1. ALLCAPS : eg: 'ABC', 'HELLO'
			2. NUM     : eg: '1234'
			3. FLOAT   : eg: '0.356'
			4. RARE    : Rest others.


B).Folder Structure
---------------------------------------------------------------------------------------------------------------------------------
   Unzip this folder.
   Get folder named 120101003_120101050.
   It contains readme.txt, Brown_train.txt, Brown_tagged_train.txt, preprocess.py and Source_codes folder.

   preprocess.py is used to create train_data.txt and test_data.txt by reading file Brown_tagged_train.txt.

   Within Source_codes you will find two folders named Vanilla_HMM_Tagger and Linear_Inter_HMM_Tagger.


   Deliverable1
   **************************************************************************************
   Vanilla_HMM_Tagger folder has following files:

   1. train_data.txt for training.
   2. test_data.txt for being tagged and tested.
   3. res.txt contains result obtained after tagging words from test_data.txt.
   4. HMM.py
   5. Sentence.py
   6. evaluate.py
   7. stat.txt contains evaluation scores using Laplacian snoothing method.

   Sentence.py defines Sentence class and implements Viterbi algorithm for faster compution of pi(k,u,v) using dynamic programming algorithm.

   HMM.py defines Class HMM which reads train_data.txt for training and reads test_data.txt.
   It evaluates tag_trigram_probability based on Laplacian smoothing technique.
   It then writes tagged words into res.txt.

   For running it:
   python HMM.py --f1 train_data.txt --f2 test_data.txt  

   evaluate.py compatres the result of actual word/tags(train_data.txt) and obtained word/tags(res.txt).
   It also calculates the precision, recall and f1-measures and write to stat.txt.

   For running it:
   python evaluate.py --f1 train_data.txt --f2 res.txt

   It writes results into stat.txt as:

    PRE_micro= 0.966361477058
	PRE_macro= 0.905838500756
	REC_micro= 0.966361477058
	REC_macro= 0.964784527667
	F1_micro= 0.966361477058
	F1_macro= 0.934382777091


   Deliverable2
   **************************************************************************************
   Linear_Inter_HMM_Tagger folder has following files:

   1. train_data.txt for training.
   2. test_data.txt for being tagged and tested.
   3. res.txt contains result obtained after tagging words from test_data.txt.
   4. HMM.py
   5. Sentence.py
   6. evaluate.py
   7. stat.txt contains evaluation scores using Linear_interpolation method.
	
   Sentence.py defines Sentence class and implements Viterbi algorithm for faster compution of pi(k,u,v) using dynamic programming algorithm.

   HMM.py defines Class HMM which reads train_data.txt for training and reads test_data.txt.
   It evaluates tag_trigram_probability based on Linear Interpolation technique as discussed in class.
   It then writes tagged words into res.txt.

   For running it:
   python HMM.py --f1 train_data.txt --f2 test_data.txt --l1 0.30 --l2 0.30

   l1 and l2 are lambda1 and lambda2 values needed to be provided to compute Linear_interpolation measures.
   lambda3 is calculated as : 
   l3=(1-l1-l2)


   evaluate.py compatres the result of actual word/tags(train_data.txt) and obtained word/tags(res.txt).
   It also calculates the precision, recall and f1-measures and write to stat.txt.

   For running it:
   python evaluate.py --f1 train_data.txt --f2 res.txt

   It writes results into stat.txt as:

    PRE_micro= 0.939508008056
	PRE_macro= 0.915691130784
	REC_micro= 0.939508008056
	REC_macro= 0.848698491794
	F1_micro= 0.939508008056
	F1_macro= 0.880922979484

	These evaluation scores using obtained using Linear_Interpolation method can be improved using different values of lambda1, lambda2 and lambda3.

	 Deliverable3
   **************************************************************************************
   evaluate.py compatres the result of actual word/tags(train_data.txt) and obtained word/tags(res.txt).
   It also calculates the precision, recall and f1-measures and write to stat.txt.

   It is present in both of above mentioned folders respectively.
   Method is run it is also mentiones as above.