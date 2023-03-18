from weightedGrapgh import WeightedGraph
import pandas as pd

def read_file(file_name: str):
    df = pd.read_csv(file_name, ",") 
    df = df.fillna(value="-")
    num_discipline = df.shape[0]
    dependences = ""

    g1 = WeightedGraph(num_discipline + 2)
    for i in range(num_discipline):
        if df['Dependências'][i] != '-':
            dependences = df['Dependências'][i]
            if ';' in dependences:
                dependences = dependences.split(';')
                for j in dependences:
                    u = df.index[df['Código'] == j].tolist()
                    v = i 
                    g1.add_directed_edge(u[0], v, 1)
                    g1.add_directed_edge(v, num_discipline + 1, 1)
            else:
                u = df.index[df['Código'] == dependences].tolist()
                v = i
                g1.add_directed_edge(u[0], v, 1)
                g1.add_directed_edge(v, num_discipline + 1, 1)
        else:
            g1.add_directed_edge(num_discipline, i, 0)
            g1.add_directed_edge(i, num_discipline + 1, 1)


        
