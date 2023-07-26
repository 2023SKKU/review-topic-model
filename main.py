from feature_extraction import FeatureExtraction

def main():
    # Example
    fe = FeatureExtraction('./닭가슴살1.csv')
    # training topic model
    fe.train_topic_model_with_bertopic('닭가슴살')
    # extract topic and keyword
    topics = fe.get_topics_with_keyword(top_n_word=10)
    # dynamic topic model (per month)
    dtm = fe.get_topics_per_month()
    print(dtm)
    # extract keyword based on dtm
    print(fe.get_keywords_with_time_series(dtm, 0))


if __name__ == '__main__':
    main()
