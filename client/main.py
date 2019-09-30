from __future__ import print_function
import logging
import grpc
import service_pb2_grpc
import service_pb2

# Open communication chanel
channel = grpc.insecure_channel('localhost:4300')
stub = service_pb2_grpc.ComunicationServiceStub(channel)

# Capture values
print("Ingrese valor para variable 1")
vala = input()
print("Ingrese valor para variable 2")
valb = input()

# Send to the server
ra = stub.SendVar(service_pb2.VarRequest(varValue=vala))
print(ra)

rb = stub.SendVar(service_pb2.VarRequest(varValue=valb))
print(rb)

# Request Operation with de 2 variables
# service_pb2.OperationRequest.Operation.SUM
# service_pb2.OperationRequest.Operation.MULTY
rc = stub.Operation(service_pb2.OperationRequest(
    operation=service_pb2.OperationRequest.Operation.SUM))

# Print the result
print(rc)
