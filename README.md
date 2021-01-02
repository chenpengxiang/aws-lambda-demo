## Demo Test 

This is a demo for using aws lambda to provide typeahead data. There are two parts:

1.  [site](site) is static resources which sync up to S3 bucket and using CloudFront to access the resources.
2.  [data-service](data-service) is a lambda function to provide dynamic data.



## Environment Setup


- Install [aws cli2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

  ```
  # configure credentials for aws cli 
  # AWS Access Key ID [None]: xxxxx
  # AWS Secret Access Key [None]: xxxxxx
  # Default region name [None]: us-east-1
  $ aws configure
  
  # sync site files to S3 bucket
  
  $ aws s3 sync site/ s3://<mybucket>/site
  ```

  

- Install Python 3.6+

- Install [serverless framework](https://github.com/serverless/serverless) 

  ```
  # create a serverless project using template aws-python3
  $ serverless create --template aws-python3 --path data-service
  ```

  

## Deployment

 [makefile](makefile)   

- BUCKET_NAME  --  uploading the site static files to the bucket
- CF_DISTRIBUTION_ID -- To clean cache for CloudFound distribution id

```
make sync   # sync the site folder to the s3 bucket
make deploy # deploy get data lambda function 
make clean-cache # to clean cloudfront cache
```

   

### Demo 

url:  https://xxxx.cloudfront.net/html/demo.html

input options using:  aws, lang, 鞋子





