import React,{Component} from 'react';
import ReactDOM from 'react-dom';

const styles={
  width:'600',
  height:'400',
  float:'left',
  margin:'30',
  borderRight:'groove'
}
const Owner = ({owner}) =>{
  return(
    <div style={styles}>
        <h3 style={{fontFamily: "Gill Sans",fontSize:'40'}}>{owner}</h3>
    </div>
  )
}

export default Owner;
