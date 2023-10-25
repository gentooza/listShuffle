from random import shuffle
import argparse

def ReorderList(myList):
    try:
        shuffle(myList)
    except:
        print("Error, can't reorder the input list: ", *myList)
    return myList


parser = argparse.ArgumentParser("randomShuffler", )
parser.add_argument("input_list_file", help="A plain text file with a list of names in every line.", type=str)
parser.add_argument("output_list_file", help="A plain text file with the same list of names randomly reordered.", type=str)
parser.add_argument("limit", help="Limit output to X number of lines.", type=int, required=False)
args = parser.parse_args()

try:
    inputFile =open(args.input_list_file, "r")
    lines = inputFile.readlines()
    reorderedLines = ReorderList(lines)
    try:
        outputFile = open(args.output_list_file, "w")
        outputFile.writelines(reorderedLines)
        outputFile.close()
        inputFile.close()
        print("Done!")
    except:
        print("Error, can't open for writting the output file:", args.output_list_file)
except:
    print("Error, can't open input file:", args.input_list_file)



