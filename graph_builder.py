import torch
from torch_geometric.data import Data

# 1. Define Tonnetz relationships (pitch class graph)
def tonnetz_edges():
    edges = []
    for pc in range(12):
        # Perfect fifth (+7), Major third (+4), Minor third (+3)
        connections = [(pc + i) % 12 for i in [3, 4, 7]]
        for neighbor in connections:
            edges.append((pc, neighbor))
            edges.append((neighbor, pc))
    return edges

# 2. Build Tonnetz graph based on notes in the piece
def build_tonnetz_graph(notes):
    pitch_classes_used = set(pitch % 12 for pitch, _ in notes)
    pc_list = sorted(pitch_classes_used)

    # Create node features: each node is a pitch class (0–11)
    # You could also count note frequency if you want richer features
    x = torch.eye(12)[pc_list]  # One-hot encode each pitch class used

    # Build edge index from Tonnetz relationships
    all_edges = tonnetz_edges()
    filtered_edges = [(a, b) for a, b in all_edges if a in pc_list and b in pc_list]

    if not filtered_edges:
        edge_index = torch.empty((2, 0), dtype=torch.long)
    else:
        edge_index = torch.tensor(filtered_edges, dtype=torch.long).t().contiguous()

    return Data(x=x, edge_index=edge_index)
