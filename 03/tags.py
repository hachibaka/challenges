import re
from collections import Counter
from nltk.stem import WordNetLemmatizer

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED) as f:
        data = f.read().strip()
    return [x.replace('-',' ').lower() for x in TAG_HTML.findall(data)]



def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    wordnet_lemmatizer = WordNetLemmatizer()
    similar_words = []
    for word in tags:
        lemmaword = wordnet_lemmatizer.lemmatize(word)
        if lemmaword != word and lemmaword in tags:
            similar_words.append((lemmaword, word))

    return similar_words


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
