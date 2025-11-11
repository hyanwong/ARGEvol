import sys
import numpy as np
from IPython.display import HTML


### Hack below - can be removed when questions are saved to JSON files named Q1.json, Q2.json etc
# This allows answers to be hidden from the casual viewer. Then we can simply set the url to a string instead of a class
class FakeURL(dict):
    def __add__(self, prefix):
        return self[prefix]
WB1_base = FakeURL()
true, false= True, False  # just to allow easy conversion to JSON format
### hack ends

WB1_base["Q1.json"] = [{
    "question": "What genomic span is passed on to sample node 6 through the route via node 15? The span is the total length of the genome region passed on (i.e. the right minus the left position)",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 930, "correct": true, "feedback": "Yes, it covers positions 0 to 930."},
        {"type": "default", "feedback": "Try hovering over the edges below node 15."}
    ]
}]
WB1_base["Q2.json"] = [{
    "question": "What does SPR stand for?",
    "type": "many_choice",
    "answers": [
        {"answer": "Subtree Prune and Regraft", "correct": true},
        {"answer": "Strand Pairing Resolution", "correct": false},
        {"answer": "Single-Point Reversion", "correct": false},
        {"answer": "Slippery Puzzle Reorganization", "correct": false, "feedback": "???."}
    ]}, {
    "question": "What is the TMRCA, or time to the most recent common ancestor (in generations) between nodes 0 and 9 at the left hand end of this ARG?",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 38472, "correct": true},
        {"type": "value", "value": 31, "correct": false, "feedback": "That's the node ID. What time is associated with that node."},
        {"type": "default", "feedback": "Try hovering over the last part of the genome, and looking at the axis labels."}
    ]},{
    "question": "What is the name of the structure in which two lineages split but immediately re-join, as seen just below node 26",
    "type": "many_choice",
    "answers": [
        {"answer": "Diamond", "correct": true},
        {"answer": "Loop", "correct": false},
        {"answer": "Bubble", "correct": false, "feedback": "This term is sometimes used, but is not standard"},
        {"answer": "Cycle", "correct": false}
    ]
}]

WB1_base["Q3.json"] = [{
    "question": "(Hard!) Only one recombination event results in a tree that shows a new topological relationship between the samples. By looking at the graph and the local trees, can you identify which one it is? Enter its breakpoint position below:",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 930, "correct": true, "feedback": "Yes (coincidentally this is the last breakpoint)"},
        {"type": "default", "feedback": "Hint: look at the breakpoints on the X axis of the tree-by-tree plot: which marks the transition between two differently shaped trees?"}
    ]
}]

WB1_base["Q4.json"] = [{
    "question": "The first two breakpoints along the genome happen to correspond to recombination at the top of the ARG. How many different root heights does this cause?",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 3, "correct": true},
        {"type": "default", "feedback": "Hint: look at the local trees"}
    ]
}]

WB1_base["Q5.json"] = [{
    "question": "How would you classify the recombination node(s) 20/21",
    "type": "many_choice",
    "answers": [
        {"answer": "Non-coalescent / always unary", "correct": true, "feedback": "By construction, in a full ARG recombination nodes are never coalescent"},
        {"answer": "Partially-coalescent / locally unary", "correct": false},
        {"answer": "All-coalescent / never unary", "correct": false}
    ]},{
    "question": "How would you classify node 17",
    "type": "many_choice",
    "answers": [
        {"answer": "Non-coalescent / always unary", "correct": false},
        {"answer": "Part-coalescent / locally unary", "correct": false},
        {"answer": "All-coalescent / never unary", "correct": true}
    ]},{
    "question": "How would you classify node 26",
    "type": "many_choice",
    "answers": [
        {"answer": "Non-coalescent / always unary", "correct": true, "feedback": "Some 'common ancestor' nodes with 2 children in the full ARG never represent local coalescence"},
        {"answer": "Part-coalescent / locally unary", "correct": false},
        {"answer": "All-coalescent / never unary", "correct": false}
    ]},{
    "question": "How would you classify node 15",
    "type": "many_choice",
    "answers": [
        {"answer": "Non-coalescent / always unary", "correct": false},
        {"answer": "Part-coalescent / locally unary", "correct": true, "feedback": "It is only coalescent on the left side of the genome: it is unary to the right of position 930"},
        {"answer": "All-coalescent / never unary", "correct": false}
    ]
}]


WB1_base["Q6.json"] = [{
    "question": "In the population-coloured ARG plot, what colour do you think represents nodes from the African population",
    "type": "many_choice",
    "answers": [
        {"answer": "green", "correct": true, "feedback": "Yes, the deepest divergences are African: in fact, even between the European genomes, some coalescences trace back into Africa"},
        {"answer": "blue", "correct": false},
    ]
}]

WB1_base["Q7.json"] = [{
    "question": "One of the sites has two mutations. Can you identify the position of that site by looking at both the tree-by-tree and the interactive ARG plot?",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 5, "correct": true, "feedback": "Yes (coincidentally this is the first position)"},
        {"type": "default", "feedback": "Hint: duplicate mutations will simultaneously be highlighted when hovering over them in the visualizer"}
    ]
}]

WB1_base["Q8.json"] = [{
    "question": "What is the allelic state of the sample with node ID 2 at position 5?",
    "type": "many_choice",
    "answers": [
        {"answer": "A", "correct": false},
        {"answer": "C", "correct": false},
        {"answer": "G", "correct": false},
        {"answer": "T", "correct": true}
    ]}, {
    "question": "What is the ancestral state at position 5?",
    "type": "many_choice",
    "answers": [
        {"answer": "A", "correct": true},
        {"answer": "C", "correct": false},
        {"answer": "G", "correct": false},
        {"answer": "T", "correct": false}
    ]}, {
    "question": "By looking at the ARG or tree visualizations, the mutation responsible for this state in sample 2 is above which node?",
    "type": "many_choice",
    "answers": [
        {"answer": "12", "correct": false},
        {"answer": "13", "correct": true},
        {"answer": "31", "correct": false},
        {"answer": "This allelic state is the ancestral state, so does not correspond to a mutation in the ARG ", "correct": false,
        "feedback": "It is true that ancestral states are not represented by a mutation in the ARG, but the state C here is a derived state, so it *is* associated with a mutation"}
    ]
}]

WB1_base["Q9.json"] = [{
    "question": "In the ARG above, what mutation groups together samples 7, 8, and 9?",
    "type": "many_choice",
    "answers": [
        {"answer": "C mutates to T at position 215", "correct": true},
        {"answer": "T mutates to C at position 215", "correct": false, "feedback": "You have the position right, but the derived state is T."},
        {"answer": "G mutates to T at position 92", "correct": false},
        {"answer": "C mutates to G at position 560", "correct": false}
    ]}, {
    "question": "What ARG node does that mutation allow us to infer?",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 16, "correct": true, "feedback": "Yes, it's the node below the mutation."},
        {"type": "value", "value": 19, "correct": false, "feedback": "No, that node groups together more than 7, 8, and 9."}
    ]},{
    "question": "Do any mutations allow us to resolve the relationship between samples 4, 5, and 6?",
    "type": "many_choice",
    "answers": [
        {"answer": "No", "correct": true, "feedback": "In fact, we can't even resolve the relative closeness of 4 versus 5 versus 6 to the (7,8,9) group"},
        {"answer": "Yes", "correct": false}
    ]}, {
    "question": "How many mutations are uninformative about the structure (topology) of the ARG?",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 2, "correct": true, "feedback": "Yes, the two so-called singletons, immediately above node 3 and node 4."},
        {"type": "default", "feedback": "Incorrect (hint: mutations above a single node do not group samples together)."}
    ]
}]

WB1_base["Q10.json"] = [{
    "question": "What is the interpretation of the genetic diversity, π in terms of branch lengths?",
    "type": "many_choice",
    "answers": [
        {"answer": "The average time of all internal nodes", "correct": false},
        {"answer": "Twice the average TMRCA between all pairs of samples", "correct": true},
        {"answer": "The average branch lengths between all pairs of samples", "correct": true},
        {"answer": "The span-weighted average branch length of the local trees", "correct": false,
        "feedback": "This is the equivalent of the number of segregating sites (under the infinite-sites model)"}
    ]
}]

class Workbook:
    @staticmethod
    def setup():
        display(HTML(
            "<style type='text/css'>" +
            ".exercise {background-color: yellow; color: black; font-family: 'serif'; font-size: 1.2em}" +
            ".exercise code {font-size: 0.7em}" +
            "</style>" + 
            "<h4>✅ Your notebook is ready to go!</h4>" +
            ("" if "pyodide" not in sys.modules else '''
To clear the notebook and reset,
select "Clear Browser Data" from the JupyterLite help menu.
''')
    ))

    def node_coalescence_status(arg):
        """
        Uses the num_children_array attribute to find nodes that represent local coalescence.
        See https://tskit.dev/tskit/docs/latest/python-api.html#tskit.Tree.num_children_array
        Returns an array of length num_nodes containing 0 if a node never has any coalescent
        segments, 1 if some segments of the node are coalescent and some unary, and 2 if
        all node segments represent a local coalescence point.
        """
        has_unary = np.zeros(arg.num_nodes + 1, dtype=int)
        has_coal = np.zeros(arg.num_nodes + 1, dtype=int)
        for tree in arg.trees():
            has_unary[tree.num_children_array == 1] = 1
            has_coal[tree.num_children_array > 1] = 1
        status = np.where(has_coal, np.where(has_unary, 1, 2), 0)
        return status[:-1] # remove the last array value, which is the "virtual root": see docs


class Workbook1(Workbook):
    url = WB1_base  # Put the real URL base string (ending in "/") here, once JSON question files have been made available at that URL
