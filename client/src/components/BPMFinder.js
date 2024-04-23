import React, { useState } from 'react';
import Slider from '@mui/material/Slider';
import Box from '@mui/material/Box';
import { DataGrid } from '@mui/x-data-grid/DataGrid';
import "./Demo.css"
import "./Single.css"
import "./DarkMode.css"

const BPMFinder = () => {
  const [sliderValue, setSliderValue] = useState(110);
  const [specificSongs, setSpecificSongs] = useState([]);

  const handleConfirm = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/singleint', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value: sliderValue }),
      });
      const data = await response.json();
      setSpecificSongs(data.specific_songs);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleSliderChange = (event, newValue) => {
    setSliderValue(newValue);
  };

  // Define columns for the DataGrid
  const columns = [
    { field: 'id', headerName: '#', width: 100 },
    { field: 'artist', headerName: 'Artist', width: 200 },
    { field: 'name', headerName: 'Title', width: 200 },
    { field: 'bpm', headerName: 'BPM', width: 150 },
  ];

  return (
    <>
    <div className="slider-grid-flex-container">
    <div className="slider-container">
      <div className="slider-wrapper">
      <h2>BPM Finder</h2>
        <Slider
          className="custom-slider"
          aria-label="Temperature"
          value={sliderValue}
          onChange={handleSliderChange}
          valueLabelDisplay="auto"
          shiftStep={30}
          step={1}
          min={100}
          max={150}
          marks={[
            { value: 100, label: '100' },
            { value: 150, label: '150' },
            // Add more marks as needed
          ]}
        />
        
      </div>
      <div>
        <p>Select a BPM</p>
      </div>
      <button onClick={handleConfirm} className="submit-button">Confirm</button>
      <div className="anonymous-container">
            <p>"With Viber, we are able to improve our song curation at the click of a button. Any song is a dropoff point
                and we're able to gain insight on what type of music our users like."
            </p>
            <p>- Anonymous</p>
        </div>
       </div>
       <div className="datagrid-container-wrapper">
      {specificSongs.length > 0 && (
        <div className= "datagrid-container">
          <DataGrid
            className="custom-datagrid"
            rows={specificSongs.map((song, index) => ({ ...song, id: index }))}
            columns={columns}
            pageSize={5}
            rowsPerPageOptions={[5, 10, 20]}
            // checkboxSelection
            disableSelectionOnClick
            getRowId={(row) => row.id}
          />
        </div>
      )}
       </div>
      </div>
   </>
  );
};

export default BPMFinder;
