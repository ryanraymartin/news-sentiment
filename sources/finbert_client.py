import requests
import os

print(
    requests.get(
        "https://ray-demo."+os.environ["TF_VAR_eks_cluster_domain"]+"/serve/finbert", params={"text": "Stocks rallied and the British pound gained."}
    ).json()
)