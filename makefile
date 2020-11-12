sync:
	aws s3 sync site/ s3://$(BUCKET_NAME)/site

deploy:test
	cd data-service && serverless deploy -v

test:
	cd data-service && python -m unittest test-handler.py

local-invoke:
	cd data-service && serverless invoke -f getData -l -p api-gateway-event.json

	
clean-cache:
	aws cloudfront create-invalidation --distribution-id=${CF_DISTRIBUTION_ID} --paths "/*"

