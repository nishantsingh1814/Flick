import React, {Component} from "react";

import OverviewDataProvider from './OverviewDataProvider';
import UserSession from './UserSession';


const Overview = (props) =>{
  return(
    <OverviewDataProvider endpoint={`/usercalls`}
                  render={(data) => <UserSession data={data} />} />
  )
}

export default Overview;
