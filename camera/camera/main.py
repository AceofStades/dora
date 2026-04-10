import cv2 as cv
import pyarrow as pa
from dora import Node


def main():
    """TODO: Add docstring."""
    node = Node()
    cap = cv.VideoCapture(0)
    while True:
        (frame, ret) = cap.read()

        node.send_output(
            output_id="cam",
            data=frame,
            metadata={},
        )


if __name__ == "__main__":
    main()
