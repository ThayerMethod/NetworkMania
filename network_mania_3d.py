import cudf
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import sys

def read_csv(file_path):
    """
    Reads the CSV file using cudf if available, falls back to pandas otherwise.
    """
    try:
        # Attempt to read using cudf (NVIDIA accelerated)
        df = cudf.read_csv(file_path)
        print("Loaded CSV using cudf.")
    except Exception as e:
        # Fallback to pandas if cudf isn't available
        print(f"cudf not available, defaulting to pandas. Error: {e}")
        df = pd.read_csv(file_path)
    return df

def analyze_data(df):
    """
    Perform advanced analysis with NetworkX based on ID and target columns,
    calculating multiple centrality measures to assess node importance.
    """
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['ID'], row['target'])

    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    
    # Calculate centrality measures
    centrality_measures = {
        "betweenness_centrality": nx.betweenness_centrality(G),
        "degree_centrality": nx.degree_centrality(G),
    }

    return G, centrality_measures

def visualize_graph_3d(G, centrality_measures):
    """
    Create a 3D interactive visualization using Plotly with node size and color
    based on centrality measures.
    """
    pos = nx.spring_layout(G, dim=3, seed=42)

    # Extract coordinates for each node
    x_nodes = [pos[node][0] for node in G.nodes()]
    y_nodes = [pos[node][1] for node in G.nodes()]
    z_nodes = [pos[node][2] for node in G.nodes()]

    # Centrality values
    node_size = [v * 100 for v in centrality_measures["degree_centrality"].values()]
    node_color = list(centrality_measures["betweenness_centrality"].values())

    # Create 3D scatter plot for nodes
    node_trace = go.Scatter3d(
        x=x_nodes,
        y=y_nodes,
        z=z_nodes,
        mode='markers',
        marker=dict(
            size=node_size,
            color=node_color,
            colorscale='Viridis',
            colorbar=dict(title="Betweenness Centrality"),
            line=dict(width=2)
        ),
        text=[f"Node {node}" for node in G.nodes()],
        hoverinfo='text'
    )

    # Create 3D lines for edges
    edge_trace = []
    for edge in G.edges():
        x0, y0, z0 = pos[edge[0]]
        x1, y1, z1 = pos[edge[1]]
        edge_trace.append(go.Scatter3d(
            x=[x0, x1, None],
            y=[y0, y1, None],
            z=[z0, z1, None],
            mode='lines',
            line=dict(color='black', width=1),
            hoverinfo='none'
        ))

    # Define layout
    layout = go.Layout(
        title="3D Network Visualization",
        scene=dict(
            xaxis=dict(title="X-axis"),
            yaxis=dict(title="Y-axis"),
            zaxis=dict(title="Z-axis")
        ),
        showlegend=False
    )

    fig = go.Figure(data=[node_trace] + edge_trace, layout=layout)
    fig.show()

def main(file_path):
    df = read_csv(file_path)
    G, centrality_measures = analyze_data(df)
    visualize_graph_3d(G, centrality_measures)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python network_mania_3d.py <csv_file_path>")
    else:
        main(sys.argv[1])
