from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Person
import pandas as pd
import pickle
import os
import logging
logger = logging.getLogger(__name__)

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Render the index page
def index(request):
    return render(request, 'index.html')

# Render the predict page
def predict(request):
    return render(request, 'predict.html')

# Render the BMI page
def bmi(request):
    return render(request, 'bmi.html')

# Handle the form submission for prediction
@csrf_protect
def predict_action(request):
    try:
        if request.method == 'POST':
            # Extract form data and perform the necessary conversions
            name = request.POST['name']
            age = int(request.POST['age'])
            marital_status = request.POST['maritalstatus']
            work_type = request.POST['Worktype']
            residence = request.POST['Residence']
            gender = request.POST['gender']
            bmi = float(request.POST['bmi'])
            gluc_level = float(request.POST['gluclevel'])
            smoke = request.POST['Smoke']
            hypertension = request.POST['Hypertension']
            heart_disease = request.POST['Heartdisease']
            logger.info(f"Input Data: {request.POST}")
             

            # Perform necessary conversions and calculations
            residence = 1 if residence == 'urban' else 0
            gender = 1 if gender == 'Male' else 0
            marital_status = 1 if marital_status == 'married' else 0
            work_type = {'privatejob': 2, 'govtemp': 1, 'selfemp': 3}.get(work_type, 0)
            smoke = {'formerly-smoked': 1, 'non-smoker': 2, 'smoker': 3}.get(smoke, 0)
            hypertension = 1 if hypertension == 'hypten' else 0
            heart_disease = 1 if heart_disease == 'heartdis' else 0 



            # Save data to the database
            Person.objects.create(
                name=name, age=age, marital_status=marital_status, work_type=work_type,
                residence=residence, gender=gender, bmi=bmi, gluc_level=gluc_level,
                smoke=smoke, hypertension=hypertension, heart_disease=heart_disease
            )

            # FOR DECISION TREE
            """ name = request.POST['name']
            age = int(request.POST['age'])
            bmi = float(request.POST['bmi'])
            gluc_level = float(request.POST['gluclevel'])
            smoke = request.POST['Smoke'] """ 
            """Person.objects.create(
                name=name, age=age, bmi=bmi, gluc_level=gluc_level,smoke=smoke) """  #DESCION tree
            #model_path = "C:\\Users\\HC\\StrokePrediction\\StrokePrediction\\std.pkl"

             # Create a DataFrame with the input data
            """input_data = pd.DataFrame([[age,gluc_level, bmi,smoke]],
                                        columns=['age','avg_glucose_level', 'bmi', 'smoking_status'])"""

            logger.info(f"Input Data: {request.POST}")
            
            # Load the trained model using the dynamic path
            model_path = "C:\\Users\\HC\\StrokePrediction\\StrokePrediction\\strokenew.pkl"
            with open(model_path, "rb") as model_file:
                model = pickle.load(model_file)
                print ("Model LOded successfully")

            # Create a DataFrame with the input data
            input_data = pd.DataFrame([[gender,age, hypertension, heart_disease, marital_status, work_type, residence,gluc_level, bmi, smoke]],
                                        columns=['gender' ,'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type',
                                               'residence_type', 'avg_glucose_level', 'bmi', 'smoking_status'])
            logger.info(f"Input Data for Prediction: {input_data}")
            
           
            logger.info(f"Input Data for Prediction: {input_data}")
            # Make predictions using the loaded model
            Predict = model.predict(input_data)
            print(Predict)
            
            if Predict== 0:
                print ("you will not get a stroke 😀")
            else:
                print ("you will get a stroke 😔" )
            


            # Provide a result message based on the prediction
            if Predict== 0:
                str_result = f"{name}, you will not get a stroke 😀"
            else:
                str_result = f"{name}, you will get a stroke 😔"

            #logger.error(f"Error in predict_action: {Predict}", exc_info=True)
           
           
            # Render the predict page with the result message
            return render(request, 'predict.html', {'prediction':str_result})
    except (KeyError, ValueError):
        
        # Handle form data extraction or conversion errors
        return render(request, 'predict.html', {'result': 'Error in form data'})

# Render the CTA page
def cta(request):
    return render(request, 'cta.html')

# Render the counsel page
def counsel(request):
    return render(request, 'counsel.html')
