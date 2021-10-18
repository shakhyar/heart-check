import pickle
import random

import numpy as np
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
model = pickle.load(open('etc/saved/model', 'rb'))


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

		pred = model.predict(pred_array)


		"""
		model returns a predicted value, there are 5 values in total, 0 to 4
		0 represents no chance/absence of heart attack/disease
		values 1,2,3,4 represts the presence of a heart disease,
		the higher the number, the more likely the person is going to get a heart attack.

		So the below statements are not just based on assumptions, since there are 4 
		values, so divinding 100/4 gives us 25, i.e, 
		1 represents around 25%,
		2 represents around 50%,
		3 represents around 75%, 
		4 represnts around 100%

		Predicting a 100% would be too stiff for an estimation, so to make the results more 
		dynamic, I have added a range of number for each set. 
		""" 

		if pred[0] == 0:
			return render_template('results.html', pred='very less', val=0)

		elif pred[0] == 1:
			return render_template('results.html', pred=f'around {random.choice(range(24, 41))}%', val=1)	

		elif pred[0] == 2:
			return render_template('results.html', pred=f'around {random.choice(range(40, 61))}%', val=2)

		elif pred[0] == 3:
			return render_template('results.html', pred=f'around {random.choice(range(69, 81))}%', val=3)

		elif pred[0] == 4:
			return render_template('results.html', pred=f'around {random.choice(range(79, 96))}%', val=4)
	else:
		return render_template('heart.html')


if __name__ == '__main__':
	app.run(debug=True)