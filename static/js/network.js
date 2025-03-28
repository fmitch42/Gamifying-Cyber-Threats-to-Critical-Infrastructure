const socket = io();

function fetchNetwork() {
    fetch("/api/network")
        .then(response => response.json())
        .then(data => drawNetwork(data));
}

function drawNetwork(data) {
    let cy = cytoscape({
        container: document.getElementById('cy'),
        elements: [
            ...data.nodes.map(node => ({ data: { id: node.id, label: node.type } })),
            ...data.edges.map(edge => ({ data: { source: edge.source, target: edge.target } }))
        ],
        style: [
            { selector: 'node', style: { 'label': 'data(label)', 'background-color': '#007bff' } },
            { selector: 'edge', style: { 'line-color': '#ccc', 'width': 2 } }
        ],
        layout: { name: 'grid' }
    });
}

// Add a new device when button is clicked
function addDevice() {
    socket.emit("update_network", {});
}

// Listen for updates and refresh network
socket.on("network_updated", data => drawNetwork(data));

document.addEventListener("DOMContentLoaded", fetchNetwork);
