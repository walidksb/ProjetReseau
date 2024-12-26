import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');
  
  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://localhost:5000/api/analyze', {
        // Vos données ou image à analyser
        image: 'C:/Users/sam/Desktop/ProjetReseau/client/public/logo512.png'
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Erreur lors de l\'analyse');
    }
  };
  
  return (
    <div>
      <button onClick={handleSubmit}>Envoyer à Flask</button>
      <p>{message}</p>
    </div>
  );
}

export default App;