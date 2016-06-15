package lemmatizer;


	import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.Matcher;
	import java.util.regex.Pattern;
	 
	public class PostProcessor {
	 
	    public String replaceWithPattern(String str,String replace){
	         
	        Pattern ptn = Pattern.compile("``\\s");
	        Matcher mtch = ptn.matcher(str);
	        return mtch.replaceAll(replace);
	    }
	     
	    public static void main(String [] args) throws IOException{
	    	String filePath = "J:/Assignment1_ISI/lemmatizedrural2.txt";
	    	String outfilePath = "J:/Assignment1_ISI/lemmatizedrural3.txt";
	        String content=new String(Files.readAllBytes(Paths.get(filePath)));
	        PostProcessor mpr = new PostProcessor();
	        FileWriter writer =new FileWriter(outfilePath) ;
	        writer.write(mpr.replaceWithPattern(content, ""));
	        writer.close();
	       // System.out.println(mpr.replaceWithPattern(content, " "));
	    }
	}

