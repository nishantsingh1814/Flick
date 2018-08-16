import GroupDataProvider from './GroupDataProvider';
import React, {Component} from "react";

import GroupList from './GroupList';


const Group = () =>{
  return(
    <GroupDataProvider endpoint="/getgroups"
                  render={(data) => <GroupList data={data} />} />
  );
}

export default Group;
