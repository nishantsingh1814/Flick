import React from 'react';


const Description = ({description}) => {
  return (
      <p>{description.substring(0,100)}...</p>
  )
};

export default Description;
