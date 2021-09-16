# inference.py

import os

import numpy as np
from joblib import load
from sklearn import datasets
from sklearn.utils import shuffle

MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE = os.environ["MODEL_FILE"]
METADATA_FILE = os.environ["METADATA_FILE"]

MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_FILE = os.path.join(MODEL_DIR, METADATA_FILE)

def get_test_data():
	"""
	Fetch data for inference.
	"""
	print("Loading data...")
	boston = datasets.load_boston()
	X, y = shuffle(boston.data, boston.target, random_state=13)
	X = X.astype(np.float32)
	offset = int(X.shape[0] * 0.9)
	X_test, y_test = X[offset:], y[offset:]
	return X_test, y_test

def inference():
	"""
	Run batch inference on test data.
	"""
	X, y = get_test_data()

	# Load model
	print(f"Loading model from: {MODEL_PATH}")
	clf = load(MODEL_PATH)

	# Predict
	print("Generating predictions...")
	preds = clf.predict(X)
	print(preds)


if __name__ == '__main__':
	inference()

