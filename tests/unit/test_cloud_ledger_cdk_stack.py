import aws_cdk as core
import aws_cdk.assertions as assertions

from cloud_ledger_cdk.cloud_ledger_cdk_stack import CloudLedgerCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cloud_ledger_cdk/cloud_ledger_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CloudLedgerCdkStack(app, "cloud-ledger-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
