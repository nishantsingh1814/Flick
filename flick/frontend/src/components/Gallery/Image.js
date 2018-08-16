import React, {Component} from "react";
import ReactDOM from 'react-dom';

const Image = ({photo}) => {
  console.log(photo);
  console.log('asa');
  return (
    <div>
      <img src = {photo.image} class="img-fluid"/>
    </div>
  );
}

export default Image;
