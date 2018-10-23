# project-3-serverless-massey-cai

# Part A  

# Lambda: Project3_S3_Processor

# For the first part - striping the stopwords, changing to lowercase and filtering non-alphabatic chars, we create a Python 3.6 Lambda function called Project3_S3_Processor. The lambda is configured with an IAM role to allow it to access our S3 bucket. It is set to trigger on an s3:ObjectCreated:* event from our bucket csci5253-fall2018-project3-massey-cai.  Whenever an object is created, the S3 bucket will publish an event and the Lambda function will be triggered.  Then we create a lambda handler function called lambda_handler. Handler function takes the event notified by s3 as an input which contains the input bucket and input file. We then retrieve the file from S3 and download it to Lambda's tmp dir. After that, we can process the file to filter the stopwords, empty strings, and non-alphabatic characters in the string. Then we output the transformed string to a new file in the Lambda tmp dir and upload the new file to the output bucket we designated. 

# Lambda: Project3_S3_WordCount

# For the second part - word count, we created a Python 3.6 Lambda function called Project3_S3_WordCount. The lambda is configured with an IAM role to allow it to access our S3 bucket. It is set to trigger from an AWS API Gateway (https://31z9b3m289.execute-api.us-west-2.amazonaws.com/default/). When that API is accessed, the Lambda function is triggered. The Lambda retrieves the list of objects in or S3 output bucket the iterates through each file. It splits the file contents into a string array of words and then iterates through each word. We create a counts dictionary of key value pairs to keep track of the word count for each word. As we loop through each word, we increment the counter for that word by one. After counting all words, we sort the dictionary by value. We then output the sorted list to a wordcount.txt file in the Lambda's tmp directory and upload it to our S3 bucket. 
