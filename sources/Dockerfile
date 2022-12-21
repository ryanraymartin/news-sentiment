FROM rayproject/ray:latest

RUN sudo yum update -y && \
    sudo pip install torch torchvision transformers pandas datasets accelerate \
        scikit-learn mlflow tensorboard s3fs ray[all]==2.0.0rc0 boto3

COPY *.py /opt/