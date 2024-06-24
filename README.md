# End to End Ecommerce Analytics Data Pipeline

## Overview

This project is designed to automate the processing and visualization of e-commerce sales data. It provides an end-to-end data pipeline that allows users to seamlessly upload a CSV file containing sales data, which is then processed and moved to Google BigQuery via an automated Dataflow job orchestrated by Google Cloud Functions. Finally, the data stored in BigQuery is connected to a Looker Studio dashboard for dynamic visualization and analysis.

## Blueprint

![image](https://github.com/damahindra/End2EndEcommerceDataPipeline/assets/105963394/42c35905-0983-4aae-87f8-45a726a1cce4)

## Features

- **User-Friendly Interface:** Custom web interface for uploading CSV files.

- **Automated Data Processing:** Uses Google Cloud Functions to trigger an automated Dataflow job for transferring data to BigQuery.

- **Scalable Storage:** Leverages BigQuery for efficient and scalable storage of large datasets.

- **Dynamic Visualization:** Integrates with Looker Studio to provide interactive and customizable dashboards for data visualization.

## Architecture

- **CSV File Upload:** Users upload their e-commerce sales CSV files via a custom-built web interface that will transfer the file to Google Cloud Storage.

- **Cloud Function Trigger:** A Cloud Function is triggered upon file upload, initiating the data pipeline process.

- **Dataflow Job:** The Cloud Function starts a Dataflow job that reads the CSV file, processes the data, and loads it into BigQuery.

- **BigQuery Storage:** Processed data is stored in BigQuery, providing a scalable and efficient storage solution.

- **Looker Studio Dashboard:** Data in BigQuery is connected to Looker Studio, enabling users to create and customize dashboards for visual analysis.

## Technologies Used

- Google Cloud Platform (GCP):
  - Google Cloud Storage
  - Google Cloud Functions
  - Dataflow
  - BigQuery
  - Looker Studio: For data visualization.
  - Python: For scripting Cloud Functions and Dataflow jobs.
  - Javasciript: For building UDF function that supplies the logic to transform the lines of text.

## 1 Minute Demo

https://github.com/damahindra/End2EndEcommerceDataPipeline/assets/105963394/656033e2-c669-46ad-b3d7-dea2c8554fc3

