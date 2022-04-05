# Thank you to COMP 474 teaching team W2022
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from collections import Counter
import spacy

nlp = spacy.load("en_core_web_sm")
corpus = [
    'Who is Bill Gates',
    'Where is Concordia located',
    'What is AI',
    'What city is McGill located in',
    'Who is McGill'
]

# Create the features and convert the feature matrix to a numpy array
features = []
for text in corpus:
    features.append(create_features(text))

feature_mtrx = np.array(features)

# Assign integer labels
le = LabelEncoder()
feature_mtrx[:, 0] = le.fit_transform(feature_mtrx[:, 0])

# 0=Who, 1= Where, 2=What
y = np.array([0, 1, 2, 2, 0])

clf = DecisionTreeClassifier(random_state=0)
clf.fit(feature_mtrx, y)

q = "Where is Canada"

clf.predict(q)

def create_features(text):
    doc = nlp(text)
    pos_list = [] # Create a list with all the POS tags in the text
    pos_count_dict = Counter(pos_list) # Count the number of POS tags withing the POS list
    entity_list = [] # Create a list with all the entities within the text
    ent_count_dict = Counter(entity_list) #Count the number of entity types withing the entity list
    root_lemma =  # Lemma of the root token in the text
    sentence_length = # Length of the text (number of characters within the text)

    return [root_lemma, pos_count_dict['WP'], pos_count_dict["WRB"], ent_count_dict["PERSON"], ent_count_dict["GPE"], ent_count_dict['ORG'], sentence_length]