from pulp import *
import numpy as np
from skbio import TreeNode

def convert_tree_to_bipartite(tree_file):
	tr = ete3.PhyloTree(newick=tree_file)

	return {"ancestor_mat":mat, "edge_lengths"}


def solve_optimization(tree_file, num_leaves_requested, leaf_costs):
	tree_as_mat = convert_tree_to_bipartite(tree_file)
	num_leaves = tree_as_mat.shape[1]
	num_ancestors = tree_as_mat.shape[0]
	prob = LpProblem("Solving for maximal PD with " + str(num_leaves_requested) + " requested",LpMaximize)
	leaves_indicator = [LpVariable("x{}".format(i+1), cat="Binary") for i in xrange(num_leaves)]
	ancestors_indicator = [LpVariable("y{}".format(i+1), cat="Binary") for i in xrange(num_ancestors)]
	total_leaves = sum(leaves_indicator)
	prob += total_leaves == num_leaves_requested

	for idx, leaf in enumerate(leaves_indicator):

def main():

