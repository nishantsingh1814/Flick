import React, {Component} from "react";

import OverviewDataProvider from './OverviewDataProvider';
import UserSession from './UserSession';
import PhotoCommentsChart from './PhotoCommentsChart';


const Overview = (props) =>{
  return(
    <div>
      <OverviewDataProvider endpoint={`/usercalls`}
                    render={(data) => <UserSession data={data} />} />
      <OverviewDataProvider endpoint={`/topphotos`}
                    render={(data) => <PhotoCommentsChart data={data} />} />
    </div>
  )
}

export default Overview;
