🚀 Project Overview:


This project demonstrates the process of provisioning a Kubernetes cluster, deploying a containerized application, exposing its metrics for monitoring, and setting up the groundwork for automated deployments and centralized logging.

1. Kubernetes Cluster Provisioning with Kubespray & Cilium

We've set up a robust 3-node Kubernetes cluster leveraging Kubespray for automated provisioning and Cilium as the CNI for advanced networking capabilities.

Guide: For detailed steps on cluster setup, refer to the ClusterProvisioning-KubeSpray-Guide document.

2. Flask Web Application Deployment
A sample Flask web application is containerized and deployed to the Kubernetes cluster. This application includes a health endpoint and exposes Prometheus metrics.

Application Details:

Location: The Flask application can be found in the flask-app/ directory.
Files: Contains app.py (Flask application), Dockerfile (for containerization), and requirements.txt (Python dependencies).
Documentation: Refer to the application documentation within the flask-app/ directory for more information.

Key Features:
REST Endpoint: /health returning {"status": "ok"}.

Prometheus Metrics: Exposes GET count for application-specific metrics.
Containerization: The application is containerized using Docker and pushed to a public registry (e.g., Docker Hub).

3. CI/CD Pipeline :

An initial CI/CD pipeline has been established, focusing on automating the build, push, and deployment process of the Flask application.

Documentation: See CI CD Documentation for an overview of the pipeline's design.
Configuration: The GitLab CI/CD YAML file outlines the stages for building the Docker image, pushing it to Docker Hub, and deploying to the Kubernetes cluster.

4. Monitoring & Logging

📊 Monitoring
Prometheus: Deployed within the cluster to collect and store application metrics.
Flask App Metrics: Successfully scraped metrics from the Flask application.
Provisioning: Refer to kube-prometheus-stack Provisioning Manual for Prometheus setup.
ServiceMonitor: See Flask-App-ServiceMonitor-Manifest for the manifest used to configure Prometheus to scrape the Flask app.


📝 Logging (Mandatory, Not Fully Delivered):

Filebeat: We are in the process of provisioning a Filebeat DaemonSet to collect and forward Flask App's logs.
Elasticsearch: Logs are intended to be forwarded to an Elasticsearch instance.
Provisioning: Refer to Provisioning Filebeat DaemonSet to collect and forward Flask App's Logs to ElasticSearch and ELasticSearch Provisioning Manual for details.
