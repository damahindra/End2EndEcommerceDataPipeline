# import libraries
import streamlit as st
from google.cloud import storage

# instantiate Client
client = storage.Client.from_service_account_json(json_credentials_path='ecommerce-sales-data-pipeline-aa66d78b834c.json')
primary_bucket = 'bkt-event-data'

def validate_file(filename):
    return filename.endswith('.csv')

def upload_file_to_gcs(local_file) :
    # Creating bucket object
    bucket = client.get_bucket(primary_bucket)

    # Name of the object to be stored in the bucket
    object_name_in_gcs_bucket = bucket.blob(f'event-data.csv')

    # Name of the object in local file system
    object_name_in_gcs_bucket.upload_from_file(local_file)

# title
st.title('Event Data Uploader')
st.write('The uploaded csv file will be stored in GCS, preprocessed with Dataflow, moved to Bigquery, and visualized in Looker Studio')

# upload logic
uploaded_file = st.file_uploader("Choose a file")
if st.button("Upload File", type="primary"):
    if uploaded_file is not None:
        if validate_file(uploaded_file.name):
            with st.spinner("Uploading..."):
                upload_file_to_gcs(uploaded_file)
            st.success("File uploaded!")
        else :
            st.error("Wrong file format")

