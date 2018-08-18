import React, {Component} from "react";
import Image from "./Image";
import '../../css/gallery.css';

class ImageList extends Component{
  constructor(props){
    super(props)
  }
  updateImages=()=>{

    return  this.props.images.map((image, index) => {
      return(
          <Image
            photo={image.photo}
            key={image.id}
          />
      );
    });
  }
  createColumns= () =>{
    let imageItems= this.updateImages();
    let imagesFirst = [];
    let imagesSec = [];
    let imagesThird = [];
    let imagesFourth = [];

    let column = [];
    for(let i=0; i<imageItems.length; i++){
      if(i%4==0){
        imagesFirst.push(imageItems[i]);
      }else if(i%4==1){
        imagesSec.push(imageItems[i]);
      }else if(i%4==2){
        imagesThird.push(imageItems[i]);
      }else if(i%4==3){
        imagesFourth.push(imageItems[i]);
      }
    }
    column.push(<div className="d-flex flex-column">{imagesFirst}</div>);
    column.push(<div className="d-flex flex-column">{imagesSec}</div>);
    column.push(<div className="d-flex flex-column">{imagesThird}</div>);
    column.push(<div className="d-flex flex-column">{imagesFourth}</div>);
    return column
  }
  componentDidMount() {
    window.addEventListener('scroll', this.onScroll, false);
  }

  componentWillUnmount() {
    window.removeEventListener('scroll', this.onScroll, false);
  }

  onScroll = () => {
    if (
    (window.innerHeight + window.scrollY==document.body.scrollHeight)&&
      this.props.images.length && !this.props.isLoading
    ) {
      this.props.onPaginatedSearch();
    }
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
