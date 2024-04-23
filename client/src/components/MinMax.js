import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';
import './MinMax.css';


function valuetext(value) {
  return `${value}°C`;
}

const MinMax = () => {
  const [value, setValue] = useState([20, 37]);
  const [myRange, setMyRange] = useState(null);

  const handleConfirm = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/minmax', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value }),
      });
      const data = await response.json();
      setMyRange(data.result);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className="slider-container">
      <h1></h1>
      <p className="subtext">test</p>
      <Box className="box">
        <div className="min-max-wrapper">
          <Slider
            className="custom-slider"
            aria-label="Temperature"
            value={value}
            onChange={handleChange}
            valueLabelDisplay="auto"
            getAriaValueText={valuetext}
            step={1}
            min={10}
            max={110}
            marks={[
              { value: 10, label: '10' },
              { value: 20, label: '20' },
              { value: 30, label: '30' },
              { value: 40, label: '40' },
              { value: 50, label: '50' },
              { value: 60, label: '60' },
              { value: 70, label: '70' },
              { value: 80, label: '80' },
              { value: 90, label: '90' },
              { value: 100, label: '100' },
              { value: 110, label: '110' },
            ]}
          />
        </div>
      </Box>
      <button onClick={handleConfirm} className="submit-button">Confirm</button>
      {myRange !== null && (
        <p className="range-result">My Range! {myRange}</p>
      )}
    </div>
  );
};

export default MinMax;
