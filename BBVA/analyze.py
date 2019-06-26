import pickle

import numpy as np

graph = pickle.load(open('../ER/graph_er.pickle', 'rb'))

latexString = """
\\begin{table}[htp]
    \\begin{tabular}{l|cccc}
    sector & size(\%)  & $k_{in}$ & $k_{out}$ & default ( \%) \\\\ \hline
"""

sector_stats = {}
total_nodes = graph.number_of_nodes()

for node_id, sector in graph.nodes('sector'):
    if sector not in sector_stats:
        sector_stats[sector] = {
            'nodes': [node_id],
            'out_conn': [len(graph[node_id])],
            'in_conn': [len(graph.in_edges(node_id))],
            'defaulted_probs': [graph.nodes[node_id]['defaulted']]
        }
    else:
        sector_stats[sector]['nodes'].append(node_id)
        sector_stats[sector]['out_conn'].append(len(graph[node_id]))
        sector_stats[sector]['in_conn'].append(len(graph.in_edges(node_id)))
        sector_stats[sector]['defaulted_probs'].append(graph.nodes[node_id]['defaulted'])

for sector, stats in sector_stats.items():
    stats['size'] = 100 * len(stats['nodes']) / total_nodes
    stats['in'] = np.mean(stats['in_conn'])
    stats['out'] = np.mean(stats['out_conn'])
    stats['default'] = 100 * np.sum(stats['defaulted_probs']) / len(stats['nodes'])
    latexString += "\n  %s & %.3f & %.3f & %.3f & %.3f \\\\" % (
    sector, stats['size'], stats['in'], stats['out'], stats['default'])
    del stats['nodes']
    del stats['in_conn']
    del stats['out_conn']
    del stats['defaulted_probs']

latexString += """
                \hline
    \end{tabular}
    \caption{Caption}
    \label{tab:my_label}
\end{table}
"""

print(latexString)
