const socket = io();

function buyResource(resource) {
    socket.emit("buy_resource", { resource: resource });
    alert(`${resource} purchased!`);
}
