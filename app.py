import json

def lambda_handler(event, context):
    # Your main logic goes here
    message = "Hello from my first CI/CD pipeline! 🚀"
    
    # Return a response that API Gateway understands
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': message,
            'event': event # This helps you see what data API Gateway sends
        })
    }