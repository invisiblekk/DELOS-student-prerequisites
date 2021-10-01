# DELOS student prerequisites

## NoSql

### Deployment

1.  `kubectl apply -f mongo-secret.yaml `
2.  `kubectl apply -f deployment-service.yaml`
3.  `kubectl apply -f pod.yaml`
4.  `kubectl logs mongodb-pod`

### Validation

1.  `kubectl exec -it mongodb-deployment-xxxxxxxxxx-xxxx /bin/sh`
2.  `mongo`
3.  `use admin`
4.  `db.auth("username", "password")`
5.  `use student`
6.  `db.student.find()`
