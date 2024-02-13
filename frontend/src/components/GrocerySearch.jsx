import React, { useState } from 'react';

// Handles the search bar for the page

const GrocerySearch = ({ onSearch, selectedStores }) => {
  const [query, setQuery] = useState('');

  const handleSearch = async () => {
    try {
      const response = await fetch('/api/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query, selectedStores }),
      });

      if (response.ok) {
        const data = await response.json();

        onSearch(data);
      } else {
        console.error('Error searching for groceries:', response.statusText);
      }
    } catch (error) {
      console.error('Error searching for groceries:', error);
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Search for groceries..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch} className="mt-1 bg-blue-500 text-white py-1 px-2 rounded">Search</button>
    </div>
  );
};

export default GrocerySearch;
