# NetworkMania: Advanced Network Analysis with NVIDIA Acceleration

NetworkMania is a Python-based project designed for advanced analysis of a CSV file containing network data. Given a CSV file with columns `ID` and `target`, NetworkMania constructs a directed graph and evaluates node importance based on various centrality measures. The project leverages NVIDIA CUDA (when available) for accelerated data processing and `NetworkX` for graph analysis.

## Features

- **Centrality Analysis**: Evaluates nodes based on betweenness, degree, closeness, and eigenvector centrality.
- **Visualization**: Generates a visualization of the network, highlighting important nodes based on centrality scores.
- **NVIDIA CUDA Acceleration**: Uses `cuDF` to accelerate CSV data loading on supported devices.

### Requirements

- **Python 3.8+**
- **NVIDIA GPU** (for `cuDF` acceleration)
- **NetworkX** and **Matplotlib** for analysis and visualization.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ThayerMethod/NetworkMania.git
   cd NetworkMania
