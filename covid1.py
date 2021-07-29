 
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
import datetime
model = load_model('saved_model')






def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('covidimage.jpg')
    image_office = Image.open('coprecautionimage.jpg')
    
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict if a patient survived or not')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predicting Corona Survival")
    st.image(image,width=100,use_column_width=False)
    if add_selectbox == 'Online':
        sex = st.radio("sex: ", ('Male', 'Female'))
        if (sex == 'Male'):
          sex=2
        else:
          sex=1
        patient_type = st.radio("patient_type: ", ('Outpatient', 'Inpatient'))
        if (patient_type == 'Outpatient'):
          patient_type=1
        else:
          patient_type=2
        entry_date=st.date_input('entry_date' ,datetime.date.today())
        date_symptoms=st.date_input('date_symptoms' , datetime.date.today())
        intubed = st.radio("intubed", ('Yes', 'No'))
        if (intubed == 'Yes'):
            intubed=1
        else:
            intubed=2

        pneumonia = st.radio("pneumonia", ('Yes', 'No'))
        if (pneumonia == 'Yes'):
            pneumonia=1
        else:
            pneumonia=2
        age=st.number_input('age' , min_value=1, max_value=80, value=1)
        pregnancy = st.radio("pregnancy", ('Yes', 'No'))
        if (pregnancy == 'Yes'):
            pregnancy=1
        else:
            pregnancy=2
        diabetes = st.radio("diabetes", ('Yes', 'No'))
        if ( diabetes == 'Yes'):
            diabetes=1
        else:
            diabetes=2
        copd = st.radio("copd", ('Yes', 'No'))
        if ( copd == 'Yes'):
            copd=1
        else:
            copd=2

        asthma = st.radio("asthma", ('Yes', 'No'))
        if ( asthma == 'Yes'):
            asthma=1
        else:
            asthma=2
        inmsupr = st.radio("inmsupr", ('Yes', 'No'))
        if (  inmsupr == 'Yes'):
              inmsupr=1
        else:
            inmsupr=2
        hypertension = st.radio("hypertension", ('Yes', 'No'))
        if (   hypertension == 'Yes'):
              hypertension=1
        else:
              hypertension=2
        other_disease = st.radio("other_disease", ('Yes', 'No'))
        if (   other_disease == 'Yes'):
              other_disease=1
        else:
              other_disease=2
        cardiovascular = st.radio("cardiovascular", ('Yes', 'No'))
        if (cardiovascular == 'Yes'):
            cardiovascular=1
        else:
            cardiovascular=2

        obesity = st.radio("obesity", ('Yes', 'No'))
        if (obesity == 'Yes'):
            obesity=1
        else:
              obesity=2

        renal_chronic = st.radio("renal_chronic", ('Yes', 'No'))
        if (renal_chronic == 'Yes'):
            renal_chronic=1
        else:
              renal_chronic=2

        tobacco = st.radio("tobacco", ('Yes', 'No'))
        if (tobacco == 'Yes'):
            tobacco=1
        else:
              tobacco=2

        contact_other_covid = st.radio("contact_other_covid", ('Yes', 'No'))
        if (contact_other_covid == 'Yes'):
            contact_other_covid=1
        else:
              contact_other_covid=2

        covid_res = st.selectbox("covid_res", ('Positive', 'Negative', 'Awaiting'))
        if ( covid_res == 'Positive'):
              covid_res=1
        elif ( covid_res == 'Negative'):
              covid_res=2 
        else:
              covid_res=3

        icu = st.radio("icu", ('Yes', 'No'))
        if ( icu == 'Yes'):
              icu=1
        else:
              icu=2
        output=" "
        input_dict={'sex':sex,'patient_type':patient_type,'entry_date':entry_date,'date_symptoms':date_symptoms,'intubed': intubed,'pneumonia':pneumonia,'age' : age,'pregnancy' : pregnancy,'diabetes' : diabetes,'copd' : copd,'asthma' : asthma,'inmsupr' : inmsupr,'hypertension' : hypertension,'other_disease' : other_disease,
'cardiovascular' : cardiovascular,'obesity' : obesity,'renal_chronic' : renal_chronic,'tobacco' : tobacco,'contact_other_covid' : contact_other_covid,'covid_res' : covid_res,'icu' : icu}
        input_df = pd.DataFrame([input_dict])
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
        st.success('Survive: {}'.format(output))
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
