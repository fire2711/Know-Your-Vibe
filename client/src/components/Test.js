import React, { useState } from 'react';
import axios from 'axios';

function Test() {
  const [inputValue, setInputValue] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000', inputValue);
      setResult(response.data);
    } catch (error) {
      console.error('Error sending request:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Enter an integer:
          <input type="number" value={inputValue} onChange={(e) => setInputValue(e.target.value)} />
        </label>
        <button type="submit">Submit</button>
      </form>
      {result && <div>Result: {result}</div>}
    </div>
  );
}

export default Test;
