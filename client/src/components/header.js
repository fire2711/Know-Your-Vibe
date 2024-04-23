// Header.js
import React from 'react';
import "./Header.css";
import logo from "../VLogo.png";
import "./DarkMode.css";
import LDSwitch from "./LDSwitch.js";

export default function Header({ onDarkModeToggle }) {
  return (
    <>
      <nav className="navbar">
        <div className="left">
          <a href="#demo" className="navbar-brand"><b>V</b><span>iber</span></a>
          <div className="anchor-wrapper">
            <a className="navbar-button" href="#intro">Home</a>
            {/* <a className="navbar-button">Meet the Team</a> */}
            <a className="navbar-button" href="#single">Get Started</a>
          </div>
        </div>
        <div className="right">
          {/* <a className="navbar-button" href="#single">Get Started</a> */}
          <div className="switch-wrapper">
            <LDSwitch onDarkModeToggle={onDarkModeToggle} />
          </div>
        </div>
      </nav>
    </>
  );
}
