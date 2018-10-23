import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
  
    counts = dict()
    output_file = '/tmp/wordcount.txt'
    temp_file = '/tmp/tmp.txt'
    
    bucket_name = 'csci5253-fall2018-project3-massey-cai-output'
    bucket = s3.Bucket(bucket_name)
    bucket_list = bucket.objects.all()

    # Count all words
    for file in bucket_list:
        bucket.download_file(file.key, temp_file)
        with open(temp_file, 'r') as inputfile:
            textData=inputfile.read()
            words = textData.split(' ')
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
                
    # Sort word count
    sorted_by_value = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Write processed text to file
    with open(output_file,'w') as f:
        for (word, count) in sorted_by_value:
            f.write(str(word)+'\t'+str(count)+'\n')

    # Upload the output file to S3 output bucket
    bucket.upload_file(output_file, 'wordcount.txt')
    
    # TODO implement
    return {
        "statusCode": 200,
        "body": json.dumps('Word Count completed')
    }
