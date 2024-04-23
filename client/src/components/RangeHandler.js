import React, { useState } from 'react';
import RangeFinder from './RangeFinder.js';
import RangeDescend from './RangeDescend.js';
import "./Intro.css"
import "./DarkMode.css"
import "./Demo.css"
import "./RangeFinder.css"


const RangeHandler = ({ mode }) => {
  return (
    <>
    <div className="single-flex-container">
        <div id="single" className="single-title-container" >
            <h1><b className="single-title">Understand </b><b>your music choices</b></h1>
        </div>
        <hr className="single-hr"></hr>
    <div className="single-title-subtext"><p>Explore <b>niche </b>sectors of your playlist needs <b>instantly</b>.</p></div>
        <div className="single-demo-container">
            {mode === 'light' ? <RangeFinder /> : <RangeDescend />}
        </div>
    </div>
    <hr className="demo-hr"></hr>
    </>
  );
};

export default RangeHandler;
