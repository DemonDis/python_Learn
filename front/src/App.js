import './App.css';
import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
      fetch('http://127.0.0.1:3030/', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          'request': {},
          'request_type': 'posts' 
        }),
       })
       .then((response) => response.json())
       .then((data) => {
          setData(data ? data.request.name : [])
       })
       .catch((error) => {
         console.error(error);
       });
    
  }, []);
  const chekBack = () => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
      'request': {},
      'request_type': 'add_posts' })
    };
    fetch('http://127.0.0.1:3030/', requestOptions)
      .then(response => response.json())
      .then(data => console.log(data));
  }

  return (
    <div className="App">
      <header className="App-header">
        <button onClick={() => chekBack()}>CLICK</button>
        {
          data.map((item, i) => {
            return <div key={i}>{item}</div>
         })
        }
      </header>
    </div>
  );
}

export default App;
