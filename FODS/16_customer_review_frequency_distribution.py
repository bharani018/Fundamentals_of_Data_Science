import collections


def frequency_distribution(text):
    words = text.split()
    word_counts = collections.Counter(words)
    return word_counts


if __name__ == "__main__":
    with open("customer_review.txt") as f:
        text = f.read()
    word_counts = frequency_distribution(text)
    print(word_counts)
