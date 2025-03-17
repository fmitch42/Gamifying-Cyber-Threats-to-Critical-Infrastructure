import React, { useEffect, useState } from "react";
import socket from "../services/WebSocket";

const NetworkGraph = () => {
    const [status, setStatus] = useState("Waiting for updates...");

    useEffect(() => {
        socket.on("status_update", (data) => {
            setStatus(data.status);
        });
    }, []);

    return (
        <div>
            <h2>Network Status</h2>
            <p>{status}</p>
        </div>
    );
};

export default NetworkGraph;
