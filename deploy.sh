# Source constants
source ./constants.sh

gcloud functions deploy dec-agency-function \
    --gen2 \
    --set-env-vars TABLE_ID=$TABLE_ID \
    --region $REGION \
    --runtime python310 \
    --trigger-resource $BUCKET_NAME \
    --trigger-event google.cloud.storage.object.v1.finalized \
    --entry-point load_to_bigquery \
    --source .


