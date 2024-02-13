import React from 'react';

// hadles the items on the Grocery List

const GroceryList = ({selectedItems}) => {


  return (
    <div>
      <h2>Selected Items</h2>
      <ul>
        {selectedItems.map((item, index) => (
          <li key={index}>({item.store}) {item.name} - ${item.price}</li>
        ))}
      </ul>
    </div>
  );
};

export default GroceryList;

