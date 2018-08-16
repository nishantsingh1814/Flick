import React, {Component} from "react";
import ReactDOM from 'react-dom';

const Image = ({photo}) => {

  return (
    <div>
      <img src = {photo.image} className="img-fluid"/>
    </div>
  );
}

export default Image;
