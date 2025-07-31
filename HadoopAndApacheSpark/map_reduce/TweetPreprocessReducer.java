import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Reducer;

public class TweetPreprocessReducer extends Reducer<LongWritable, Text, NullWritable, Text> {
    public void reduce(LongWritable key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        for (Text val : values) {
            context.write(NullWritable.get(), val);
        }
    }
}
