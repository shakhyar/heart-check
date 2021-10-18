reading time: 3 mins 
# Heart-Check



Heart-Check is an open source ML project based on Decision Tree Architecture with a 88.7% accuracy used to predict the presence of a heart disease based on specific arguments that would be taken from the user as a survey. 


[Working Demo](https://heartcheck.pythonanywhere.com)

 [Colab Notebook](https://colab.research.google.com/github/shakhyar/heart-check/blob/main/etc/train.ipynb)

## Tech Stack
- I have used python flask for backend
- tailwind css and tailblocks for quick front-end
- numpy and pandas for data preprocessing
- sklearn library for ML


## DataSet
- The dataset is taken from [UCI machine learning repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease) . 
- A total of 4 different datasets have been combined to one dataframe. 
- The used Datasets can be found in the `etc/data`directory. 
- The data was really noisy, a lot of preprocessing still had to be done on a processed dataset. The preprocessing part can be found in the jupyter notebook inside the directory `etc/`
- Few columns have been dropped, some of them were not much important, and few of them had a lot of missing values.
- Remaining Classes/Columns:
```python
classes = ['age', 'gender', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'target']
```


## Array Descriptions
- The train and test arrays are 2D in shape. 
- The shape of the input array for prediction of the model is `(1,8)`. 
- The dataset contains 9 params, out of which the last param is the value to be predicted. So we have only 8 params for the training. 
- The dataframe has data of more than 700 people, therefore the dataframe shape goes like `(708,8)`.
- A split of 10% is made on the data into training and testing data.
 ```python 
 x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 0) 
 ```
- The inputs from the html form is taken and converted into a numpy array, first reshaped by `(-1,1)`, and then again reshaped with shape `(1,8)`, and fed into the model for prediction. 
```python
pred = np.array([73,0,3,160,0,0,1,121])
pred = pred.reshape(-1, 1)
pred = pred.reshape(1, 8)

history = model.predict(pred)
print(history) # [1]

```


## Model
- The test has been performed on various architectures including SGD, Random Forest, Decision Tree, KNN, SVM, out of which, the Decision Tree model was found to have the most accuracy among all, which was 88.7%
- The accepted array shape by the trained model has been discussed above. 
- The model is even lighter than the KNN model, the model size of the KNN was around 90KB, while the Decision tree was only of 30KB

## Prediction
- The model prediction is something like this : `[value] `
- The value can range from 0 to 4
- 0 is the absence of a disease, 1 to 4 indicates the presence of a heart disease, the intensity is less when 1, a little more  when 2 and so on. 
- since there were 4 presence values, dividing 100/4 would give us 25, i.e, 1=25% chance, 2=50% chance, and so on. 
- But if the prediction  is 4, declaring a 100% chance would be too stiff for a prediction, so to make it dynamic I have added a particular range of percentages for each set, and it will randomly choose among the range of given percentages. The code can be seen below(from `main.py`)

```python
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

```

## Installation
Just clone the repo, and use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.


```bash
pip install -r requirements.txt
```

## Usage
Run `main.py` in the terminal, and the site will be up running on `127.0.0.1:5000`

To use the model for other purposes you have to deserialize the pickle file, present in `/etc/saved/`

```python
import pickle

filename='etc/saved/model'
model = pickle.load(open(filename, 'rb'))

history = model.predict(array)
print(f'predicted:{history[0]}, model score: {model.score})

```
