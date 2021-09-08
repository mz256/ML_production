# Docker for ML deployment

Playing around with Docker to package a simple predictive model for deployment.

The workflow is as follows:
- Create/import two separate training and inference routines:
	- `train.py` loads the training data, fits the model and serialises it in the image's local filesystem for future reference.
	- `inference.py` fetches new data, loads the deserialised model and outputs predictions.
- Write Dockerfile to configure all necessary setup. Notice that `train.py` is called from within the Dockerfile (i.e. we train at build-time, which is useful for debugging and version control).
- Build Docker image from Dockerfile: our trained model lives here.
- Run a container and launch `inference.py` from within it, where it has access to the pre-trained model and all necessary dependencies.