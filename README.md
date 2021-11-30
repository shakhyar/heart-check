reading time: 3 mins 
# Heart-Check



Heart-Check is an open source ML project based on KNN Architecture with a 92.3% accuracy used to predict the presence of a heart disease based on specific arguments that would be taken from the user as a survey. 


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
- The test has been performed on various architectures including SGD, Random Forest, Decision Tree, KNN, SVM, out of which, the KNN model was found to have the most accuracy among all, which was 92.3%
- The accepted array shape by the trained model has been discussed above.


## Prediction
- The model prediction is something like this : `[value] `
- It wasn't exactly a binary classification problem. The target values were 0, 1, 2, 3 and 4. Any value above 0 is considered as positive. To make performance better in such a noisy dataset, this was the best option to get higher accuracy.
```python
		if pred[0] == 0:
			return render_template('results.html', val=0)

		elif pred[0] == 1:
			return render_template('results.html', val=1)

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
