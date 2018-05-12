# Document Classifier
This Document Classifier is developed to automatically determine which violence a given document (academic papers, etc.) is about. 

## How it works (in a high-level sense)
The classifier utilizes the term-frequency method to vectorize the docuements. The "model" vector is currently set to be the *mean* of the training documents, then a test document is classified by measuring the distance between the test document's vector and the "model" vector.

## Potential ways to improve performance
- Use a better distance metric. The version now uses a Euclidean distance.
- Tweaking parameters, including the size of the vector (i.e. how many words are we only considering). Currently, the model only considers the top-100 words of the training data.
- Etc.

## Issues
- The model currently only tells how *similar* the test document is to the training documents, which could potentially lead to accuracy issues.
- The trained model's performance could be affected, if some documents are used to train in more than one models. Currently, some documents are classified as more than one violences.