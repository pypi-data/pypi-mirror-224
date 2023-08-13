import numpy
import torch


def get_device():
    return "cuda" if torch.cuda.is_available() else "cpu"


def get_batch_quota():
    return numpy.inf


def main():
    print("hello world")
    get_device()
    get_batch_quota()


if __name__ == "__main__":
    main()
