# k8-volume-prototype

## Prerequisites

Create Azure Storage Account in the same region as the AKS cluster

Create the following File Shares

* input-share
* temp-share
* output-share

Create secret (https://github.com/kubernetes/examples/tree/master/staging/volumes/azure_file)

    kubectl create secret generic azure-secret --from-literal=azurestorageaccountname=szgteststorage --from-literal=azurestorageaccountkey=1+E15MnwPZfs6ZQoMsjugQf7bdEwY7rjxUR5FdIYmIfYRk0K8JkkoXu3knKVYdcKqn+4HpWCeoftPzvlPPeCaA==

## Build and deployment

See component descriptions

## Access UI

After deployment execute. The public IP is shown for each service (may take some time).

    kubectl get services



