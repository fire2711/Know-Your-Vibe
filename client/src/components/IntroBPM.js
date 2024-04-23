import React, { useState } from 'react';
import Slider from '@mui/material/Slider';
import "./Demo.css"
import "./Intro.css"

const IntroBPM = () => {
    const [sliderValue, setSliderValue] = useState(100);
    const [demoSong, setDemoSong] = useState(null);

    const handleConfirm = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/singledemo', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ bpm: sliderValue }),
            });
            const data = await response.json();
            setDemoSong(data.specific_songs[0]);  // Set the first song from the response to demoSong
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const handleSliderChange = (event, newValue) => {
        setSliderValue(newValue);
    };

    return (
        <div className="slider-container">
            <h3>BPM Finder</h3>
            <div className="slider-wrapper-intro">
                <Slider
                    style={{marginTop: "0px"}}
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
                        { value: 100, label: 'slow' },
                        { value: 110, label: '' },
                        { value: 120, label: '' },
                        { value: 130, label: '' },
                        { value: 140, label: '' },
                        { value: 150, label: 'fast' },
                    ]}
                />
            </div>
            <button onClick={handleConfirm} className="submit-button-intro">demo</button>
                <b className ="submit-button-subtext">you might like:</b>
            {demoSong && (
                <div className="demo-output">
                
                    <p>{demoSong.artist} - {demoSong.title}</p>
                </div>
            )}
        </div>
    );
};

export default IntroBPM;
