'''
Picking a fixed size set of tree tips that maximizes total branch length,
while simultaneously staying under a provided cost budget

Usage:
choose_optimal_leaves.py <tree> <costs> <budget> <num_leaves_to_choose>

'''

from docopt import docopt
from pulp import *
from collections import defaultdict
from skbio import TreeNode


def convert_tree_to_bipartite(tree_file):
    tree = TreeNode.read(tree_file)
    tree.prune()
    tree.assign_ids()

    ancestors_dict = {tip.name: [node.id for node in tip.ancestors()] for tip in tree.tips() } # this might need checking
    edge_lengths = {node.parent.id: node.length for node in tree.traverse() if not node.is_root()}
    return {"tree": tree,
            "ancestors_dict": ancestors_dict,
            "edge_lengths": edge_lengths}


def solve_optimization(tree_file, num_leaves_requested, leaf_costs_file, budget):
    costs = defaultdict(float)
    with open(leaf_costs_file) as f:
        for line in f:
            tip_name, cost = line.strip().split(" ")
            costs[tip_name] = float(cost)
    tree_info = convert_tree_to_bipartite(tree_file)
    prob = LpProblem("Solving for maximal PD with " + str(num_leaves_requested) + " requested", LpMaximize)
    leaves_indicator = LpVariable.dicts("t",tree_info["ancestors_dict"].keys(),0,1,LpInteger)
    ancestors_indicator = LpVariable.dicts("n",tree_info["edge_lengths"].keys(),0,1,LpInteger)

    # The main objective is to maximize the sum of active edge lengths
    prob += lpSum([ancestors_indicator[node] * tree_info["edge_lengths"][node] for node in ancestors_indicator])

    # The total number of chosen items should be equal to the requested amount. Consider changing this to <=
    total_leaves = lpSum(leaves_indicator.values())
    prob += total_leaves == num_leaves_requested

    # The sum of the costs per tip should be under or equal to allotted budget
    costs_sum = lpSum([costs[tip] * leaves_indicator[tip] for tip in leaves_indicator])
    prob += costs_sum <= budget

    # If an ancestor node is active, it should have at least 1 corresponding tip active
    for tip in leaves_indicator:
        prob += leaves_indicator[tip] - lpSum([ancestors_indicator[ancestor] for ancestor in tree_info["ancestors_dict"][tip]]) >= 0

    status = prob.solve()
    #print(status)
    for k, v in leaves_indicator.items():
        if v.value() > 0:
            print(k)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    #print(arguments)
    solve_optimization(arguments["<tree>"],
                       int(arguments["<num_leaves_to_choose>"]),
                       arguments["<costs>"],
                       float(arguments["<budget>"]))