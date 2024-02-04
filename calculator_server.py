from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc


class Calculator(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        a = request.a
        b = request.b
        sum_result = a + b
        return calculator_pb2.AddResponse(sum=sum_result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port("[::]:50051")
    print("Starting server. Listening on port 50051.")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
