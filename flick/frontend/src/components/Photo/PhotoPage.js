import React from "react";
import CommentCount from "./CommentCount";
import Description from "./Description";
import Owner from './owner';
import PlaceHolder from './PlaceHolder';
import TagList from './TagList';
import ViewCount from './ViewCount';
import Title from './Title';
import '../../css/photopage.css';

const PhotoPage = ({data}) => {
    return (
        <div id="mainContent" >
          <PlaceHolder
            url={data.image}
            />
          <Owner owner={data.owner}/>
          <br/>
          <div id="title-des">
            <Title title={data.title}/>
            <br/>
            <Description description={data.description}/>
          </div>
          <div>

            <div >
              <CommentCount count={data.comments_count}/>
              <ViewCount count={data.views_count}/>
            </div>
            <TagList tags={data.tags}/>
          </div>
        </div>
    );
};

export default PhotoPage;
