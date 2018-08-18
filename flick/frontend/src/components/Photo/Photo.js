import PhotoDataProvider from './PhotoDataProvider';
import React, {Component} from "react";

import PhotoPage from './PhotoPage';


const Photo = (props) =>{
  return(
    <PhotoDataProvider endpoint={`/getphotoinfo?photo_id=${props.match.params.id}`}
                  render={(data) => <PhotoPage data={data} />} />
  );
}

export default Photo;
