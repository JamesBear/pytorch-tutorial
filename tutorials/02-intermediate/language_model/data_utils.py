import torch
import os


class Dictionary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0
    
    def add_word(self, word):
        if not word in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1
    
    def __len__(self):
        return len(self.word2idx)


class Corpus(object):
    def __init__(self):
        self.dictionary = Dictionary()

    def get_data(self, path, batch_size=20):
        # Add words to the dictionary
        with open(path, 'r') as f:
            tokens = 0
            #for line in f:
            #    words = line.split() + ['<eos>']
            #    tokens += len(words)
            #    #for word in words: 
            content = f.read()
            for c in content: 
                self.dictionary.add_word(c)
        tokens = len(content)
        
        # Tokenize the file content
        ids = torch.LongTensor(tokens)
        token = 0
        for token, c in enumerate(content):
            ids[token] = self.dictionary.word2idx[c]
        #with open(path, 'r') as f:
        #    for line in f:
        #        words = line.split() + ['<eos>']
        #        for word in words:
        #            ids[token] = self.dictionary.word2idx[word]
        #            token += 1
        num_batches = ids.size(0) // batch_size
        ids = ids[:num_batches*batch_size]
        return ids.view(batch_size, -1)