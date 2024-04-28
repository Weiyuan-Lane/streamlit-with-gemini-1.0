# streamlit-with-gemini

This codebase is adapted from the Cloud Skills Boost Lab ["Develop an App with Vertex AI Gemini 1.0 Pro"](https://www.cloudskillsboost.google/paths/19/course_templates/980/labs/468844)

Follow these instructions to run it in your own project or deploy it to Cloud Run!

### Warning!

Running this codebase, whether local or deployed, will consume cloud credits as Vertex AI is used (for Gemini prompts)!
If your intention is to test it at no cost, do ensure that you have free Google Cloud credits before running it.

## Development

#### Follow the following steps to setup:

1. Launch Cloud Shell from [this link](https://shell.cloud.google.com/)

2. Run the following command with the intended "PROJECT_ID" that you are developing this project from:
```
gcloud config set project %PROJECT_ID%
```

3. Clone the repository with the following command
```
git clone https://github.com/Weiyuan-Lane/streamlit-with-gemini-1.0.git
```

4. Change the directory to the recently cloned repository
```
cd ~/streamlit-with-gemini-1.0
```

5. Create a python cirtual environment
```
python3 -m venv gemini-streamlit
```

6. Install the required python packages
```
pip install -r requirements.txt
```

7. Enable APIs needed for Vertex AI and Cloud Run
```
gcloud services enable cloudbuild.googleapis.com cloudfunctions.googleapis.com run.googleapis.com logging.googleapis.com storage-component.googleapis.com aiplatform.googleapis.com
```

#### Follow the following steps to develop in the cloud shell:

1. (If you didn't do it above) Launch Cloud Shell from [this link](https://shell.cloud.google.com/)

2. (If you didn't do it above) Run the following command with the intended "PROJECT_ID" that you are developing this project from:
```
gcloud config set project %PROJECT_ID%
```

3. Change the directory to the cloned repository
```
cd ~/streamlit-with-gemini-1.0
```

4. Init the virtual environment
```
source gemini-streamlit/bin/activate
```

5. Run the local server in the cloud shell's localhost:
```
PROJECT_ID=%YOUR_PROJECT_ID% LOCATION=us-west4 streamlit run app.py \
  --browser.serverAddress=localhost \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false \
  --server.port 8080
```

## Deployment

1. Setup your environment variables (change the values below as you intend)
```
SERVICE_NAME='streamlit-with-gemini'
IMAGE_REPO='streamlit-with-gemini'
PROJECT_ID='%YOUR_PROJECT_ID%'
REGION='%INTENDED_GCP_REGION%'
```

2. (Only for first time) Setup artifact registry for storing your docker images
```
gcloud artifacts repositories create "$IMAGE_REPO" --location="$REGION" --repository-format=Docker
gcloud auth configure-docker "$REGION-docker.pkg.dev"
```

3. Use Cloud Build to build a new docker image for running this application
```
gcloud builds submit --tag "$REGION-docker.pkg.dev/$PROJECT_ID/$IMAGE_REPO/$SERVICE_NAME"
```

4. Deploy to Cloud Run
```
gcloud run deploy "$SERVICE_NAME" \
  --port=8080 \
  --image="$REGION-docker.pkg.dev/$PROJECT_ID/$IMAGE_REPO/$SERVICE_NAME" \
  --allow-unauthenticated \
  --region=$REGION \
  --platform=managed  \
  --project=$PROJECT_ID \
  --set-env-vars=PROJECT_ID=$PROJECT_ID,REGION=$REGION
```

5. Once the deployment is done, check your available Cloud Run applications from [here](https://console.cloud.google.com/run) and make sure that your application is working.
