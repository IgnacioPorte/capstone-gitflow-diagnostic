import json
# Los top 10 tweets más retweeted.
# Los top 10 usuarios en función de la cantidad de tweets que emitieron.
# Los top 10 días donde hay más tweets.
# Los top 10 hashtags más usados.

def top_10_retweeted(data):
    """
    Los top 10 tweets más retweeted.
    """
    top_retweeted = []
    for one_json in data:
        top_retweeted.append((one_json['retweetCount'], one_json['content']))
    # sort by retweet count
    top_retweeted.sort(key=lambda x: x[0], reverse=True)
    return top_retweeted[:10].map(lambda x: x[1])


def top_10_users():
    """
    Los top 10 usuarios en función de la cantidad de tweets que emitieron.
    """
    pass


def top_10_days():
    """
    Los top 10 días donde hay más tweets.
    """
    pass


def top_10_hashtags():
    """
    Los top 10 hashtags más usados.
    """
    pass


def main():
    top_10_retweeted()
    top_10_users()
    top_10_days()
    top_10_hashtags()


if __name__ == "__main__":
    main()
