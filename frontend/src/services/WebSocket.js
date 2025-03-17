import { io } from "socket.io-client";

const socket = io("http://localhost:5000");

socket.on("status_update", (data) => {
    console.log("New update:", data.status);
});

export default socket;
