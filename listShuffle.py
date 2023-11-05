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

from random import shuffle, seed
import argparse
import time
import sys

def ReorderList(myList):
    try:
        shuffle(myList)
    except:
        print("Error, can't reorder the input list: ", *myList)
    return myList

def GenerateSeed(actualSeed):
    seedUsed = actualSeed
    if (args.seed and args.seed > 0):
        seedUsed = args.seed
    seed(seedUsed)
    return seedUsed

def ProgramArguments():
    parser = argparse.ArgumentParser("randomShuffler", )
    parser.add_argument("input_list_file", help="A plain text file with a list of names in every line.", type=str)
    parser.add_argument("output_list_file", help="A plain text file with the same list of names randomly reordered.", type=str)
    parser.add_argument("-l", "--limit", help="Limit output to X number of lines. (Supply X value!)", type=int, required=False)
    parser.add_argument("-s", "--seed", help="Force a seed value for shuffling", type=float, required=False)
    return parser.parse_args()

args = ProgramArguments()
seedUsed = time.time()
try:
    inputFile =open(args.input_list_file, "r")
    lines = inputFile.readlines()
    seedUsed = GenerateSeed(seedUsed)
    reorderedLines = ReorderList(lines)
    if (args.limit):
        reorderedLines = reorderedLines[:args.limit]
    try:
        outputFile = open(args.output_list_file, "w")
        outputFile.writelines(reorderedLines)
        outputFile.close()
        inputFile.close()
        print("Done!")
        print("Seed used: ", seedUsed )
    except Exception as e:
        print("Error,({0}): {1}, can't open for writting the output file:".format(e.errno, e.strerror), args.output_list_file)
except Exception as e:
   print("Error,({0}): {1}, can't open input file:".format(e.errno, e.strerror), args.input_list_file)



