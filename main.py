
import streamlit as st
import pandas as pd
import joblib

def main():
    # Simple Write Commands
    # Mainly uses a markdown style of parsing
    st.write('# Sample heading')
    st.write("""
    Example of a longer description. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque id hendrerit orci, ac posuere quam. Suspendisse quis dapibus dui. Etiam volutpat pellentesque ligula et suscipit. Curabitur facilisis urna metus, id mattis nunc scelerisque non. Curabitur commodo est sit amet massa egestas mattis. Nam vestibulum lacus erat, nec tincidunt lorem laoreet sed. Nulla convallis neque erat, sed facilisis tortor bibendum ut. Vivamus mollis tortor vel lacus euismod, sit amet semper lectus placerat. Sed porttitor libero et velit volutpat, ut scelerisque nulla elementum. Phasellus a eleifend ligula.
             
    Line breaks. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    """)
    st.write('Example of `highlighting a messagr` or not.')

    # Example of Media
    st.write('## Media')
    st.image('https://i.kym-cdn.com/entries/icons/facebook/000/048/010/side_eye_cat.jpg',
        caption='Sample Caption'         
    )
    st.video('https://files.shutokorevivalproject.com/srp-bg.mp4')

    # Pandas Stuff
    st.write('## Pandas Stuff')
    df = pd.DataFrame({
        'Numbers that are cool': [1, 4, 5, 10],
        'Words that are cool': ['supercalifragilisticexpialidocious', 'uhh', 'cheese', 'speed']
    })
    st.dataframe(df)

    # User Inputs
    # https://docs.streamlit.io/develop/api-reference/widgets
    st.write('## User Inputs')
    input_text = st.text_input('Sample Input Label')
    input_button = st.button('Sample BT Text')
    input_radio = st.radio('Sample Radio Label', [
        'do',
        'you',
        'remember',
        'the',
        '21st',
        'night',
        'of',
        'september'
    ])
    input_number_1 = st.number_input('First Num')
    st.write('\+')
    input_number_2 = st.number_input('Secon Num')

    # And using the user input
    st.write('## Using the inputs')
    st.write(f'Cool person says: {input_text}')
    if input_button:
        st.write('Yeah you hit that button')
    else:
        st.write('nuh uh')
    st.write(f'Currently selected: {input_radio}')
    st.write(f'Math aint mathin: {input_number_1 + input_number_2}')


    # Model Stuff
    using_model_version = True
    if using_model_version:
        st.write('## Using Pre-trained Models')

        # Load Model
        pipeline = joblib.load('./model-dev/RandomForestClassifier.pkl')

        # Get and validate user input
        pclass = st.radio('Pclass', [1, 2, 3])
        sex = st.radio('Sex', ['male', 'female'])
        age = st.number_input('Age')
        sibsp = st.number_input('SibSp', step=1)
        parch = st.number_input('Parch', step=1)
        fare = st.number_input('Fare')
        embarked  = st.radio('Embarked', ['C', 'Q', 'S'])

        st.write('### Prediction')
        if all([pclass, sex, age, fare, embarked]):

            # Prediction
            user_form = pd.DataFrame({
                'Pclass': [pclass],
                'Sex': [sex],
                'Age': [age],
                'SibSp': [sibsp],
                'Parch': [parch],
                'Fare': [fare],
                'Embarked': [embarked]
            })
            pred = pipeline.predict(user_form)
            st.write('Random Forest Classifier Prediction: ', 'Surived' if pred else 'Ded asf')

        else:
            st.write('Please fill out form above.')
    

if __name__ == "__main__":
    main()
