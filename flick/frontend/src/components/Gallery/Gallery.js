import React, {Component} from "react";

import ImageDataProvider from './ImageDataProvider';
import ImageList from './ImageList';


const Gallery = (props) =>{
  return(
    <ImageDataProvider endpoint={`/getphotos?group_id=${props.match.params.id}`}
                  render={(images, onPaginatedSearch, isLoading) => <ImageList images={images} onPaginatedSearch={onPaginatedSearch} isLoading={isLoading} />} />
  )
}

export default Gallery;
