# Docker for ML deployment

Playing around with Docker to package a simple predictive model for deployment.

The workflow is as follows:
- Create/import two separate training and inference routines:
	- `train.py` loads the training data, fits the model and serialises it in the image's local filesystem to be accessed later at inference time.
	- `inference.py` fetches new data, loads the deserialised model and outputs predictions.
- Write Dockerfile to configure all necessary setup. Notice that `train.py` is called from within the Dockerfile (i.e. we train at build-time, which is useful for debugging and version control).
- Build Docker image from Dockerfile: our trained model lives here.
- Run a container and launch `inference.py` from within it, where it has access to the pre-trained model and all necessary dependencies.

The great advantage for wanting to package our Python code like so lies in the fact that we can now embed it in new environments with great ease, e.g. we may
- load our Docker image on the cloud (e.g. AWS) for more computing power and scalability during training.
- deploy it as an application with API endpoints with Docker and Kubernetes.

This is based on a great tutorial at https://mlinproduction.com/docker-for-ml-part-3/.
