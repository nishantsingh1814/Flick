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
        <div >
          <PlaceHolder
            url={data.image}
            />
          <div id="title-des" >
            <Owner owner={data.owner}/>
            <br/>
            <Title title={data.title}/>
            <br/>
            <Description description={data.details[0].description}/>
            <div>
              <CommentCount count={data.details[0].comments_count}/>
              <ViewCount count={data.details[0].views_count}/>
            </div>
            <TagList tags={data.tags}/>
          </div>
        </div>
    );
};

export default PhotoPage;
