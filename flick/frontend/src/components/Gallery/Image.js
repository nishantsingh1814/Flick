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
        <Link className="image_links" key={this.props.photo.id} to={`/photo/${this.props.photo.id}`}>
            <div className="image-card">
              <div className="content-container">
                <h4><b>{this.props.photo.owner}</b></h4>
                <p>{this.props.photo.title}</p>
              </div>
              <img  src = {this.props.photo.image} onLoad={this.handleImageimageLoaded.bind(this)} className="img-fluid"/>
              {this.props.photo.details[0]&&
                <div className="content-container">
                  <p>{this.props.photo.details[0].comments_count} comments </p>
                  <p>{this.props.photo.details[0].views_count} views</p>
                </div>
              }
            </div>
        </Link>
      )
    }
    return(
      <Link className="image_links" key={this.props.photo.id} to={`/photo/${this.props.photo.id}`}>
          <div className="image-card">
            <div className="content-container">
              <h4><b>{this.props.photo.owner}</b></h4>
              <p>{this.props.photo.title}</p>
            </div>
            <img  src = {this.props.photo.image} onLoad={this.handleImageimageLoaded.bind(this)} className="img-fluid img-background"/>
            {this.props.photo.details[0]&&
              <div className="content-container">
                <p>{this.props.photo.details[0].comments_count} comments </p>
                <p>{this.props.photo.details[0].views_count} views</p>
              </div>
            }
          </div>
      </Link>
    )
  }
}


export default Image;
