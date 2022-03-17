from diagrams import Cluster, Diagram
from diagrams.onprem.vcs import Github
from diagrams.onprem.ci import GithubActions
from diagrams.onprem.iac import Terraform
from diagrams.aws.network import VPC


with Diagram("AWS Infra Example", show=False):
    vcs = Github("github")
    ci  = GithubActions("github-actions")
    iac = Terraform("terraform")
    with Cluster("ca-central-1"):
        vpc = VPC("prod-vpc")

        vcs >> ci >> iac >> vpc