# PROJECT ARCHITECTURE OVERVIEW
This project demonstrates a Production-Ready Ai Interence System built on Google Cloud Platform:
## Infrastructure Layer: Managed via Terraform (Infrastructure as Code) to provision a Google Kubernetes Engine (GKE) cluster
## Orchestration Layer: Kubernetes handles container lifecycle and resource management
## Serving Layer: Kserve & Knative provide "Serverless" capabilities, allowing the model to scale based on demand
## Networking Layer: Istio Service Mesh manages the Ingress Gateway and internal request routing

# DEPLOYMENT WORKFLOW
## 1. Containerization:
#### - Developed a Sentiment Analysis service using Python and HuggingFace Transformers.
#### - Packaged the application into a Docker image and pushed it to Google Artifact Registry
### 2. Infrastructure Provisioning:
#### - Executed Terraform scripts to automatically spin up the VPC network and a multi-node GKE cluster.
### 3. Platform Setup
#### - Install and configured the KServe stack (including Istio and Knative) to transform the standard Kubernetes cluster into an AI-specialized serving platform
### 4. Model Deployment
#### - Applied an InferenceService manifest to deploy the model.This step involved fine-tuning Resource Request & Limits to ensure the model coulf fit within the cluster's hardware constraints.
### 5. Validation & Inference
#### - Tested the end-to-end flow by sending REST API requests. Handled complex networking troubleshooting, including Firewall rudes and Port-forwading.

# DEMO GUIDE
## Step 1: Verify Infrastructure Health
Run: kubectl get pods
This confirm that the GKE nodes are healthy and the container image was successfully pulled from the registry
## Step 2: Check the Service Readness
Run: kubectl get infereneservice sentiment-model
The READY: True status indicated that the control plane has successfully reconciled the service and the internal URL is live.
## Step 3: Execute the Real-time inference
curl -X POST -H "Content-Type: application/json" \
  -d '{"text": "Everything is working perfectly!"}' \
  http://localhost:8888/predict

Sending a raw text string to API, validates the entire MLOps pipeline.