import { useEffect, useState } from "react";
import api from "../services/api";

function Requests() {
  const [incoming, setIncoming] = useState([]);
  const [outgoing, setOutgoing] = useState([]);

  useEffect(() => {
    loadRequests();
  }, []);

  const loadRequests = async () => {
    try {
      const incomingRes = await api.get(
        "/exchange/received/"
      );

      const outgoingRes = await api.get(
        "/exchange/sent/"
      );

      setIncoming(incomingRes.data);
      setOutgoing(outgoingRes.data);

    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Requests</h1>

      <h2>Incoming Requests</h2>

      {incoming.map((request) => (
  <div key={request.id}>
    <p>
      Request #{request.id}
    </p>

    <p>
      Status: {request.status}
    </p>

    {request.status === "PENDING" && (
      <button
        onClick={() =>
          acceptRequest(request.id)
        }
      >
        Accept
      </button>
    )}

    {request.status === "ACCEPTED" && (
      <button
        onClick={() =>
          completeRequest(request.id)
        }
      >
        Complete
      </button>
    )}
  </div>
))}

      <h2>Outgoing Requests</h2>

      {outgoing.map((request) => (
        <div key={request.id}>
          <p>
            Request #{request.id}
          </p>

          <p>
            Status: {request.status}
          </p>
        </div>
      ))}
    </div>
  );
}
const acceptRequest = async (id) => {
  try {
    await api.post(
      `/exchange/${id}/accept/`
    );

    loadRequests();

  } catch (error) {
    console.error(error);
  }
};

const completeRequest = async (id) => {
  try {
    await api.post(
      `/exchange/${id}/complete/`
    );

    loadRequests();

  } catch (error) {
    console.error(error);
  }
};

export default Requests;