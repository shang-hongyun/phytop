import sys,os
import copy
import argparse
import shutil
import json
import math
import multiprocessing
from collections import OrderedDict, Counter
from .Astral import AstralTree
from .RunCmdsMP import logger
from .small_tools import mkdirs
from .__version__ import version


bindir = os.path.dirname(os.path.realpath(__file__))

def makeArgparse():
	parser = argparse.ArgumentParser( 
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description='Visualizing ILS/HI signals on species tree from ASTRAL.',
		)
	# input
	parser.add_argument("astral", metavar='NEWICK',
					help="Species tree output by ASTRAL (`-u 2` for C++ versions and `-t 2` for JAVA versions) [required]")
	parser.add_argument('-alter', default=None, type=str, dest='show',  metavar='FILE',
                    help="Show the tree instead of the ASTRAL tree (their topologies MUST be identical) [default=%(default)s]")

	parser.add_argument('-collapse', default=None, type=str, dest='collapsed',  metavar='FILE',
					help="Collapse leaves as specified in the file [default=%(default)s]")
	parser.add_argument('-subset', default=None, type=str, nargs='+', dest='subset',  metavar='TAXON',
                    help="Show a subset clade [default=%(default)s]")

	# output
	parser.add_argument('-pre', '-prefix', default=None, type=str, dest='prefix', metavar='STR',
					help="Prefix for output [default=%(default)s]")
	parser.add_argument('-tmp', '-tmpdir', default='tmp', dest='tmpdir', type=str, metavar='DIR',
					help="Temporary directory [default=%(default)s]")
	parser.add_argument('-sort', action="store_true", default=False, 
                    help="Sort q1, q2 and q3 [default=%(default)s]")
	parser.add_argument('-notext', action="store_true", default=False, 
                    help="Do not draw text on the barcharts [default=%(default)s]")

	args = parser.parse_args()
	return args

def plot(**kargs):
	mkdirs(kargs['tmpdir'])
	AstralTree(**kargs).process_quartet()
def main():
	args = makeArgparse()
	logger.info('Command: {}'.format(' '.join(sys.argv)))
	logger.info('Version: {}'.format(version))
	logger.info('Arguments: {}'.format(args.__dict__))
	pipeline = plot(**args.__dict__)

if __name__ == '__main__':
	main()
