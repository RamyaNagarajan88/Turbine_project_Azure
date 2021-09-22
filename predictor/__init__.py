import logging
import azure.functions as func
import numbers

from predict import calculate_generated_power

def isANumber(num):
    try:
        float(num)
        return True
    except:
        return False

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    feature_1=req.params.get('Exhaust temp')
    feature_2=req.params.get('Comp IGV angle')
    feature_3=req.params.get('Comp discharge pressure')
    feature_4=req.params.get('Comp discharge temp')

    parameters=[feature_1,feature_2,feature_3,feature_4]
    
    if all( isANumber(i) for i in parameters):
        generated_watts=calculate_generated_power([feature_1,feature_2,feature_3,feature_4])
        return func.HttpResponse(f"Predicted generated power: {generated_watts}" )
    else:
        return (f"Enter valid numbers for inputs " )
    



    

    
