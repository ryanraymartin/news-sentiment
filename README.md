install terraform

sudo yum install -y yum-utils shadow-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install terraform

install git

sudo yum install git

install docker

sudo yum install docker
sudo service docker start
sudo docker run hello-world

install jq

sudo yum install jq

expand volumes on EBS with these steps:

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html

to login to the ECR regisitry use:

aws ecr get-login-password \
  --region $AWS_REGION | sudo docker login \
  --username AWS \
  --password-stdin $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/ray-demo

When running the terraform init you have to add -backend-config options for your credentials (aws keys). So your command should look like:

terraform init -backend-config="access_key=<your access key>" -backend-config="secret_key=<your secret key>"