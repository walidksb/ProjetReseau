import React, { useState } from 'react';
import axios from 'axios';
import { io } from 'socket.io-client';

const socket = io('http://localhost:5000');  // Connect to the Flask backend using SocketIO

function App() {
  const [image, setImage] = useState(null);
  const [message, setMessage] = useState('');

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => setImage(reader.result);
      reader.readAsDataURL(file);  // Convert image to base64
    }
  };

  const handleSubmitHttp = async () => {
    try {
      const response = await axios.post('http://localhost:5000/api/analyze', {
        image: image,
      });
      setMessage(`Prediction from API: ${response.data.prediction}`);
    } catch (error) {
      setMessage('Error during analysis');
    }
  };

  const handleSubmitSocket = () => {
    socket.emit('image_data', { image: image });
    socket.on('analysis_result', (data) => {
      setMessage(`Prediction from Socket: ${data.prediction}`);
    });
  };

  return (
    <div className="App">
      <h1>Image Analysis with CNN</h1>
      <input type="file" onChange={handleImageChange} />
      <button onClick={handleSubmitHttp}>Analyze via HTTP</button>
      <button onClick={handleSubmitSocket}>Analyze via Socket</button>
      <p>{message}</p>
    </div>
  );
}

export default App;
