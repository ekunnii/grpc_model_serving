# Serve tensorflow model with gRPC.

This is the repo to demostrate how to serve machine learning models to clients with gRPC. 
The task is the classic mnist classification. 

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


