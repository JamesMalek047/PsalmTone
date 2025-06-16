from music_parser import parse_music
from graph_builder import build_graph

def main():
    notes = parse_music("example.musicxml")  # Replace with your real file
    graph = build_graph(notes)
    print("Node features (x):\n", graph.x)
    print("Edge index:\n", graph.edge_index)

if __name__ == "__main__":
    main()
