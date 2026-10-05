APP_NAME := rag-app
IMAGE := rag-app:local
K8S_DIR := ./k8s

minikube-start:
	minikube start

minikube-docker-env:
	@echo "Run this in your shell: eval \$$(minikube -p minikube docker-env)"

docker-build:
	docker build -t $(IMAGE) .

secret-create:
	@test -n "$$OPENAI_API_KEY" || (echo "OPENAI_API_KEY not set"; exit 1)
	kubectl create secret generic openai-secrets \
		--from-literal=OPENAI_API_KEY=$$OPENAI_API_KEY \
		--dry-run=client -o yaml | kubectl apply -f -

apply:
	kubectl apply -f $(K8S_DIR)/app.yaml

ingress-enable:
	minikube addons enable ingress

ingress-apply:
	kubectl apply -f $(K8S_DIR)/ingress.yaml

service:
	minikube service $(APP_NAME)
