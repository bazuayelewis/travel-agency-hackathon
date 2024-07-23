gcloud functions deploy dec-agency-function \
    --gen2 \
    --region europe-west1 \
    --runtime python310 \
    --trigger-resource dec-travel-agency \
    --trigger-event google.cloud.storage.object.v1.finalized \
    --entry-point load_to_bigquery \
    --source .


