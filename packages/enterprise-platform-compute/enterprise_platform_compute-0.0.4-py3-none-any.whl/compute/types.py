from enum import Enum


class Runners(Enum):
    ECS = "ECS"
    Lambda = "LAMBDA"
    LambdaFemm = "LAMBDA_FEMM"


class Events(str, Enum):
    GraphExecutionSubmitted = "COMPUTE_GRAPH_EXECUTION_SUBMITTED"
    GraphExecutionPrepared = "COMPUTE_GRAPH_EXECUTION_PREPARED"
    NodeExecutionSubmitted = "COMPUTE_NODE_EXECUTION_SUBMITTED"
    ExecutionSubmitted = "COMPUTE_EXECUTION_SUBMITTED"
    ExecutionCompleted = "COMPUTE_EXECUTION_SUCCEEDED"
    ExecutionFailed = "COMPUTE_EXECUTION_FAILED"
    NodeExecutionSucceeded = "COMPUTE_NODE_EXECUTION_SUCCEEDED"
    GraphExecutionSucceeded = "COMPUTE_GRAPH_EXECUTION_SUCCEEDED"
    GraphExecutionExited = "COMPUTE_GRAPH_EXECUTION_EXITED"
