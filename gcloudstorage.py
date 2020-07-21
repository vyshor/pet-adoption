from google.cloud import storage

BUCKET_NAME = 'summer20-sps-42.appspot.com'
storage_client = storage.Client.from_service_account_json('servicekey.json')


def upload_blob(source_file_name, destination_blob_name, content_type="application/octet-stream", bucket_name=BUCKET_NAME):
    """Uploads a file to the bucket."""
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(source_file_name, content_type=content_type)
    blob.make_public()

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))
    return blob.public_url


