import numpy as np
from scipy.spatial import distance
from sklearn.feature_extraction.text import TfidfVectorizer
#import sklearn.feature_extraction.text
class VDC():
    def __init__(self, class_threshold=0.25, use_idf=True, binary=True, max_features=100):
        self.Vectorizer = TfidfVectorizer(use_idf=use_idf, binary=binary, max_features=max_features)
        self.class_threshold = class_threshold
        self.model_vector = None


    def fit(self, train_text: list):
        self.model_vector = np.mean(self.Vectorizer.fit_transform(train_text), axis=0)
    

    def predict(self, test_texts: list, in_binary=True):
        results = []
        for tt in test_texts:
            test_vector = self.Vectorizer.transform([tt])
            dist = np.mean(distance.cdist(self.model_vector, test_vector.toarray(), 'euclidean'))
            if in_binary:
                if dist <= self.class_threshold:
                    results.append(True)
                else:
                    results.append(False)
            else:
                results.append(dist)
        return results