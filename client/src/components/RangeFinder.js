import React, { useState } from 'react';
import Slider from '@mui/material/Slider';
import Box from '@mui/material/Box';
import { DataGrid } from '@mui/x-data-grid';
import './RangeFinder.css';
import './DarkMode.css';

const RangeFinder = () => {
  const [value, setValue] = useState([120, 160]);
  const [myRange, setMyRange] = useState([]);

  const columns = [
    { field: 'id', headerName: '#', width: 100 },
    { field: 'name', headerName: 'Name', width: 200 },
    { field: 'artist', headerName: 'Artist', width: 200 },
    { field: 'bpm', headerName: 'BPM', width: 150 },
  ];

  const handleConfirm = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/pairint', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value }),
      });
      const data = await response.json();
      setMyRange(data.range_songs);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className ="slider-grid-flex-container">
    <div className="slider-container">
      <div className="slider-wrapper">
      <h2>BPM Range Finder</h2>
        <div className="min-max-wrapper">
          <Slider
            className="custom-slider"
            aria-label="Temperature"
            value={value}
            onChange={handleChange}
            valueLabelDisplay="auto"
            step={1}
            min={80}
            max={280}
            marks={[
              { value: 80, label: '80' },
              { value: 120, label: '120' },
              { value: 160, label: '160' },
              { value: 200, label: '200' },
              { value: 240, label: '240' },
              { value: 280, label: '280' },
            ]}
          />
        </div>
      </div>
      <div>
        <p>Select a BPM Range</p>
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
        {myRange.length > 0 && (

          <div className="datagrid-container">
            <DataGrid
              className="custom-datagrid"
              rows={myRange.map((song, index) => ({
                id: index,
                name: song.name,
                artist: song.artist,
                bpm: song.bpm,
              }))}
              columns={columns}
              pageSize={5}
              rowsPerPageOptions={[5, 10, 20]}
              disableSelectionOnClick
              getRowId={(row) => row.id}
            />
          </div>
       
      )}
       </div>
   
    </div>
  );
};

export default RangeFinder;
