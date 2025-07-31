import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Mapper;

public class TweetPreprocessMapper extends Mapper<LongWritable, Text, LongWritable, Text> {
    
    private static final Pattern URL_PATTERN = Pattern.compile("https?://\\S+");

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String tweet = value.toString().trim();

        // Remove URLs
        Matcher matcher = URL_PATTERN.matcher(tweet);
        String cleaned = matcher.replaceAll("");

        // Normalize whitespace
        cleaned = cleaned.replaceAll("\\s+", " ").trim();

        if (!cleaned.isEmpty()) {
            context.write(key, new Text(cleaned));
        }
    }
}
