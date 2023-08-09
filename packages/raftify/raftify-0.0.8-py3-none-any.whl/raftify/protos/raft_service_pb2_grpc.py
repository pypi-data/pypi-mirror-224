# type: ignore
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import eraftpb_pb2 as eraftpb__pb2
from . import raft_service_pb2 as raft__service__pb2


class RaftServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RequestId = channel.unary_unary(
            "/raftservice.RaftService/RequestId",
            request_serializer=raft__service__pb2.IdRequestArgs.SerializeToString,
            response_deserializer=raft__service__pb2.IdRequestResponse.FromString,
        )
        self.ChangeConfig = channel.unary_unary(
            "/raftservice.RaftService/ChangeConfig",
            request_serializer=eraftpb__pb2.ConfChange.SerializeToString,
            response_deserializer=raft__service__pb2.ChangeConfigResponse.FromString,
        )
        self.SendMessage = channel.unary_unary(
            "/raftservice.RaftService/SendMessage",
            request_serializer=eraftpb__pb2.Message.SerializeToString,
            response_deserializer=raft__service__pb2.RaftMessageResponse.FromString,
        )
        self.RerouteMessage = channel.unary_unary(
            "/raftservice.RaftService/RerouteMessage",
            request_serializer=raft__service__pb2.RerouteMessageArgs.SerializeToString,
            response_deserializer=raft__service__pb2.RaftMessageResponse.FromString,
        )


class RaftServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RequestId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ChangeConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def RerouteMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RaftServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "RequestId": grpc.unary_unary_rpc_method_handler(
            servicer.RequestId,
            request_deserializer=raft__service__pb2.IdRequestArgs.FromString,
            response_serializer=raft__service__pb2.IdRequestResponse.SerializeToString,
        ),
        "ChangeConfig": grpc.unary_unary_rpc_method_handler(
            servicer.ChangeConfig,
            request_deserializer=eraftpb__pb2.ConfChange.FromString,
            response_serializer=raft__service__pb2.ChangeConfigResponse.SerializeToString,
        ),
        "SendMessage": grpc.unary_unary_rpc_method_handler(
            servicer.SendMessage,
            request_deserializer=eraftpb__pb2.Message.FromString,
            response_serializer=raft__service__pb2.RaftMessageResponse.SerializeToString,
        ),
        "RerouteMessage": grpc.unary_unary_rpc_method_handler(
            servicer.RerouteMessage,
            request_deserializer=raft__service__pb2.RerouteMessageArgs.FromString,
            response_serializer=raft__service__pb2.RaftMessageResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "raftservice.RaftService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class RaftService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RequestId(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/raftservice.RaftService/RequestId",
            raft__service__pb2.IdRequestArgs.SerializeToString,
            raft__service__pb2.IdRequestResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ChangeConfig(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/raftservice.RaftService/ChangeConfig",
            eraftpb__pb2.ConfChange.SerializeToString,
            raft__service__pb2.ChangeConfigResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SendMessage(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/raftservice.RaftService/SendMessage",
            eraftpb__pb2.Message.SerializeToString,
            raft__service__pb2.RaftMessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def RerouteMessage(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/raftservice.RaftService/RerouteMessage",
            raft__service__pb2.RerouteMessageArgs.SerializeToString,
            raft__service__pb2.RaftMessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
