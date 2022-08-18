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


def top_10_users(data):
    """
    Los top 10 usuarios en función de la cantidad de tweets que emitieron.
    """
    top_users = {}
    for one_json in data:
        if one_json['user']['username'] in top_users:
            top_users[one_json['user']['username']] += 1
        else:
            top_users[one_json['user']['username']] = 1
    pass
    # sort by value
    top_users = sorted(top_users.items(), key=lambda x: x[1], reverse=True)
    return top_users[:10].map(lambda x: x[0])


def top_10_days(data):
    """
    Los top 10 días donde hay más tweets.
    """
    top_days = {}

    for one_json in data:
        date = one_json['date'].split('T')[0]
        if date in top_days:
            top_days[date] += 1
        else:
            top_days[date] = 1
    # sort by value
    top_days = sorted(top_days.items(), key=lambda x: x[1], reverse=True)
    return top_days[:10].map(lambda x: x[0])

def top_10_hashtags(data):
    """
    Los top 10 hashtags más usados.
    """
    top_hashtags = {}
    for one_json in data:
        for hashtag in one_json['content'].split(' '):
            if hashtag.startswith('#'):
                if hashtag in top_hashtags:
                    top_hashtags[hashtag] += 1
                else:
                    top_hashtags[hashtag] = 1
    # sort by value
    top_hashtags = sorted(top_hashtags.items(), key=lambda x: x[1], reverse=True)
    return top_hashtags[:10].map(lambda x: x[0])


def main():
    top_10_retweeted()
    top_10_users()
    top_10_days()
    top_10_hashtags()


if __name__ == "__main__":
    main()
