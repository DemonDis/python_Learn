import './App.css';
import React, { useState, useEffect } from "react";
import Socket_client from './components/Socket_client';

function App() {
  const [dataDB, setDataDB] = useState([]);
  const [data, setData] = useState('Initializing...')

  const allPostss = () => {
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
  }
  useEffect(() => {
    allPostss()
  }, []);

  const add_date = () => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
      'request': {},
      'request_type': 'add_posts' 
      })
    };
    fetch('http://127.0.0.1:3030/', requestOptions)
      .then(response => response.json())
      .then(data => console.log(data));
  }
  const del_posts = () => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
      'request': {},
      'request_type': 'del_posts' 
      })
    };
    fetch('http://127.0.0.1:3030/', requestOptions)
      .then(response => response.json())
      .then(data => console.log(data));
  }
  useEffect(() => {
    const sse = new EventSource('http://127.0.0.1:3030/sse')
    const handleStream = (e) => { 
      switch (e.data) {
        case 'update':
          setData(e.data);
          console.log(e.data)
          allPostss();
          break;
        case 'delete':
          console.log(e.data)
          allPostss();
          break;
        default: console.log('empty')
      }
     }
    sse.onmessage = (e) =>{ handleStream(e) }
    // sse.onerror = (e) => { sse.close() }
    // return () => { sse.close()
    // }
  }, [])
  
  return (
    <div className="App">
      <header className="App-header">
        <Socket_client/>
        <button onClick={() => add_date()}>CLICK</button>
        {
          dataDB.map((item, i) => {
            return <div key={i}>{item}</div>
         })
        }
        <div>------</div>
        The last streamed item was: {data}
        <button onClick={() => del_posts()}>Delete</button>
      </header>
    </div>
  );
}

export default App;