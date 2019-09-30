# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import service_pb2 as service__pb2


class ComunicationServiceStub(object):
  """Servicio gRPC, funciones servidas
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendVar = channel.unary_unary(
        '/ComunicationService/SendVar',
        request_serializer=service__pb2.VarRequest.SerializeToString,
        response_deserializer=service__pb2.VarResponse.FromString,
        )
    self.Operation = channel.unary_unary(
        '/ComunicationService/Operation',
        request_serializer=service__pb2.OperationRequest.SerializeToString,
        response_deserializer=service__pb2.OperationResult.FromString,
        )


class ComunicationServiceServicer(object):
  """Servicio gRPC, funciones servidas
  """

  def SendVar(self, request, context):
    """Instanciar variable
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Operation(self, request, context):
    """Realizar operacion
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ComunicationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendVar': grpc.unary_unary_rpc_method_handler(
          servicer.SendVar,
          request_deserializer=service__pb2.VarRequest.FromString,
          response_serializer=service__pb2.VarResponse.SerializeToString,
      ),
      'Operation': grpc.unary_unary_rpc_method_handler(
          servicer.Operation,
          request_deserializer=service__pb2.OperationRequest.FromString,
          response_serializer=service__pb2.OperationResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ComunicationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))