sync:
	aws s3 sync site/ s3://$(BUCKET_NAME)/site
