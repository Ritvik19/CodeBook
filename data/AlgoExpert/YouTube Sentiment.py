def get_youtube_sentiment(video_stats_df):
    video_stats_df['sentiment'] = video_stats_df['likes'] / (video_stats_df['dislikes'] + video_stats_df['likes'])
    mean_sentiment_df = video_stats_df.groupby('category_id').mean()
    mean_sentiment_df = mean_sentiment_df.sort_values("sentiment", ascending=False)
    mean_sentiment_df["mean_sentiment"] = mean_sentiment_df["sentiment"]
    return mean_sentiment_df.filter(["mean_sentiment"])
    
    
