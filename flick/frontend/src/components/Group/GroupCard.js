import React, {Component} from "react";
import ReactDOM from 'react-dom';
import '../../css/groupcard.css';

import {Link} from 'react-router-dom';



const GroupCard = ({group}) => {
  return(
    <Link to={`/gallery/${group.id}`}>
      <div id="group_card">
        <div id='card_content'>
          <div id = 'image_content'>
          <img src = {group.icon}/>
          </div>
          <div id="desc">
            <p className="strong slate">{group.name}</p>
            <h6 className="secondary">{group.member_count}</h6>
            <h6 className="secondary">{group.image_count}</h6>
          </div>
        </div>
      </div>
    </Link>
  );
}

export default GroupCard;
