import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from "react";


export default function App() {
    const [paper, setPaper] = useState({})


  useEffect(() => {
    // GET request using fetch inside useEffect React hook
    fetch('http://127.0.0.1:8000/paper/')
        .then(response => response.json())
        .then(actualData => {
          setPaper(actualData)
          console.log(actualData);
        });

// empty dependency array means this effect will only run once (like componentDidMount in classes)
  }, []);

  return (
      <p>{paper[0]?.contents}</p>
  );
}
