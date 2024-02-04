import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    num1, num2 = 10, 20
    response = stub.Add(calculator_pb2.AddRequest(a=num1, b=num2))
    print("Sum = {}".format(response.sum))


if __name__ == "__main__":
    run()
