import os
import json
import boto3
import re
from operator import add
import string



# Initialize s3 client
s3 = boto3.client('s3')


# File processor method
def process_file(original_file, processed_file, stopword_file):
    with open(original_file, 'r') as inputfile:
        
        # Read input file to string
        textData=inputfile.read()
        
        lowerCase = textData.lower()
        textData = re.sub(r'[^a-zA-Z ]','',lowerCase)
        words = textData.split(' ')

        # Read stopword file
        with open(stopword_file, 'r') as stopwordfile:
            stopworddata = stopwordfile.read()
        
        # Split stopwords to list
        stopwords = stopworddata.splitlines()
        filterword=[]
        for word in words:
            if word not in stopwords and word != '':
                filterword.append(word)
                
        textData = ' '.join(filterword)

        
        # Process text here
        # -----------------
        # Strip stopwords
        #for word in stopwords:
        #    textData = textData.replace(word, "")
        
        # Write processed text to file
        text_file = open(processed_file, "w")
        text_file.write(textData)
        text_file.close()
    

# Main handler method
def lambda_handler(event, context):
    
    # Get information from incoming S3 event
    for record in event['Records']:
    
        # Get input bucket and file names from event
        input_bucket = record['s3']['bucket']['name']
        input_filename = record['s3']['object']['key']
        
        # Set ouput bucket and file names
        output_bucket = input_bucket + '-output'
        output_filename = input_filename
        
        # Set local Lambda file paths for text files
        original_file = '/tmp/{}'.format(input_filename)
        processed_file = '/tmp/{}'.format(input_filename)
        stopword_file = '/var/task/stopword.txt'
        
        # Save the input object to disk in Lambda
        s3.download_file(input_bucket, input_filename, original_file)

        # Process the object
        process_file(original_file, processed_file, stopword_file)

        # Upload the processed object to S3 output bucket
        s3.upload_file(processed_file, output_bucket, output_filename)

    return {
        "statusCode": 200,
        "body": json.dumps('Processing completed successfully')
    }

