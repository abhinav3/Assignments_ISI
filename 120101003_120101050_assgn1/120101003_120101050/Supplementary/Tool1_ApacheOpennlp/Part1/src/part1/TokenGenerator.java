package part1;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import opennlp.tools.tokenize.Tokenizer;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;

/**
 *
 * @author kislay.verma
 */
public class TokenGenerator {

    private static Tokenizer _TOKENIZER;
    private static boolean INITIALIZED = false;
    //private static final String modelFile = "/Users/mi0059/Documents/classifier/tokenModel";

    public static void main(String[] args) throws IOException {
        /*System.out.println(TokenGenerator.tokenize(
            "Russell Ira Crowe (born 7 April 1964) is a New Zealand-born, "
            + "Australian-raised actor, film producer and musician. "
            + "He came to international attention for his role as "
            + "the Roman General Maximus Decimus Meridius in the "
            + "2000 historical epic film Gladiator").length);*/
    }

    public static String[] tokenize(String input) throws IOException {
        if (!INITIALIZED) {
            init();
        }
       /* for(String res:_TOKENIZER.tokenize(input)){
        	System.out.println(res);
        }*/
        return _TOKENIZER.tokenize(input);
    }

    public static void init() throws IOException {
        InputStream modelIn = null;
        try {
            // Loading tokenizer model
            modelIn = new FileInputStream("J:/Assignment1_ISI/Part1/binaries/en-token.bin");
            final TokenizerModel tokenModel = new TokenizerModel(modelIn);
            modelIn.close();

            _TOKENIZER = new TokenizerME(tokenModel);
            INITIALIZED = true;
        } catch (final IOException ioe) {
            ioe.printStackTrace();
        } finally {
            if (modelIn != null) {
                try {
                    modelIn.close();
                } catch (final IOException e) {
                } // oh well!
            }
        }
    }
}