import React from 'react';

const style={
  margin:10
}
const ImageCount = ({count}) => {
  return (
      <b style={style}>{count} images</b>
  )
};

export default ImageCount;
