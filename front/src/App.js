import './App.css';
import React, { useState, useEffect } from "react";

function App() {
  useEffect(() => {
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: 'React Hooks POST Request Example' })
    };
    fetch('http://127.0.0.1:3030/', requestOptions)
        .then(response => response.json())
        .then(data => console.log(data));
  }, []);
  const chekBack = () => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
      'request': {'name': 'hi!'},
      'request_type': 'auto_test' })
    };
    fetch('http://127.0.0.1:3030/', requestOptions)
      .then(response => response.json())
      .then(data => console.log(data));
  }

  return (
    <div className="App">
      <header className="App-header">
        <button onClick={() => chekBack()}>CLICK</button>
      </header>
    </div>
  );
}

export default App;
