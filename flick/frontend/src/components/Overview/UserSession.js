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
  console.log(sessionCalls);
  return(
    <div id="user-session-chart">
      <LineChart
        axes
        grid
        dataPoints
        width={700}
        height={350}
        verticalGrid
        axisLabels={{x: 'Sessions', y: 'Calls'}}
        data={[sessionCalls]}
      />
    </div>
  )
}

export default UserSession;
