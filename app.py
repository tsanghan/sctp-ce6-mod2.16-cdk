#!/usr/bin/env python3
from aws_cdk import App, Stack, Environment, RemovalPolicy
import aws_cdk.aws_s3 as s3
from constructs import Construct
import os

class C6TsanghanPythonHelloCdkStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3.Bucket(self, "tsanghan-ce6-Python-CdkBucket", versioned=True, removal_policy=RemovalPolicy.DESTROY, auto_delete_objects=True)

app = App()
C6TsanghanPythonHelloCdkStack(app, "C6TsanghanPythonS3CdkStack",
                              description="tsanghan-ce6: This stack is synth by Python",
                              tags={"Name":"tsanghan-ce6"},
                              env=Environment(
                                  account=os.environ['AWS_ACCOUNT_ID'],
                                  region=os.environ['AWS_DEFAULT_REGION']
                                  )
                              )


# import os

# import aws_cdk as cdk

# from hello_cdk.hello_cdk_stack import HelloCdkStack


# app = cdk.App()
# HelloCdkStack(app, "HelloCdkStack",
#     # If you don't specify 'env', this stack will be environment-agnostic.
#     # Account/Region-dependent features and context lookups will not work,
#     # but a single synthesized template can be deployed anywhere.

#     # Uncomment the next line to specialize this stack for the AWS Account
#     # and Region that are implied by the current CLI configuration.

#     #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

#     # Uncomment the next line if you know exactly what Account and Region you
#     # want to deploy the stack to. */

#     #env=cdk.Environment(account='123456789012', region='us-east-1'),

#     # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
#     )

app.synth()
