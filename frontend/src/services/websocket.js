const socketUrl = process.env.REACT_APP_WS_URL || 'ws://localhost:8000';

export function connectLiveSocket(onMessage) {
  const socket = new WebSocket(socketUrl);

  socket.onopen = () => console.log('WebSocket connected');
  socket.onmessage = (event) => {
    const payload = JSON.parse(event.data);
    onMessage?.(payload);
  };
  socket.onclose = () => console.log('WebSocket closed');

  return socket;
}
