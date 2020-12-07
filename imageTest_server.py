from concurrent import futures
import imageTest_pb2
import imageTest_pb2_grpc
import cv2
import time
import numpy as np
import grpc


def process_frame(frame, ops):
    return frame

class Greeter(imageTest_pb2_grpc.ImageTestServicer):
    def Analyse(self, request_iterator, context):
        bg_substractor = cv2.createBackgroundSubtractorMOG2()

        start = 0
        total_processed_frames = 0  

        for request in request_iterator:
            print("time diffrence = ", str(time.clock()-start))
            start = time.clock()

            frame = np.array(list(req.img))
            frame = frame.reshape((576,704))
            frame = np.array(frame, dtype=np.uint8)

            total_processed_frames += 1

            # place holder for frame processing function
            processed = process_frame(frame.shape[:2])

            cv2.imshow('Processed Image', processed)
            cv2.waitKey(1)
        yield imageTest_pb2.MsgReply(reply = total_processed_frames)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    imageTest_pb2_grpc.add_ImageTestServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(0)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()