from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler


def predict_cancellations(user_interaction_df):
    assembler = VectorAssembler(
        inputCols=["month_interaction_count", "week_interaction_count", "day_interaction_count"],
        outputCol="features"
    )
    features_df = assembler.transform(user_interaction_df)
    features_df = features_df.withColumn("label", features_df["cancelled_within_week"])

    model = LogisticRegression(maxIter=10, threshold=0.6, elasticNetParam=1, regParam=0.1)
    trained_model = model.fit(features_df)

    return trained_model.transform(features_df).select(["user_id", "rawPrediction", "probability", "prediction"])
    
    
