from __future__ import print_function

import grpc
import cv2
import imageTest_pb2_grpc
import imageTest_pb2
import skvideo.io
import skvideo.datasets

FILE_URL = ""

def run():
    channel = grpc.insecure_channel('192.168.0.35:50051')
    stub = imageTest_pb2_grpc.ImageTestStub(channel)

    for response in stub.Analyse(generateRequests()):
        print(str(response.reply))

def generateRequests():
    # videogen = skvideo.io.vreader(FILE_URL)
    videogen = skvideo.io.vreader(skvideo.datasets.bigbuckbunny())

    for frame in videogen:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = bytes(frame)

        yield imageTest_pb2.MsgRequest(img=frame)

if __name__ == "__main__":
    run()