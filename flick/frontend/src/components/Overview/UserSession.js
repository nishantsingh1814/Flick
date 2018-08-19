import React from "react";

import {LineChart} from 'react-easy-chart';
import '../../css/overview.css';

const UserSession=({data}) =>{
  const sessionCalls=[]
  for(var i = 0; i < data.length; i++){
    var text = {}
    text.x=i+1;
    text.y=data[i].click;
    sessionCalls.push(text);
  }
  return(
    <div id="user-session-chart">
      <LineChart
        axes
        grid
        dataPoints
        width={700}
        height={350}
        verticalGrid
        axisLabels={{x: 'My x Axis', y: 'My y Axis'}}
        data={[sessionCalls]}
      />
    <h3>No. of calls made by user in each session</h3>
    </div>
  )
}

export default UserSession;
