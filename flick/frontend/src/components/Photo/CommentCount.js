import React from 'react';

const style={
  margin:10
}
const CommentCount = ({count}) => {
  return (
      <b style={style}>{count} Comments</b>
  )
};

export default CommentCount;
