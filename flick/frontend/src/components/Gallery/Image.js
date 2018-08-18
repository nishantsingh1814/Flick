import React, {Component} from "react";
import ReactDOM from 'react-dom';
import {Link} from 'react-router-dom';

class Image extends Component{
  constructor(props){
    super(props)
    this.state = {imageLoaded:false};
  }
  handleImageimageLoaded() {
      this.setState({ imageLoaded: true });
  }

  render(){
    if(this.state.imageLoaded){
      return(
        <Link key={this.props.photo.id} to={`/photo/${this.props.photo.id}`}>
            <div >
              <img id="gallery-img" src = {this.props.photo.image} onLoad={this.handleImageimageLoaded.bind(this)} className="img-fluid"/>
            </div>
        </Link>
      )
    }
    return(
      <Link key={this.props.photo.id} to={`/photo/${this.props.photo.id}`}>
          <div >
            <img id="gallery-img" src = {this.props.photo.image} onLoad={this.handleImageimageLoaded.bind(this)} className="img-fluid img-background"/>
          </div>
      </Link>
    )
  }
}


export default Image;
