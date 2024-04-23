import React from 'react'
import "./DarkMode.css";
import "./Intro.css";
import "./Single.css";

// Single BPM Finder
import BPMFinder from "./BPMFinder.js"

export default function Single() {
  return (
    <>
    <div className="single-flex-container">
    
    <div id="single" className="single-title-container" >
        <h1><b>One space for </b><b className="single-title">any </b><b className="i">BPM</b></h1>

    </div>
    <hr className="single-hr"></hr>
    <div className="single-title-subtext"><p>Reduce playlist <b>friction </b>  powered by your own interests as <b>dropoff </b>points.</p></div>
    <div className="single-demo-container">
        <BPMFinder/>
    </div>
    </div>
    <hr className="demo-hr"></hr>    
    </>
  )
}


