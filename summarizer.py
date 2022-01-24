import numpy as np
import networkx as nx  # For TextRank using networkx.pagerank()
from nltk.corpus import stopwords as stop_words
from nltk.cluster.util import cosine_distance

import sys


def read_article(file):

    with open(file, 'r', encoding='utf-8') as f:

        fcontent = f.read().split('. ')
        sentences = []

        for sentence in fcontent:
            sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))  # List of words in the sentence
        
        sentences.pop()
        return sentences


def sentence_similarity(sentence1, sentence2, stopwords=None):
    
    if stopwords is None:
        stopwords = []
    
    sentence1 = [w.lower() for w in sentence1 if w not in stopwords]
    sentence2 = [w.lower() for w in sentence2 if w not in stopwords]

    vocab = list(set(sentence1 + sentence2))  # sentence1 and sentence2 are the lists of words in the sentences

    vec1 = [0 for i in range(len(vocab))]  # Embeddings from vocab for sentence1 
    vec2 = [0 for i in range(len(vocab))]  # Embeddings from vocab for sentence2

    for word in sentence1:
        vec1[vocab.index(word)] += 1

    for word in sentence2:
        vec2[vocab.index(word)] += 1

    return 1 - cosine_distance(vec1, vec2)



def create_similarity_matrix(sentences, stopwords):

    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:  # Same sentences
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(
                                                                sentences[idx1],
                                                                sentences[idx2],
                                                                stopwords
                                                                )

    return similarity_matrix


def generate_summary(file, n=5):
    """Retuens a list of n sentences in the given file. n=5 when unspecified.
    """

    stopwords = stop_words.words('english')
    summary = []

    sentences = read_article(file)

    sentence_similarity_matrix = create_similarity_matrix(sentences, stopwords)

    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank((sentence_similarity_graph))

    ranked = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    for i in range(n):
        summary.append(" ".join(ranked[i][1]))  # Splitting was done on " ".
                                                # ranked contains tuples with first element being score
        
        # One top sentence is added to summary on each iteration of this loop

    return summary


if __name__ == "__main__":


    args = sys.argv
    file = args[1]
    if len(args) == 2:
        summary = generate_summary(file)
    elif len(args) == 3:
        n = int(args[2])
        summary = generate_summary(file, n)
    elif len(args) == 4:
        n = int(args[2])
        output = args[3]
        summary = generate_summary(file, n)
        with open(output, 'w') as ofile:
            ofile.writelines(["\n\n" + "-"*80 + "\n\n" + summaryline for summaryline in summary])
        exit(0)
    
    print("Summary of given text file is:\n\n\n")
    for sentence in summary:
        print("\n\n" + "-"*80 + "\n\n" + sentence)