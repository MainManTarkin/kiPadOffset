import argparse



parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-o', '--offset', metavar='offset', type=float, required=True,
                    help='the offset between pads')
parser.add_argument('-n','--pads',  metavar='padding', type=int, required=True,
                    help='the number of pads to calculate offsets too')
parser.add_argument('-w', '--padWidth',  metavar='width', type=float, default=0.0,
                    help='the width of a pad. is used to calculate offset based on center of a pad')
parser.add_argument('-s', '--startingPoint',  metavar='start', type=float, default=0.0,
                    help='sets the start postion of the first pad: defualts to 0')
args = parser.parse_args()

offset=args.offset
paddingOffset=args.startingPoint
paddingWidth=args.padWidth
pads=args.pads

for i in range(0, pads):
    print("pad " + str((i+1)) + ": " + str(paddingOffset))
    paddingOffset+=(offset + paddingWidth)