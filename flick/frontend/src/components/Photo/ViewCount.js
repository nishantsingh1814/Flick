import React from 'react';

const style={
  margin:10
}
const ViewCount = ({count}) => {
  return (
      <b style={style}>{count} Views</b>
  )
};

export default ViewCount;
