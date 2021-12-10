import pickle
import random

import numpy as np
from flask import Flask, render_template, request, url_for, redirect
from sklearn.preprocessing import MinMaxScaler


app = Flask(__name__)
model = pickle.load(open('etc/saved/model', 'rb'))
min_max_scaler = MinMaxScaler()

def fix_array(*args):
	arr = np.array(args)
	arr = arr.reshape(-1, 1)
	arr = arr.reshape(1, 8) # 8 values to be passed into the model
	return arr


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/heart', methods=['GET', 'POST'])
def test():
	if request.method == 'POST':
		age = int(request.form['age'])
		gender = int(request.form['gender'])
		cp = int(request.form['cp'])
		trestbps = int(request.form['trestbps'])
		chol = int(request.form['chol'])
		fbs = int(request.form['fbs'])
		restecg = int(request.form['restecg'])
		thalach = int(request.form['thalach'])

		pred_array = fix_array(age, gender, cp, trestbps, chol, fbs, restecg, thalach)
		pred_array =  min_max_scaler.fit_transform(p)

		pred = model.predict(pred_array)



		if pred[0] == 0:
			return render_template('results.html', val=0)

		elif pred[0] == 1:
			return render_template('results.html', val=1)	

	else:
		return render_template('heart.html')


if __name__ == '__main__':
	app.run(debug=True)
