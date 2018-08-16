import React, {Component} from "react";
import Image from "./Image";
import '../../css/gallery.css';

class ImageList extends Component{
  constructor(props){
    super(props)
    this.imageItems = props.data.results.map((image, index) => {
      return(
        <div>
          <Image
            photo={image.photo}
            key={index}
          />
        </div>
      );
    });
  }
  createColumns= () =>{
    let imagesFirst = [];
    let imagesSec = [];
    let imagesThird = [];
    let imagesFourth = [];

    let column = [];
    for(let i=0; i<this.imageItems.length; i++){
      if(i%4==0){
        imagesFirst.push(this.imageItems[i]);
      }else if(i%4==1){
        imagesSec.push(this.imageItems[i]);
      }else if(i%4==2){
        imagesThird.push(this.imageItems[i]);
      }else if(i%4==3){
        imagesFourth.push(this.imageItems[i]);
      }
    }
    column.push(<div className="d-flex flex-column">{imagesFirst}</div>);
    column.push(<div className="d-flex flex-column">{imagesSec}</div>);
    column.push(<div className="d-flex flex-column">{imagesThird}</div>);
    column.push(<div className="d-flex flex-column">{imagesFourth}</div>);
    return column
  }
  render(){
    return (
      <div className="d-flex flex-row flex-wrap justify-content-center">
        {this.createColumns()}
      </div>
    );
  };
}
export default ImageList;
