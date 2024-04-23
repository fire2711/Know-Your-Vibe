import React, {useState, useEffect} from 'react'
import "./Intro.css";

// component for slowest songs
import MinSongs from "./MinSongs.js"
import IntroBPM from "./IntroBPM.js"
import Single from "./Single.js"

export default function Intro({ mode }) {

    
  return (
    <div id="intro" className="flex-container">
    <div className ="intro">
      <h1><b>Know Your </b><b></b><b className="intro-vibe">Vibe</b><b className="intro-dot">.</b></h1>
      <p className ="intro-subtext">Leverage your mood to discover songs you can enjoy.</p>
      <p className ="intro-subtext">
      This database is powered by <span className="sort">{mode === 'light' ? 'quicksort' : 'heapsort'}.</span></p>
      <div className="demo-button-wrapper">
        <a href ="#single"className="demo-button">Get Started</a>
      </div>      
    </div>
    <div className = "word-block">
      <div className ="user-container">
        <p className= "user-box">User</p>
        <div className="user-block">
          <p>I'm in the mood for a slow song.</p>
        </div>
      </div>
      <div className="vibes-container">
        <p className="vibes-box">Viber</p>
        <div className="vibes-block">
          <div className = "intro-bpm-wrapper">
            <IntroBPM/>
          </div>
            <div className="intro-bpm-subtext">
              <div className ="intro-bpm-subtext-list">
                <p><b><span className ="intro-bpm-subtext-number">1. </span> Identify your tempo</b></p>
                <span><p>Use our BPM finder to improve your song selection.</p></span>
              </div>
              <div className="intro-bpm-subtext-list">
                <p><b><span className ="intro-bpm-subtext-number">2. </span> Create playlists </b></p>
                <span><p>User-tailored experience to invent playlists meant for you.</p></span>
              </div>
          </div>
        </div>
      </div>
    </div>
    <hr className="intro-hr"></hr>
    </div>
  )
}
