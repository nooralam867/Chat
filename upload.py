import pytesseract
from PIL import Image
import json
import os
from io import BytesIO

def handler(request):
    # Get the uploaded files
    images = request.files.getlist('images')
    questions = []

    for image in images:
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        
        # Assume the first line is the question and the following lines are options
        lines = text.split("\n")
        question = lines[0].strip()
        options = [line.strip() for line in lines[1:] if line.strip()]
        
        questions.append({
            "question": question,
            "options": options[:4]  # Limit to 4 options
        })

    return {
        "statusCode": 200,
        "body": json.dumps({'questions': questions}),
        "headers": {
            "Content-Type": "application/json"
        }
    }
  
