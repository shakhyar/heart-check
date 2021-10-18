# Heart-Check

Heart-Check is an open source ML project based on Decision Tree Architecture with a 88.7% accuracy used to predict the presence of a heart disease based on specific arguments that would be taken from the user as a survey. 

**NOTE: demo and notebook is not up now, will be uploaded soon**

[Working Demo](https://pip.pypa.io/en/stable/)

 [Colab Notebook](https://pip.pypa.io/en/stable/)

## Tech Stack
- I have used python flask for backend
- tailwind css and tailblocks for quick front-end
- numpy and pandas for data preprocessing
- sklearn library for ML


## DataSet
- The dataset is taken from UCI machine learning repository. 
- A total of 4 different datasets have been combined to one dataframe. 
- The used Datasets can be found in the `etc/data`directory. 
- The data was really noisy, a lot of preprocessing still had to be done on a processed dataset. The preprocessing part can be found in the jupyter notebook inside the directory `etc/`
- Few columns have been dropped, some of them were not much important, and few of them had a lot of missing values. 

## Array Descriptions
- The train and test arrays are 2D in shape. 
- The shape of the input array for prediction of the model is `(1,8)`. 
- The dataset contains 9 params, out of which the last param is the value to be predicted. So we have only 8 params for the training. 
- The the dataframe has data of more than 700 people, therefore the dataframe shape goes like `(702,8)`. 
- A split of 10% is made on the data into training and testing data.
- The inputs from the html form is taken and converted into a numpy array, first reshaped by `(-1,1)`, and then again reshaped with shape `(1,8)`, and fed into the model for prediction. 


## Model
- The test has been performed on various architectures including SGD, Random Forest, Decision Tree, KNN, SVM, out of which, the Decision Tree model was found to have the most accuracy among all, which was 88.7%
- The accepted array shape by the trained model has been discussed above. 
- The model is even lighter than the KNN model, the model size of the KNN was around 90KB, while the Decision tree was only of 30KB

## Prediction
- The model prediction is something like this : `[value] `
- The value can range from 0 to 4
- 0 is the absence of a disease, 1 to 4 indicates the presence of a heart disease, the intensity is less when 1, a little more  when 2 and so on. 
- since there were 4 presence values, dividing 100/4 would give us 25, i.e, 1=25% chance, 2=50% chance, and so on. 
- But if the prediction  is 4, declaring a 100% chance would be too stiff for a prediction, so to make it dynamic I have added a particular range of percentages for each set, and it will randomly choose among the range of given percentages.

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
