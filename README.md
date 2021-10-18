# Heart-Check

Heart-Check is an open source ML project used to predict the presence of a heart disease based on specific arguments that would be taken from the user as a survey. 
[Working Demo](https://pip.pypa.io/en/stable/)[Colab Notebook](https://pip.pypa.io/en/stable/)

## Installation
Just clone the repo, and use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.


```bash
pip install -r requirements.txt
```

## Usage
Run `main.py` in the terminal, and the site will be up running on `127.0.0.1:5000`

To use the model for other purposes you have to deserialize the pickle file, present in /etc/saved/
```python
import pickle

model = pickle.load
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
