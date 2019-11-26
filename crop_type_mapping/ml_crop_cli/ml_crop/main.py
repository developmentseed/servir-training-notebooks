import sys
import argparse
import logging

from ml_crop.version import __version__
from ml_crop.utils_train import train
from ml_crop.utils_predict import predict

logger = logging.getLogger(__name__)


def parse_args(args):
    desc = 'ml_crop (v%s)' % __version__
    dhf = argparse.ArgumentDefaultsHelpFormatter
    parser0 = argparse.ArgumentParser(description=desc)

    pparser = argparse.ArgumentParser(add_help=False)
    pparser.add_argument('--version', help='Print version and exit', action='version', version=__version__)
    pparser.add_argument('--log', default=2, type=int,
                         help='0:all, 1:debug, 2:info, 3:warning, 4:error, 5:critical')

    subparsers = parser0.add_subparsers(dest='command')

    parser = subparsers.add_parser('train', parents=[pparser], help='train the model', formatter_class=dhf)
    parser.add_argument('-model', '--model_id', help='classifer model to apply, e.g. randomforest', default='randomforest', type=str, required=True)
    parser.add_argument('-tif', '--raster_file', help='path to the satellite image in raster', default='trans_nzoia.tif', type=str, required=True)
    parser.add_argument('-crop', '--train_geo', help='path to the crop type vector in geojson or shp', default='training_combined.geojson', type=str, required=True)
    parser.add_argument('-out', '--out_model', help='the train model output as pickle file', default="model.sav", type=str, required=True)

    parser = subparsers.add_parser('predict', parents=[pparser], help='used a pretrained model for prediction', formatter_class=dhf)
    parser.add_argument('-out', '--out_model', help='the train model output as pickle file', default="model.sav", type=str, required=True)
    parser.add_argument('-ntif', '--pred_tiff', help='path to the satellite image in raster', default='trans_nzoia.tif', type=str, required=True)
    parser.add_argument('-outimg', '--output_image', help='filename to save the output classification images', default='trans_nzoia.tif', type=str, required=True)
    parsed_args = vars(parser0.parse_args(args))

    return parsed_args


def main(cmd, **kwargs):
    if cmd == 'train':
        train(**kwargs)
    elif cmd == 'predict':
        predict(**kwargs)


def cli():
    args = parse_args(sys.argv[1:])
    logger.setLevel(args.pop('log') * 10)
    main(args.pop('command'), **args)


if __name__ == "__main__":
    cli()
