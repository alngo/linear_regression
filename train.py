import argparse
from libml.trainer import Trainer


def arguments():
    parser = argparse.ArgumentParser(
        description='Train a model given a dataset')

    parser.add_argument('--path', dest="path", metavar='path',
                        help='must be a valid dataset path')
    parser.add_argument('--out', dest="out", metavar='path',
                        help='must be a valid output path')
    parser.add_argument('--plot', dest="plot", default=False, type=bool,
                        help='plot training')
    parser.add_argument('--verbose', dest="verbose", default=False, type=bool,
                        help='verbose')
    parser.add_argument('--epochs', dest="epochs", type=int,
                        help='number of iteration')
    parser.add_argument('--lrate', dest="lrate", type=int,
                        help='number of iteration')
    args = parser.parse_args()
    return args


def train():
    path = "./datasets/data.csv"
    out = "./models/model.csv"
    plot = False
    verbose = False
    lrate = 0.0001
    epochs = 1000
    args = arguments()

    if args.path is not None:
        path = args.path
    if args.out is not None:
        out = args.out
    if args.plot is not False:
        plot = True
    if args.verbose is not False:
        verbose = True
    if args.lrate is not None:
        lrate = args.lrate
    if args.epochs is not None:
        epochs = args.epochs

    train = Trainer(data_path=path, out_path=out, epochs=epochs, lrate=lrate,
                    verbose=verbose, plot=plot)

    train.gradient_descent()


if __name__ == "__main__":
    train()
