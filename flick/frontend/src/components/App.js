import React from "react";
import ReactDOM from "react-dom";
import GroupDataProvider from './Group/GroupDataProvider';
import GroupList from './Group/GroupList';

import ImageDataProvider from './Gallery/ImageDataProvider';
import ImageList from './Gallery/ImageList';

const App = () => (
  <ImageDataProvider endpoint="/getphotos?group_id=27"
                render={data => <ImageList data={data} />} />
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
