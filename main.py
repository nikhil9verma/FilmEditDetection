import argparse
from run import run

def main():
    parser = argparse.ArgumentParser(description='Film Edit Detection CLI tool')

    parser.add_argument('--vidpath', type=str, default='', help='What is the input video path?')
    parser.add_argument('--modpath', type=str, default='', help='What is the path of trained 3DCNN model')
    parser.add_argument('--operation', type=str, default='', help='What is the output content?(cuts, shots, mepformat)')

    args = parser.parse_args()

    print("Configuration")
    print("----------------------------------------------------------------------")
    print("Video Path : {}".format(args.vidpath))
    print("Model Path : {}".format(args.modpath))
    print("Operation : {}".format(args.operation))
    print("----------------------------------------------------------------------")

    if args.operation=='cuts':
        run().run(args.vidpath, args.modpath, iscsvframe=True)
    if args.operation=='shots':
        run().run(args.vidpath, args.modpath, iscsvtime=True)
    if args.operation=='mepformat':
        run().run(args.vidpath, args.modpath, ismepjson=True)


if __name__=='__main__':
    main()