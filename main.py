import pickle
import random

import numpy as np
import pandas as pd
from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename



app = Flask(__name__)
model = pickle.load(open('etc/saved/model', 'rb'))

classes = ['age', 'gender', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
           'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

classes_to_drop = ['exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']


def fix_array(*args):
	arr = np.array(args)
	arr = arr.reshape(-1, 1)
	arr = arr.reshape(1, 8) # 8 values to be passed into the model
	return arr


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/bulk', methods=['POST', 'GET'])
def bulk():
	if request.method == "POST":
		f = request.files['file']
		fname = f.filename
		f.save(secure_filename(f.filename))
		data = pd.read_csv(f.filename)

		data.columns = classes
		for i in classes_to_drop:
			data.drop(i, inplace=True, axis=1)


		pred = model.predict(data)

		
		return render_template('bulk_result.html', pred=list(pred))

	else:
		return render_template("bulk.html")




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

		pred = model.predict(pred_array)



		if pred[0] == 0:
			return render_template('results.html', val=0)

		elif pred[0] == 1:
			return render_template('results.html', val=1)	

	else:
		return render_template('heart.html')


if __name__ == '__main__':
	app.run(debug=True)