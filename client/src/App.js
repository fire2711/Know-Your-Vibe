// App.js
import React, { useState } from "react";
import logo from './VLogo.png';
import './App.css';
import './components/DarkMode.css';

// Stuff I use
import Header from "./components/header.js";
import Intro from "./components/Intro.js";
import Single from "./components/Single.js";
import RangeHandler from "./components/RangeHandler.js";

function App() {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };

  return (
    <div className={`app ${isDarkMode ? 'dark-mode' : 'light-mode'}`}>
      <Header onDarkModeToggle={toggleDarkMode} />
      <Intro mode={isDarkMode ? 'dark' : 'light'} />
      <Single />
      <RangeHandler mode={isDarkMode ? 'dark' : 'light'} />
    </div>
  );
}

export default App;
