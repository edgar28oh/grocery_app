import React, { useState } from "react";

const MultiSelectButtons = ({src, alt, store}) => {
  const [selectedButtons, setSelectedButtons] = useState([]);

  const handleButtonClick = (button) => {
    if (selectedButtons.includes(button)) {
      setSelectedButtons(selectedButtons.filter((item) => item !== button));
    } else {
      setSelectedButtons([...selectedButtons, button]);
    }
  };

  return (
    <div className="flex justify-center space-x-4">
      <button
        className={`w-24 h-24 bg-gray-200 flex justify-center items-center focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 hover:bg-gray-300 ${
          selectedButtons.includes("WM")
            ? "bg-lime-500"
            : "bg-teal-50"
        }`}
        onClick={() => handleButtonClick({store})}
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

export default MultiSelectButtons;
