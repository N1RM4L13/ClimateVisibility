import os
from prediction.validation_insertion import pred_validation
from training.train_model import trainModel
from training.validation_insertion import train_validation
from prediction.predict_model import prediction

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


try:

    path = 'Training_Batch_Files'
    train_valObj = train_validation(path) #object initialization

    train_valObj.train_validation()#calling the training_validation function


    trainModelObj = trainModel() #object initialization
    trainModelObj.trainingModel() #training the model for the files in the table


except ValueError:

    print("Error Occurred! %s" % ValueError)

except KeyError:

    print("Error Occurred! %s" % KeyError)

except Exception as e:

    print("Error Occurred! %s" % e)
# print("Training successfull!!")



# try:
#     path = 'Prediction_Batch_Files'

#     pred_val = pred_validation(path) #object initialization

#     pred_val.prediction_validation() #calling the prediction_validation function

#     pred = prediction(path) #object initialization

#     # predicting for dataset present in database
#     path = pred.predictionFromModel()
#     print("Prediction File created at %s!!!" % path)

# except ValueError:
#     print("Error Occurred! %s" %ValueError)
# except KeyError:
#     print("Error Occurred! %s" %KeyError)
# except Exception as e:
#     print("Error Occurred! %s" %e)













