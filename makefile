sync:
	aws s3 sync site/ s3://$(BUCKET_NAME)/site

deploy:
	cd data-service && serverless deploy -v

clean-cache:
	aws cloudfront create-invalidation --distribution-id=${CF_DISTRIBUTION_ID} --paths "/*"