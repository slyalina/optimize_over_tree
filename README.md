# optimize_over_tree
A mixed integer programming solution to the maximum phylogenetic diversity problem

## Invocation
```
Usage:
choose_optimal_leaves.py <tree> <costs> <budget> <num_leaves_to_choose> [-v -h -o]

Arguments:
<tree>                  Newick formatted tree that contains all the tips to be considered
<costs>                 Costs file with line of tip_name and cost separated by space
<budget>                Total sum of costs to stay under
<num_leaves_to_choose>  Number of active tips in final solution

Options:
-v --verbose            Verbose logging
-h --help               Help text
```
