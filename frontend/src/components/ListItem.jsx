import React from 'react';
//Handles the items in the search results
const ListItem = ({ items, onItemClick }) => {
  return (
    <div className="flex flex-wrap justify-center">
      {items.map((item, index) => (
        <div key={index} className="max-w-64 mx-4 my-4 bg-gray-100 rounded-lg shadow-md">
          <div className="relative">
            <img className="w-full h-auto rounded-t-lg max-w-xs" src={item.image_src} alt={item.name} />
            <div className="absolute inset-0 bg-black opacity-5 rounded-t-lg"></div>
          </div>
          <div className="p-4">
            <p className="text-lg text-center font-semibold mb-2">{item.name}</p>
            <p className="text-black-300">Store: {item.store}</p>
            <p className="text-black-300">Price: {item.price}</p>
            <p className="text-black-300">Sale Price: {item.sale_price ? `$${item.sale_price}` : "Not on Sale"}</p>
            <div className= "mx-0 flex flex-col items-center">
                <button onClick={() => onItemClick(item)} className="mt-2 bg-blue-500 text-white py-2 px-4 rounded">Add to List</button>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
  
};

export default ListItem;
