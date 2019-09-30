from concurrent import futures

import logging
import grpc

import service_pb2
import service_pb2_grpc

# Override ComunicationServer default proto class
class ComunicationServer(service_pb2_grpc.ComunicationServiceServicer):

  # Almacenar las variables enviadas por el cliente
  variables = []

  # Message SendVar, Recibe la variable y la almacena en la clase
  def SendVar(self, request, context):
    self.variables.append(request.varValue)
    return service_pb2.VarResponse(reply=("Your var is: "+self.variables[-1]))

  # Message Operation, Recibe la opreacion a realizar
  # Realiza la operacion con los ultimas dos variables amacenadas
  def Operation(self, request, context):
    op = float(self.variables[-1]) + float(self.variables[-2])
    return service_pb2.OperationResult(result=("Your res is: %f " % op))


# Prepare the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ComunicationServiceServicer_to_server(
        ComunicationServer(), server)
    server.add_insecure_port('0.0.0.0:4300')
    server.start()
    server.wait_for_termination()

# Run server
if __name__ == '__main__':
    logging.basicConfig()
    serve()
