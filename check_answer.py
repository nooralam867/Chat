import json
import random

def handler(request):
    data = request.json
    question_index = data['questionIndex']
    option_index = data['optionIndex']
    
    # Simulating AI to randomly determine if the answer is correct
    is_correct = random.choice([True, False])
    
    message = "Correct!" if is_correct else "Incorrect"
    
    return {
        "statusCode": 200,
        "body": json.dumps({'message': message}),
        "headers": {
            "Content-Type": "application/json"
        }
    }
  
