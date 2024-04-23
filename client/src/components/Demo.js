import React, { useState } from 'react';
import Slider from '@mui/material/Slider';
import "./Demo.css"


const Demo = () => {
  const [sliderValue, setSliderValue] = useState(0);
  const [multipliedValue, setMultipliedValue] = useState(null);

  const handleConfirm = async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/multiply', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ value: sliderValue }),
          });
      const data = await response.json();
      setMultipliedValue(data.result);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleSliderChange = (event, newValue) => {
    setSliderValue(newValue);
  };

  return (
    <div className="slider-container">
       <h1>Slide for your vibe</h1>
            <p className ="subtext">Use your mood to find songs you will enjoy</p>
        <div className="slider-wrapper">
      <Slider
        className="custom-slider"
        aria-label="Temperature"
        value={sliderValue}
        onChange={handleSliderChange}
        valueLabelDisplay="auto"
        shiftStep={30}
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
      <button onClick={handleConfirm} className="submit-button">Confirm</button>
      {multipliedValue !== null && (
        <p>Multiplied value: {multipliedValue}</p>
      )}
    </div>
  );
};

export default Demo;
