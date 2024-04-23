// LDSwitch.js
import React from 'react';
import Switch from 'react-switch';
import "../App.css";
import "./Header.css";

function LDSwitch({ onDarkModeToggle, isDarkMode }) {
  const handleSwitchChange = (checked) => {
    onDarkModeToggle(checked);
  };

  return (
    <label>
      <Switch
        onChange={handleSwitchChange}
        checked={isDarkMode}
        onColor="#ff8000"
        offColor="#6A6A6A"
        activeBoxShadow="#ff8000"
        checkedIcon={false}
        uncheckedIcon={false}
      />
    </label>
  );
}

export default LDSwitch;
