# optimize_over_tree
A mixed integer programming solution to the maximum phylogenetic diversity with cost constraints problem.
Requires the following packages: docopt, scikit-bio, and pulp

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

## Example
In the `example` subdir you will find a sample costs file (`example_costs.txt`) and a pruned phylogenetic tree that has the candidate cells (first column of costs file) as tips (`example_phylogenetic_placement_subtree.txt`). The third file (`chosen_samples.txt`) is the result of the following call:
```
python choose_optimal_leaves.py example/example_phylogenetic_placement_subtree.txt example/example_costs.txt 300 150 > example/chosen_samples.txt
```