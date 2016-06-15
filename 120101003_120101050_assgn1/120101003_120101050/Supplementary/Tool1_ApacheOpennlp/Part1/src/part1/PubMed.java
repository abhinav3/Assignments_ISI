package part1;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map.Entry;


public class PubMed {

	private static String filePath = "J:/Assignment1_ISI/PubMed/pubmed_2.txt";
	private static String unigramfilePath = "J:/Assignment1_ISI/PubMed/uni.csv";
	private static String bigramfilePath = "J:/Assignment1_ISI/PubMed/bi.csv";
	//private static String trigramfilePath = "J:/Assignment1_ISI/PubMed/tri.csv";

	public static void main(String[] args) throws IOException{
		
		
		
		 Map<String, Integer> unigram = new HashMap<String, Integer>();
		 Map<String, Integer> bigram = new HashMap<String, Integer>();
		// Map<String, Integer> trigram = new HashMap<String, Integer>();
	     
		 //String content=new String(Files.readAllBytes(Paths.get(filePath)));
		 
		 FileInputStream fstream = new FileInputStream(filePath);
		 BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

		 String strLine;

		 //Read File Line By Line
		 while ((strLine = br.readLine()) != null)  {
			       
			    	
			    	String [] sentences=Sentence_Detector.detect(strLine);
					 for(String mString:sentences){
						
				         for (String ngram : ngrams(1, mString)){
				        	 
				        	 //System.out.println(ngram);
				        	 if (unigram.containsKey(ngram)) {
				                 int cont = unigram.get(ngram);
				                 unigram.put(ngram, cont + 1);
				              } else {
				                 unigram.put(ngram, 1);
				              }
				             
				         }//System.out.println();
				         
				         for (String ngram : ngrams(2, mString)){
				        	 
				        	 //System.out.println(ngram);
				        	 if (bigram.containsKey(ngram)) {
				                 int cont = bigram.get(ngram);
				                 bigram.put(ngram, cont + 1);
				              } else {
				                 bigram.put(ngram, 1);
				              }
				             
				         }//System.out.println();
				         /*for (String ngram : ngrams(3, mString)){
				        	 
				        	 //System.out.println(ngram);
				        	 if (trigram.containsKey(ngram)) {
				                 int cont = trigram.get(ngram);
				                 trigram.put(ngram, cont + 1);
				              } else {
				                 trigram.put(ngram, 1);
				              }
				             
				         }*///System.out.println();
			           }
			    	
			    	
			    }
			
		 
		 
		 br.close();
		 
		 
	
		 //Sorting the unigrammaps 
		 FileWriter writer1 =new FileWriter(unigramfilePath) ;
		 Set<Entry<String, Integer>> set1 = unigram.entrySet();
	        List<Entry<String, Integer>> list1 = new ArrayList<Entry<String, Integer>>(set1);
	        Collections.sort( list1, new Comparator<Map.Entry<String, Integer>>()
	        {
	            public int compare( Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2 )
	            {
	                return (o2.getValue()).compareTo( o1.getValue() );
	            }
	        } );
	        for(Map.Entry<String, Integer> entry:list1){
	            //System.out.println(entry.getKey()+","+entry.getValue());
	            writer1.write(entry.getKey()+","+entry.getValue()+"\n");
	        }
		 writer1.close();
		 
		//Sorting the bigrammaps 
		 FileWriter writer2 =new FileWriter(bigramfilePath) ;
		 Set<Entry<String, Integer>> set2 = bigram.entrySet();
	        List<Entry<String, Integer>> list2 = new ArrayList<Entry<String, Integer>>(set2);
	        Collections.sort( list2, new Comparator<Map.Entry<String, Integer>>()
	        {
	            public int compare( Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2 )
	            {
	                return (o2.getValue()).compareTo( o1.getValue() );
	            }
	        } );
	        for(Map.Entry<String, Integer> entry:list2){
	            //System.out.println(entry.getKey()+","+entry.getValue());
	            writer2.write(entry.getKey()+","+entry.getValue()+"\n");
	        }
		 writer2.close();
		 
		 
		//Sorting the trigrammaps 
		 /*FileWriter writer3 =new FileWriter(trigramfilePath) ;
		 Set<Entry<String, Integer>> set3 = trigram.entrySet();
	        List<Entry<String, Integer>> list3 = new ArrayList<Entry<String, Integer>>(set3);
	        Collections.sort( list3, new Comparator<Map.Entry<String, Integer>>()
	        {
	            public int compare( Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2 )
	            {
	                return (o2.getValue()).compareTo( o1.getValue() );
	            }
	        } );
	        for(Map.Entry<String, Integer> entry:list3){
	            //System.out.println(entry.getKey()+","+entry.getValue());
	            writer3.write(entry.getKey()+","+entry.getValue()+"\n");
	        }
		 writer3.close();*/
		 
	}

	public static List<String> ngrams(int n, String str) throws IOException {
		List<String> ngrams = new ArrayList<String>();
		// String[] words = str.split(" ");
		String[] words = TokenGenerator.tokenize(str);
		for (int i = 0; i < words.length - n + 1; i++)
			ngrams.add(concat(words, i, i + n));
		return ngrams;
	}

	public static String concat(String[] words, int start, int end) {
		StringBuilder sb = new StringBuilder();
		for (int i = start; i < end; i++)
			sb.append((i > start ? " " : "") + words[i]);
		return sb.toString();
	}

}
