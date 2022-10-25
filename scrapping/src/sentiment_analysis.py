import pandas as pd
from transformers import pipeline

labels = {
    'LABEL_0': 'Negative',
    'LABEL_1': 'Neutral',
    'LABEL_2': 'Positive',
}


def sentiment_analysis(df, column_name):
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="Seethal/sentiment_analysis_generic_dataset"
    )
    sentiment_results = sentiment_pipeline(df[column_name].tolist())
    sentiment_results = pd.DataFrame(sentiment_results)
    # df['scores'] = sentiment_results.score
    df["Sentiment"] = sentiment_results.label.map(labels)
    return df
