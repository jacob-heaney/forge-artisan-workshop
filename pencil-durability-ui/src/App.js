import './App.css';
import {useEffect, useState} from "react";


export default function App() {
    const [paper, setPaper] = useState({})


  useEffect(() => {
    fetch('http://127.0.0.1:8000/paper/')
        .then(response => response.json())
        .then(actualData => {
          setPaper(actualData)
          console.log(actualData);
        });
  }, []);

  return (
      <p>{paper[0]?.contents}</p>
  );
}
