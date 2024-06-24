from googleapiclient.discovery import build

def trigger_job(cloud_event, environment) :
  service = build('dataflow', 'v1b3')
  project = 'ecommerce-sales-data-pipeline'

  template_path = 'gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery'

  template_body = {
    "jobName" : "gcs-to-bq-sales-data",
    "parameters": {
        "inputFilePattern": "gs://bkt-ecommerce-sales-data/ecommerce-sales-data.csv",
        "JSONPath": "gs://bkt-ecommerce-sales-metadata/ecommerce_schema.json",
        "outputTable": "ecommerce-sales-data-pipeline:ecommerce_sales_data.sales",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt-ecommerce-sales-metadata",
        "javascriptTextTransformGcsPath": "gs://bkt-ecommerce-sales-metadata/ecommerce-sales-data-udf.js",
        "javascriptTextTransformFunctionName": "transform"
    }
  }

  request = service.projects().templates().launch(projectId=project, gcsPath=template_path, body=template_body)
  response = request.execute()
  print(response)

