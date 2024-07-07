=========
Broadcast
=========

Console messages :lower:`(stdout)` can be sent to the browser console instead through the `DevTools <https://chromedevtools.github.io/devtools-protocol/>`_ protocol.

Interface
=========

.. code-block:: typescript

  interface LogStatus {
      name: string;
      type: number;
      value: string;
      timeStamp: number;
      from: string;
      sessionId: string;
      duration?: number;
      source?: string;
  }

  interface BroadcastResponse {
      event: "broadcast" | "close" | "error";
      socketId?: string | string[];
      type?: string;
      encoding?: BufferEncoding;
      value?: unknown; // Payload
      timeStamp?: number;
      status?: LogStatus[];
      errors?: string[];
      options?: unknown;
  }

Example usage
=============

.. code-block:: javascript

  squared.broadcast(result => { console.log(result.value); }, "111-111-111"); // Messages from "project-1" project
  squared.broadcast(result => { console.log(result.value); }, { socketId: "222-222-222", socketKey: "socket_id" }); // Messages sent from another channel (default is "socketId")

  await squared.copyTo("/path/to/project", {
    projectId: "project-1",
    log: { useColor: true }, // Chromium
    broadcastId: "111-111-111" // Specific use alias for "socketId"
  });