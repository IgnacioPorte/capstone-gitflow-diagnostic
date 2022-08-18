import json


def top_10_retweeted(data):
    """
    Los top 10 tweets más retweeted.
    """
    top_retweeted = []
    for one_json in data:
        top_retweeted.append((one_json['retweetCount'], one_json['content']))
    # sort by retweet count
    top_retweeted.sort(key=lambda x: x[0], reverse=True)
    return list(map(lambda x: x[1], top_retweeted[:10]))


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
    return list(map(lambda x: x[0], top_users[:10]))


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
    return list(map(lambda x: x[0], top_days[:10]))


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
    top_hashtags = sorted(top_hashtags.items(),
                          key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], top_hashtags[:10]))


def main():
    # read json
    jsons = []
    with open('farmers-protest-tweets-2021-03-5.json') as f:
        for line in f:
            one_json = json.loads(line)
            jsons.append(one_json)

    print(top_10_retweeted(jsons))
    print(top_10_users(jsons))
    print(top_10_days(jsons))
    print(top_10_hashtags(jsons))


if __name__ == "__main__":
    main()
