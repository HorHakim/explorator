import pandas

def prepare_data(edges_df):

	starting_nodes = edges_df[edges_df["type_aretes"] == "depart"]["noeud_amont"].values

	ending_nodes = edges_df[edges_df["type_aretes"] == "arrivee"]["noeud_aval"].values

	dict_upstream_downstream = {} # key : noeud_amont => value : noeud_aval
	for _, row in edges_df.iterrows():
		dict_upstream_downstream[row["noeud_amont"]] = row["noeud_aval"]

	# proposition alternative 1
	# dict_upstream_downstream = {row["noeud_amont"] : row["noeud_aval"] for _, row in edges_df.iterrows()} 


	# proposition alternative 2
	# for upstream_node, downstream_node in zip(edges_df["noeud_amont"].values, edges_df["noeud_aval"].values):
	# 	dict_upstream_downstream[upstream_node] = downstream_node

	return starting_nodes, ending_nodes, dict_upstream_downstream


def get_explorators_paths(starting_nodes, ending_nodes, dict_upstream_downstream):


	"""
	on loop sur starting node :
		# une itération consiste à reconstruire le chemain pris par 1 explorateur
		explorator_path = []
		Tant que le noeud en cours n'appartient pas à ending_nodes:
			je reccupère à l'aide dictionnaire le noeud aval du noeud en cours et je la rajoute à explorator_path
	"""


	for starting_node in starting_nodes:
		# une itération consiste à reconstruire le chemain pris par 1 explorateur	
		explorator_path = [starting_node]
		
		while explorator_path[-1] not in ending_nodes:
			downstream_node = dict_upstream_downstream[explorator_path[-1]]
			
			explorator_path.append(downstream_node)

		print(explorator_path)



if __name__ == "__main__":
	
	edges_df = pandas.read_csv("./parcours_explorateurs.csv")
	starting_nodes, ending_nodes, dict_upstream_downstream = prepare_data(edges_df)
	get_explorators_paths(starting_nodes, ending_nodes, dict_upstream_downstream)