import React, {Component} from "react";
import ReactDOM from 'react-dom';
import {Link} from 'react-router-dom';

const Image = ({photo}) => {

  return (
    <Link key={photo.id} to={`/photo/${photo.id}`}>
        <div >
          <img id="gallery-img" src = {photo.image} className="img-fluid"/>
        </div>
    </Link>
  );
}

export default Image;
