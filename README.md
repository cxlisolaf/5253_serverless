# project-3-serverless-massey-cai

####  

* When creating the S3 bucket, we add notification configuration to the source bucket. In our case, we configure the notification as s3:ObjectCreated:* even type,so that whenever an object is created, the S3 bucket will publish event to Lambda function, which has been permitted the access to the S3. 

* For the first part - striping the stopwords,change to lowercase and filtering non-alphabatic chars, we create a lambda function called Project3_S3_Processor. And then add S3 as a trigger of the function. Then we create a lambda hanlder function called lambda_handler. Handler function takes the event notified by s3 as an input which contains the input bucket and input file. Then create an output bucket and output file. We also need to specify the temporary local file path in Lambda and download the file from s3 to Lambda local path. After that, we can process the file to filter the stopwords, empty strings, and non-alphabatic characters in the string.  

* For the second part - word count.
