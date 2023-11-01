import './App.css';
import React, { useState, useEffect } from "react";

function App() {
  const [dataDB, setDataDB] = useState([]);
  const [data, setData] = useState('Initializing...')

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
        setDataDB(data ? data.request.name : [])
       })
       .catch((error) => {
         console.error(error);
       });
    
  }, []);

  const add_date = () => {
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
  useEffect(() => {
    const sse = new EventSource('http://127.0.0.1:3030/sse')
    // const handleStream = (e) => { setData(e.data) }
    // sse.onmessage = (e) =>{ handleStream(e) }
    sse.onmessage = (e) => {
      switch (e.data) {
        case 'update_posts':
          setData(e.data);
          break;
        case '5':
          console.log('!!!!!!!')
        default: setData(e.data);
      }
    }
    sse.onerror = (e) => { sse.close() }
    return () => { sse.close()
    }
  }, [])
  
  return (
    <div className="App">
      <header className="App-header">
        <button onClick={() => add_date()}>CLICK</button>
        {
          dataDB.map((item, i) => {
            return <div key={i}>{item}</div>
         })
        }
        <div>------</div>
        The last streamed item was: {data}
        {/* <button onClick={() => startSSE()}>Start SSE</button>
        <button onClick={() => stopSSE()}>STOP SSE</button> */}
      </header>
    </div>
  );
}

export default App;
