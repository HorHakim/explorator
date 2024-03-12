import pandas

edges_df = pandas.read_csv("./parcours_explorateurs.csv")


starting_nodes = edges_df[edges_df["type_aretes"] == "depart"]["noeud_amont"].values

ending_nodes = edges_df[edges_df["type_aretes"] == "arrivee"]["noeud_aval"].values

dict_amont_aval = {} # key : noeud_amont => value : noeud_aval
for _, row in edges_df.iterrows():
	dict_amont_aval[row["noeud_amont"]] = row["noeud_aval"]

# proposition alternative 1
# dict_amont_aval = {row["noeud_amont"] : row["noeud_aval"] for _, row in edges_df.iterrows()} 


# proposition alternative 2
# for upstream_node, downstream_node in zip(edges_df["noeud_amont"].values, edges_df["noeud_aval"].values):
# 	dict_amont_aval[upstream_node] = downstream_node
