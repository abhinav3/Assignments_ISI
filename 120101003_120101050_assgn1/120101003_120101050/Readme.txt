Corpora source: nltk_data/abc/rural.txt (Web source)-> Not included in assignment submitted(due to large size).Hence you have to download it from "http://www.nltk.org/nltk_data/".

Unzip 120101003_120101050.tar.gz.

It contains 3 things:

1.Rpt_120101003_120101050.pdf is the assignment report.

2.readme.txt and

3.Supplementary folder:

	3.1. Tool_ApacheOpennlp folder:
		3.1.1. Lemmatization: Eclipse Source code for lemmatization using stanford NLP lemmatizer.

		3.1.2. Part1 folder: Eclipse Source code for Sentence segementor and tokenizor using Apache Opennlp tool.

		3.1.3. Lemmatized_results folder: It contains unigrams, bigrams and trigrams frequencies for lemmatized corpus present in file "lemmatized_CORPUS.txt".

		3.1.4. Unlemmatized_Results folder: It contains unigrams, bigrams and trigrams frequencies for Unlemmatized corpus "rural.txt".It also contains "percent_compute.py" script to count top 90% of corpus etc.
		3.1.4. Unlemmatized_Results folder: It contains unigrams, bigrams and trigrams frequencies for Unlemmatized corpus "rural.txt".It also contains "percent_compute.py" script to count top 90% of corpus etc.

	3.2. Tool2_NLTK folder:
		3.2.1. Lemmatized_Results folder: It contains unigrams, bigrams and trigrams frequencies for lemmatized corpus present in file "lemmatized_CORPUS.txt".It also contains the source codes required for generating these results as python scripts.

		3.2.2. unlemmatized_Results folder: It contains unigrams, bigrams and trigrams frequencies for unlemmatized corpus present in file "rural.txt".It also contains the source codes required for generating these results as python scripts.
		It contains "sentencesegmenter.py" script and segemented sentences are present in "segmentedsentence.txt".

	3.3. Part3 folder:

		3.3.1.Chi_square folder: It contains python scripts to implement chi_square method in "chisquare_implementation.py" and using library in "chisquare_lib.py". Resulting all contiguous and discontiguous collocations along with the chi_square scores are present in "collocations.txt".

		3.3.1.Chi_square folder: It contains python scripts to implement chi_square method in "chisquare_implementation.py" and using library in "chisquare_lib.py". Resulting all contiguous and discontiguous collocations along with the chi_square scores are present in "collocations.txt".

		3.3.2. Heuristic folder: It contains heuristic python script to segement the sentences and tokenize the words in "heuristic.py" file ."percent_counter.py" is used to count the top 90% ,80% and 70% ngrams etc.
		Resulting uni,bi and trigrams are present in "uni.txt","bi.txt" and "tri.txt".
	3.4 Dictionary folder: It contains dictionary in "dictionary.txt" and lemmatized dictionary in "dictionary_lemmatized.txt".

	3.5.Bonus Problem folder: Word frequency distribution is present in "uni.csv" and "bi.csv" contains all contiguous collocations.
