import matplotlib.pyplot as plt
import pandas as pd


def sentiment_pie(df):
    plt.pie(
        df["Sentiment"].value_counts(),
        shadow=True,
        explode=(0.05, 0.06, 0.05),
        labels=df["Sentiment"].value_counts().index,
        autopct='%1.2f%%'
    );
    plt.title("Sentiment Percentage");
