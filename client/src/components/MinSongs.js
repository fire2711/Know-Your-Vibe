import React, { useState } from 'react';
import axios from 'axios';

const MinSongs = () => {
  const [minSongs, setMinSongs] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const fetchData = async () => {
    try {
      setIsLoading(true);
      const response = await axios.post('http://127.0.0.1:5000/api/test', {});
      if (response.data && response.data.min_songs) {
        // Update this line to access the correct key in the response
        setMinSongs(response.data.min_songs);
      } else {
        console.error('Error: No minimum songs data found in response');
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <h1>Minimum Songs</h1>
      <button onClick={fetchData} disabled={isLoading}>
        {isLoading ? 'Loading...' : 'Fetch Minimum Songs'}
      </button>
      {minSongs && (
        <ul>
          {minSongs.map((song, index) => (
            <li key={index}>{song.name} - {song.artist}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default MinSongs;
