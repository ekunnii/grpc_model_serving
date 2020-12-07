# Serve model with gRPC.

This is the repo to demostrate how to serve machine learning models to clients with gRPC. 
The task is process the video with the opencv and return the processed frames to client. 
In the future I will add tensorflow model to do the style transfor or object detection for each frame.




### The benifits to serve the model with gRPC are listed as below:


- gRPC uses binary payloads, which are efficient to create and parse and hence light-weight.
- Bi-directional streaming is possible in gRPC, which is not the case with REST API
- gRPC API is built on top of HTTP/2 supporting the traditional request and response steaming as well as bi-directional streaming
10 times faster message transmission compared to REST API as gRPC uses serialized Protocol Buffers and HTTP/2
- Loose coupling between client and server makes it easy to make changes
- gRPC allows integration of API’s programmed in different languages


### The differences between gRPC and RESTful:

- Payload Format: REST uses JSON for exchanging messages between client and server, whereas gRPC uses Protocol Buffers. Protocol Buffers are compressed better than JSON, thus making gRPC transmit data over networks more efficiently.
- Transfer Protocols: REST heavily uses HTTP 1.1 protocol, which is textual, whereas gRPC is built on the new HTTP/2 binary protocol that compresses the header with efficient parsing and is much safer.
- Streaming vs. Request-Response: REST supports the Request-Response model available in HTTP1.1. gRPC uses bi-directional streaming capabilities available in HTTP/2, where the client and server send a sequence of messages to each other using a read-write stream.

## Running the code

First, we can build the docker image

```
docker build -f Dockerfile .
```

Second, launch the docker image

``` bash
docker run -it grpcmodelserving 
```
## Build from proto


If you would like to build the sw from the beginnning. First, generate the gRPC files with below command:

```
python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/imageTest.proto
```

Second step is to use the generated file to implement the service. the client stream the video file to the server. then the server process the frame with opencv and send back the processed frames using streaming. 

``` 
python imageTest_server.py & 
```

Start the client

```
python imageTest_client.py
```