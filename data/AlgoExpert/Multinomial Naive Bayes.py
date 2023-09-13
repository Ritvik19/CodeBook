import math
from collections import defaultdict

class MultinomialNB:
    def __init__(self, articles_per_tag):
        self.alpha = 1
        self.priors_per_tag = {}
        self.likelihood_per_word_per_tag = {}
        self.articles_per_tag = articles_per_tag 
        self.tags = articles_per_tag.keys()
        self.train()

    def train(self):
        tag_counts_map = {tag: len(self.articles_per_tag[tag]) for tag in self.tags}
        self.priors_per_tag = {tag: tag_counts_map[tag] / sum(tag_counts_map.values()) for tag in self.tags}
        self.likelihood_per_word_per_tag = self.__get_word_likelihoods_per_tag()

    def predict(self, article):
        posteriors_per_tag = {tag: math.log(prior) for tag, prior in self.priors_per_tag.items()}
        for word in article:
            for tag in self.tags:
                posteriors_per_tag[tag] += math.log(self.likelihood_per_word_per_tag[word][tag])
        return posteriors_per_tag

    def __get_word_likelihoods_per_tag(self):
        word_frequencies_per_tag = defaultdict(lambda: {tag: 0 for tag in self.tags})
        total_word_counts_per_tag = defaultdict(int)
        for tag in self.tags:
            for article in self.articles_per_tag[tag]:
                for word in article:
                    word_frequencies_per_tag[word][tag] += 1
                    total_word_counts_per_tag[tag] += 1
        word_likelihoods_per_tag = defaultdict(lambda: {tag: 0.5 for tag in self.tags})
        for word, tags_map in word_frequencies_per_tag.items():
            for tag in tags_map.keys():
                word_likelihoods_per_tag[word][tag] = (word_frequencies_per_tag[word][tag] + 1 * self.alpha) / (total_word_counts_per_tag[tag] + 2 * self.alpha)
        return word_likelihoods_per_tag