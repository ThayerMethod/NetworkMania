# NetworkMania: Advanced Network Analysis with NVIDIA Acceleration

NetworkMania is a Python-based project for advanced analysis and 3D interactive visualization of network data stored in a CSV file. Given a CSV file with columns `ID` and `target`, NetworkMania constructs a directed graph and evaluates node importance based on centrality measures.

## Features

- **Centrality Analysis**: Assesses nodes based on betweenness and degree centrality.
- **3D Interactive Visualization**: Generates a 3D interactive visualization, where node size and color represent importance by centrality.
- **NVIDIA CUDA Acceleration**: Uses `cuDF` for accelerated CSV loading on supported devices.

### Requirements

Install the required packages:
```bash
pip install -r requirements.txt
