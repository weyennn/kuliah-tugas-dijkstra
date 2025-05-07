
from flask import Flask, render_template, request
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import heapq
import os
import base64
from io import BytesIO

app = Flask(__name__)

graph = {
    'Malioboro': {'Keraton Yogyakarta': 2, 'Taman Sari': 4, 'Bukit Bintang': 12, 'Alun-Alun Kidul': 3},
    'Keraton Yogyakarta': {'Malioboro': 2, 'Taman Sari': 2, 'Alun-Alun Kidul': 2, 'Tebing Breksi': 14},
    'Taman Sari': {'Malioboro': 4, 'Keraton Yogyakarta': 2, 'Pantai Parangtritis': 24, 'Alun-Alun Kidul': 1},
    'Candi Prambanan': {'Bukit Bintang': 15, 'Tebing Breksi': 7, 'Gunung Merapi Lava Tour': 20},
    'Candi Borobudur': {'Gunung Merapi Lava Tour': 28, 'Malioboro': 30, 'Bukit Bintang': 25},
    'Bukit Bintang': {'Malioboro': 12, 'Candi Prambanan': 15, 'Tebing Breksi': 5, 'Candi Borobudur': 25},
    'Tebing Breksi': {'Candi Prambanan': 7, 'Bukit Bintang': 5, 'Gunung Merapi Lava Tour': 14, 'Keraton Yogyakarta': 14},
    'Pantai Parangtritis': {'Taman Sari': 24, 'Alun-Alun Kidul': 21, 'Gunung Merapi Lava Tour': 40},
    'Gunung Merapi Lava Tour': {'Candi Borobudur': 28, 'Tebing Breksi': 14, 'Candi Prambanan': 20, 'Pantai Parangtritis': 40},
    'Alun-Alun Kidul': {'Keraton Yogyakarta': 2, 'Pantai Parangtritis': 21, 'Taman Sari': 1, 'Malioboro': 3}
}

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        if node == end:
            return (cost, path)
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + graph[node][neighbor], neighbor, path))
    return (float("inf"), [])

def generate_graph_image(path):
    G = nx.Graph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor, weight=graph[node][neighbor])
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=4)
    plt.axis('off')
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

@app.route("/", methods=["GET", "POST"])
def index():
    locations = list(graph.keys())
    return render_template("index.html", locations=locations)

@app.route("/rute", methods=["POST"])
def rute():
    asal = request.form.get("asal", "")
    tujuan = request.form.get("tujuan", "")
    if not asal or not tujuan or asal == tujuan:
        return "Asal dan tujuan harus diisi dan tidak boleh sama", 400
    jarak, jalur = dijkstra(graph, asal, tujuan)
    graph_img = generate_graph_image(jalur)
    return render_template("rute.html", asal=asal, tujuan=tujuan, jarak=jarak, jalur=jalur, graph_img=graph_img)
