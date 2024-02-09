import React, { useState, useEffect } from 'react';

function GroceryItem() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetch('/items', {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(response => response.json())
          .then(data => {
                setItems(data); 
            })
            .catch(error => console.error('Error fetching items:', error));
    }, []);

    return (
        <div className="flex flex-wrap justify-center">
            {items.map((item, index) => (
                <div key={index} className="max-w-xs mx-4 my-4 bg-gray-100 rounded-lg shadow-md">
                    <div className="relative">
                        <img className="w-full h-auto rounded-t-lg" src={item.image_src} alt={item.name} />
                        <div className="absolute inset-0 bg-black opacity-50 rounded-t-lg"></div>
                        <div className="absolute bottom-0 w-full p-4 text-white">
                            <p className="text-lg font-semibold mb-2">{item.name}</p>
                            <p className="text-gray-300">Price: {item.price}</p>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    );
}

export default GroceryItem;
