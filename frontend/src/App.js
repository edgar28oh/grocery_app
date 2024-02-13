import React, { useState, useEffect } from 'react';
import ListItem from './components/ListItem';
import GroceryList from './components/GroceryList';
import GrocerySearch from './components/GrocerySearch';
import StoreIcons from './components/StoreIcons';
import './App.css';

const App = () => {

  // state to hold selected stores
  const [selectedStores, setSelectedStores] = useState([]);

  // search results state
  const [searchResults, setSearchResults] = useState([]);

  // handle search result
  const handleSearch = (data) => {setSearchResults(data);};

  // State to hold selected items
  const [selectedItems, setSelectedItems] = useState([]);

  // handle adding an item to the selected items list
  const handleAddItem = (item) => {
    // DEBUG console.log('Item added:', item);
    setSelectedItems([...selectedItems, item]);
  };
  // Function to handle store selection
  const handleStoreSelect = (store) => {
    setSelectedStores((prevSelectedStores) => {
      if (prevSelectedStores.includes(store)) {
        return prevSelectedStores.filter((s) => s !== store);
      } else {
        return [...prevSelectedStores, store];
      }
    });
  };
  // time state JUST an API test
  const [currentTime, setCurrentTime] = useState(404);
  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time)
    });
  }, []);
  
return (

    <div className="h-screen flex flex-col">
      <h1 className='text-center text-4xl'>Grocery App </h1>
      <p>the time is {currentTime}</p>
      <div className="h-1/6 flex"> {/* top container */}
        <div className="w-1/2 border-solid border-2 border-purple-950	 "> {/* left half */}
          <h2>
            Stores
          </h2>
            {/*  option to select stores */}
            <div className="flex justify-center items-center space-x-4 ">
              <StoreIcons src={process.env.PUBLIC_URL + "WM_logo.png"} alt ="Wal-Mart Store Logo" store="Wal-Mart" selectedStores={selectedStores} onStoreSelect={handleStoreSelect}/>
              <StoreIcons src={process.env.PUBLIC_URL + "FM_logo.png"} alt ="Fred Meyer Store Logo" store="Fred-Meyer" selectedStores={selectedStores} onStoreSelect={handleStoreSelect}/>
            </div>
        </div>
        <div className="w-1/2 border-solid border-2 border-purple-950"> {/* right half */}
          <h2>Search items to add to your list!</h2>
          <GrocerySearch onSearch={handleSearch} selectedStores ={selectedStores}/>
        </div>
      </div>
      <div className="flex-1 flex"> {/* bottom container */}
        <div className="w-4/6 border-solid border-2 border-purple-950"> {/* left half */}
          <h2>Search Results</h2>
          {searchResults.length > 0 && <ListItem items={searchResults} onItemClick={handleAddItem} />}
        </div>
        <div className="w-2/6 bg-gray-200 border-solid border-2 border-purple-950"> {/* right half */}
          <h2>Grocery Lists</h2>
          <p>---------------</p>
          <GroceryList selectedItems={selectedItems} />
        </div>
      </div>
    </div>
  );
};

export default App;
