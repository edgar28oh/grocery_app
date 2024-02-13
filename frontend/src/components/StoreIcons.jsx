import React, { useState } from 'react';


const StoreIcons = ({ src, alt, store, selectedStores, onStoreSelect }) => {
  /*
    const [selectedStore, setSelectedStore] = useState([]);
  
    const toggleSelectStore = () => {
      setSelectedStore((prevSelectedStore) => {
        if (prevSelectedStore.includes(store)) {
          return prevSelectedStore.filter((s) => s !== store);
        } else {
          return [...prevSelectedStore, store];
        }
      });
    };
    */
   const isSelected = selectedStores.includes(store);

   const handleClick = () => {onStoreSelect(store);};
  
    return (
      <div className="flex">
        <button
          className={`w-24 h-24 bg-gray-200 flex justify-center items-center focus:outline-none hover:bg-gray-300 ${
            isSelected ? 'bg-lime-500' : 'bg-gray-500'
            //selectedStore.includes(store) ?
          }`}
          //onClick={toggleSelectStore}
          onClick={handleClick}
        >
          <img
            src={src}
            alt={alt}
            className="w-20 h-20"
          />
        </button>
      </div>
    );
  };

export default StoreIcons;