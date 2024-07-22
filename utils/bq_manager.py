from google.cloud import bigquery
import logging


# Set up BigQuery client
def load_data_to_bigquery(data, table_id: str) -> None:
    client = bigquery.Client()
    try:
        job_config = bigquery.LoadJobConfig(
            create_disposition=bigquery.CreateDisposition.CREATE_IF_NEEDED,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        )

        load_job = client.load_table_from_dataframe(
            data, destination=table_id, job_config=job_config
        )
        load_job.result()
        logging.info(f"Successfully loaded to bigquery")
        table = client.get_table(table_id)  # Make an API request.
        print(
            "Loaded {} rows and {} columns to {}".format(
                table.num_rows, len(table.schema), table_id
            )
        )
    except Exception as e:
        logging.error(f"Error {e} occurred while uploading to bigquery")
        raise e
