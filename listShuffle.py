'''
Copyright 2023 Joaquín Cuéllar <joaquin(dot)cuellar(at)uco(dot)es>

This file is part of listShuffle.

listShuffle is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

listShuffle is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with listShuffle.  If not, see <https://www.gnu.org/licenses/>.
'''

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



