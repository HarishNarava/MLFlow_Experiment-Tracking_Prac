import mlflow
print("Printing tacking URI scheme:")
print(mlflow.get_tracking_uri())
print('\n')

mlflow.set_tracking_uri("http://127.0.0.1:5000")
print("Printing new tracking URI Scheme:")
print(mlflow.get_tracking_uri())
print('\n')