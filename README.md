
# Streamlit Demo
This repository contains files for the Project Website Workshop for DataHacks 2024. This workshop is targeted towards students who want to create website for their project and have a working model embedded inside.

## Installation 
1. (Fork and) Clone the repo.
2. Create a virtual environment and install required packages as specified in the `requirements.txt`.
```bash
python3 -m venv your_env
source your_env/bin/activate  # 'source your_env/Scripts/activate' if on Windows
pip install -r requirements.txt
```
3. Launch you local server by running the following.
```
streamlit run main.py
```

## Saving Models for Production
An example of this being done is under `model-dev/model-dev.ipynb`.
1. You may be working on developing your model in your Jupyter Notebook. You will need to import `joblib` in order to save your model to a file.
```python
# https://joblib.readthedocs.io/en/stable/
import joblib
```
2. In this case, we are serializing (saving) a Scikit-Learn pipeline using a RFC based on the famous [Titanic dataset](https://www.kaggle.com/competitions/titanic/overview). Use `dump` to save your model.
```python
# dump( <YOUR_ML_MODEL_OBJ>, <FILENAME> )
joblib.dump(pipeline, "RandomForestClassifier.pkl")
```
3. Find what version of the package of the model you are using. In this case I am using Scikit-Learn so I need to find out which version of Scikit-Learn I used in my notebook.
```python
!pip list | grep scikit-learn
# scikit-learn  1.2.1
```

## Using Pre-trained Models in Streamlit
An example of this being done is under `main.py` starting from [line 63](https://github.com/ucsdds3/streamlit-demo/blob/5af213f5d185516edfad25bbc2344ef6d93c7054/main.py#L63).
1. In some but not all cases, the version in your virtual environment may not the one in the Jupyter Notebook. This is especially common if you are using a Conda environment. Ensure in your virtual environment that you have the **same version** of your ML package used in your notebook.
If they do not match, uninstall the package and re-install it using the correct version.
```bash
pip uninstall scikit-learn
pip install scikit-learn==1.2.1
```
2. In your Streamlit file import `joblib`. Use the `load` function to load your model into an variable. From there, you can treat it as the same as the model from the notebook.
```python
import joblib

# load( <FILEPATH_TO_MODEL> )
pipeline = joblib.load('./model-dev/RandomForestClassifier.pkl')
```
3. Generate user inputs that are inline with the model inputs. Use that to predict. An example using the Titanic pipeline is below
```python
# Get and validate user input
pclass = st.radio('Pclass', [1, 2, 3])
sex = st.radio('Sex', ['male', 'female'])
age = st.number_input('Age')
sibsp = st.number_input('SibSp', step=1)
parch = st.number_input('Parch', step=1)
fare = st.number_input('Fare')
embarked  = st.radio('Embarked', ['C', 'Q', 'S'])
```
4. Deploy using the `Deploy` button at the top right.

## License
This project is licensed under the MIT License. See `LICENSE` for more information.
