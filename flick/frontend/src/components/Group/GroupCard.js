import React, {Component} from "react";
import ReactDOM from 'react-dom';
import '../../css/groupcard.css';
import Icon from './Icon';
import ImageCount from './ImageCount';
import MemberCount from './MemberCount';
import Description from './Description';
import Name from './Name';

import {Link} from 'react-router-dom';



const GroupCard = ({group}) => {
  return(
    <Link className="group_links" to={`/gallery/${group.id}`}>
      <div id="group_card">
        <Icon url = {group.icon}/>
        <Name name={group.name}/>
        <MemberCount count={group.member_count}/>
        <ImageCount count={group.image_count}/>
        <Description description = {group.description}/>
      </div>
    </Link>
  );
}

export default GroupCard;
