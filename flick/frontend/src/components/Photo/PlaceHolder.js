import React,{Component} from 'react';
import ReactDOM from 'react-dom';

const styles={
  marginLeft:'20%',
  marginRight:'20%'
}
const PlaceHolder = ({url}) => {
  return (
    <div style={styles}>
      <img src={url}/>
    </div>
  )
}
export default PlaceHolder;
