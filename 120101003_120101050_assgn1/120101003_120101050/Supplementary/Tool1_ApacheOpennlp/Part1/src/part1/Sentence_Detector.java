package part1;



import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import opennlp.tools.sentdetect.SentenceDetector;
import opennlp.tools.sentdetect.SentenceDetectorME;
import opennlp.tools.sentdetect.SentenceModel;

	/**
 *
 * @author kislay.verma
 */
public class Sentence_Detector {

    private static SentenceDetector SENTENCE_DETECTOR;
    private static boolean INITIALIZED = false;

    public static void main(String[] args) {
        /*System.out.println(Sentence_Detector.detect("Russell Ira Crowe (born 7 April 1964) is a New Zealand-born, "
            + "Australian-raised actor, film producer and musician. "
            + "He came to international attention for his role as "
            + "the Roman General Maximus Decimus Meridius in the "
            + "2000 historical epic film Gladiator").length);*/
    }

    public static String[] detect(String input) {
        if (!INITIALIZED) {
            init();
        }
        /*for(String res:SENTENCE_DETECTOR.sentDetect(input)){
        	System.out.println(res);
        }*/
        return SENTENCE_DETECTOR.sentDetect(input);
    }

    public static void init() {
        InputStream modelIn = null;
        try {
            // Loading sentence detection model
            modelIn = new FileInputStream("J:/Assignment1_ISI/Part1/binaries/en-sent.bin");
            final SentenceModel sentenceModel = new SentenceModel(modelIn);
            modelIn.close();

            SENTENCE_DETECTOR = new SentenceDetectorME(sentenceModel);
            INITIALIZED = true;
        } catch (final IOException ioe) {
            ioe.printStackTrace();
        } finally {
            if (modelIn != null) {
                try {
                    modelIn.close();
                } catch (final IOException e) {
                }
            }
        }
    }
}




