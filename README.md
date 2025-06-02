🚀 Kubernetes Cluster & App Deployment:


This repository details setting up a 3-node Kubernetes cluster, deploying a Flask application, and outlining initial steps for CI/CD, monitoring, and logging.

✨ Project Overview:


This project showcases the journey from provisioning a Kubernetes cluster to deploying a containerized application, exposing its metrics for robust monitoring, and laying the groundwork for automated deployments and centralized logging.

☁️ 1. Kubernetes Cluster with Kubespray & Cilium:


We've provisioned a resilient 3-node Kubernetes cluster using Kubespray for automated setup and Cilium as the CNI for advanced network policies and performance.

📚 Guide: Dive into the ClusterProvisioning-KubeSpray-Guide for a step-by-step walkthrough of the cluster setup.

🌐 2. Flask Web Application Deployment:


A demonstration Flask web application is containerized and deployed to the Kubernetes cluster. This app includes a standard health endpoint and exposes Prometheus metrics.

📁 Application Structure:

Location: Find the Flask application within the flask-app/ directory.
Contents: It includes app.py (the Flask app), Dockerfile (for containerization), and requirements.txt (Python dependencies).
Documentation: More details are available in the application documentation, also located in flask-app/.

💡 Key Features:

REST Endpoint: /health returns {"status": "ok"}.

Prometheus Metrics: Exposes GET count for specific application metrics.

📦 Containerization: The application is built into a Docker image and pushed to a public registry like Docker Hub.

🛠️ 3. CI/CD Pipeline :

An initial CI/CD pipeline is established, aiming to automate the build, push, and deployment phases of the Flask application.

📄 Documentation: Refer to CI CD Documentation for an overview of the pipeline's design.
⚙️ Configuration: The GitLab CI/CD YAML file details the stages for building the Docker image, pushing it to Docker Hub, and deploying to the Kubernetes cluster.

👀 4. Monitoring & Logging:


Comprehensive monitoring with Prometheus is active, scraping metrics from the deployed Flask application. The logging infrastructure is currently being set up.

📈 Monitoring

Prometheus: Deployed within the cluster to collect and store application metrics.
Flask App Metrics: Successfully configured to scrape metrics from the Flask application.

📚 Provisioning: Consult the kube-prometheus-stack Provisioning Manual for details on Prometheus setup.

🔗 ServiceMonitor: See Flask-App-ServiceMonitor-Manifest for the manifest used to configure Prometheus to scrape the Flask app.

📝 Logging (Mandatory, Not Fully Delivered):


Filebeat: We're in the process of provisioning a Filebeat DaemonSet to collect and forward the Flask App's logs.

Elasticsearch: Logs are designed to be sent to an Elasticsearch instance for centralized management.

📚 Provisioning: For setup details, refer to Provisioning Filebeat DaemonSet to collect and forward Flask App's Logs to ElasticSearch and the ELasticSearch Provisioning 
Manual.
