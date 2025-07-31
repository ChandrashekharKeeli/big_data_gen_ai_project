from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from transformers import pipeline

# Initialize Spark session
spark = SparkSession.builder \
    .appName("TweetSentimentAnalysis") \
    .getOrCreate()

# Load CSV file from HDFS
# Replace this path with your correct HDFS path
df = spark.read.option("header", "true").csv("hdfs://localhost:9000/user/chandrashekhar/tweets15000/tweets_15000_clean.csv")

# Show schema for debugging
df.printSchema()

# Check sample records (optional)
df.show(5)

# Load Hugging Face sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Define a function for sentiment prediction
def analyze_sentiment(text):
    if text:
        result = sentiment_pipeline(text[:512])[0]  # Limit input to 512 tokens
        return result['label']
    return "NEUTRAL"

# Register UDF
sentiment_udf = udf(analyze_sentiment, StringType())

# Apply sentiment analysis
df_with_sentiment = df.withColumn("sentiment", sentiment_udf(df["tweet"]))

# Save result to HDFS
df_with_sentiment.write.mode("overwrite").option("header", "true").csv("hdfs://localhost:9000/user/chandrashekhar/tweets15000/sentiment_final_output")

# Optional: Show sample output
df_with_sentiment.show(10)

# Stop Spark session
spark.stop()
