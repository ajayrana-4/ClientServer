# Build Images
cd server
docker build -t server:latest .
cd ../client
docker build -t client:latest .

# Deploy to Kubernetes
cd ../kubernetes
kubectl apply -f redis-pvc.yaml
kubectl apply -f redis-deployment.yaml
kubectl apply -f server-deployment.yaml
kubectl apply -f client-deployment.yaml

# Check deployment
kubectl get pods
kubectl get services

# Monitor logs
kubectl logs -l app=client -f

# Test fault tolerance
kubectl delete pod $(kubectl get pod -l app=server -o jsonpath='{.items[0].metadata.name}')
kubectl get pods -w

# Check data
kubectl exec -it $(kubectl get pod -l app=redis -o jsonpath='{.items[0].metadata.name}') -- redis-cli
# Inside Redis CLI:
KEYS *
GET key_name
SCAN 0

# Access API
kubectl port-forward service/server-service 5000:5000
curl http://localhost:5000/api/data/key_name

# Cleanup
kubectl delete -f redis-deployment.yaml
kubectl delete -f server-deployment.yaml
kubectl delete -f client-deployment.yaml
kubectl delete -f redis-pvc.yaml
