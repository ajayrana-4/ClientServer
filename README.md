# Client-Server Fault Tolerance Demo

This project demonstrates a fault-tolerant client-server architecture using Docker and Kubernetes. The system consists of a Python client sending data to a server, with Redis for data persistence. When pods crash or are deleted, Kubernetes automatically rebuilds them while maintaining data integrity.

# Project Structure

![image](https://github.com/user-attachments/assets/e34f3f91-4e3d-4410-9673-189ccbf05131)


# Prerequisites:

  Docker Desktop
  
  Kubernetes enabled in Docker Desktop
  
  kubectl command-line tool
  

# QUICK START

Build Docker Images:

# Build server image
  cd tela/server
  
  docker build -t server:latest . 

# Build client image
  cd ../client
  
  docker build -t client:latest . 

# Deploy to Kubernetes

  cd ../kubernetes

# Create Redis PVC and deploy Redis

  kubectl apply -f redis-pvc.yaml
  
  kubectl apply -f redis-deployment.yaml

# Deploy server and client

  kubectl apply -f server-deployment.yaml
  
  kubectl apply -f client-deployment.yaml

  

# Check running pods

kubectl get pods (Check running pods)

# Check services
kubectl get services  (Check services)


# Test Fault Tolerance

# List pods:
kubectl get pods (List pods)

# Delete a server pod to test auto-rebuild:
kubectl delete pod <server-pod-name> (Delete server pod to test auto-rebuild)

# Watch pods recreate
kubectl get pods 

# View Application Logs:

# View client logs
kubectl logs -l app=client -f 
# View server logs
kubectl logs -l app=server -f 

# Access Data

# Port forward server service
kubectl port-forward service/server-service 5000:5000 

# In another terminal, access the API
curl http://localhost:5000/api/data/<key> 

# Cleaning Up:

# Delete all deployments
kubectl delete -f redis-deployment.yaml

kubectl delete -f server-deployment.yaml

kubectl delete -f client-deployment.yaml

kubectl delete -f redis-pvc.yaml

# Conclusion

This project demonstrates a fault-tolerant client-server system using Docker, Kubernetes, and Redis. Key highlights include:

  Fault-Tolerant Architecture: Client and server interact seamlessly, with Redis ensuring data persistence, even during pod failures.
  
  Kubernetes Auto-Recovery: Kubernetes automatically re-deploys crashed or deleted pods, ensuring minimal downtime and high availability.
  
  Redis for Data Persistence: Redis ensures no data loss by storing data persistently, even if pods are recreated.
  
  Seamless Client-Server Interaction: Client continues to send requests while Kubernetes manages server pod recovery.
  
  Scalability and Fault Isolation: The system scales horizontally and isolates failures to individual components.
  
  Continuous Monitoring: Kubernetes allows real-time pod monitoring, log access, and easy troubleshooting.
  
  Testing: Fault tolerance was successfully tested by simulating pod failures, with Kubernetes automatically recovering services.
  
  Resource Management: Clean-up is easily managed with Kubernetes commands.
