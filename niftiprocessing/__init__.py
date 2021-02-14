import argparse


def parsercli():
    parser = argparse.ArgumentParser(prog='ExamplePackage')

    parser.add_argument('integer', type=int, help='Integer to square')
    parser.add_argument('--power', '-p', type=int, help='Integer to nth power')

    args = parser.parse_args()

    if args.power:
        print(args.integer**args.power)
    else:
        print(args.integer**2)



def main():
    parsercli()
