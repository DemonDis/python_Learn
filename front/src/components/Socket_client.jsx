import React, { useState } from "react";
const socket = new WebSocket('ws://localhost:8001');

function Socket_client() {
  const [messages, setMessages] = useState([]);

  socket.onopen = function() {
    console.log('Соединение установлено');
  };
  
  socket.onmessage = function(event) {
    console.log(`Получено сообщение: ${event.data}`);
  };
  
  socket.onclose = function(event) {
    console.log('Соединение закрыто');
  };
  
  socket.onerror = function(error) {
    console.log(`Ошибка: ${error.message}`);
  };

  const onChange = (event) => {
    setMessages(event)
  };

  const sendMessage = () => {
    socket.send(messages);
  };

  return (
    <div>
      <label>
        Message:
        <input value={messages} onChange={e => onChange(e.target.value)} />
      </label>
      <button onClick={() => sendMessage()}>Send</button>
    </div>
  );
}

export default Socket_client;