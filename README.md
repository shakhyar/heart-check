# Heart-Check

Heart-Check is an open source ML project used to predict the presence of a heart disease based on specific arguments that would be taken from the user as a survey. 
[Working Demo](https://pip.pypa.io/en/stable/)[Colab Notebook](https://pip.pypa.io/en/stable/)

## Tech Stack
- I have used python flask for quick web prototyping
- sklearn library for ML
- Decision Tree Architecture for the model

## Array Descriptions
The train, test arrays are 2D in shape. 

The shape of the input array of the model is `(1,8)`. 

-The dataset contains 9 params, out of which the last param is the value to be predicted. So we have only 8 params for the training. 
-The the dataframe has data of more than 700 people, therefore the dataframe shape goes like (702,8). 
-A split of 10% is made on the data into training and testing data.
-The inputs from the html form is taken and converted into a numpy array, first reshaped by `(-1,1)`, and then again reshaped with shape `(1,8)`, and fed into the model for prediction. 


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
