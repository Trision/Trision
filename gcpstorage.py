from google.cloud import storage
#

class StorageGCP:
    
    def __init__(self):
        self.bucket_name = "resolve-contas-docs" #
        self.credentials = "mythical-runner-350501-79f85db1d3dd.json"
        self.client      = storage.Client.from_service_account_json(self.credentials)
        self.bucket      = self.client.bucket(self.bucket_name)
    
    
    def list(self, prefix):
        blobs_list = []
        blobs = self.client.list_blobs(self.bucket_name, prefix=prefix, delimiter='/')
        for blob in blobs:
            blobs_list.append(blob.name)
        return blobs_list
    
    
    def upload(self, source, destination):
        blob = self.bucket.blob(destination)
        blob.upload_from_filename(source)
        print(f"File {source} uploaded to gs://{self.bucket_name}/{destination}")
    
        
    def download(self, source, destination):
        blob = self.bucket.blob(source)
        blob.download_to_filename(destination)
        print(f"File gs://{self.bucket_name}/{source} downloaded to {destination}")
        