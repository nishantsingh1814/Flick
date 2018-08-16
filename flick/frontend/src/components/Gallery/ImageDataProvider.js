import React, { Component } from "react";
import PropTypes from "prop-types";

class ImageDataProvider extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired,
  };
  state = {
      images: [],
      loaded: false,
      isLoading:true,
      placeholder: "Loading...",
      endpoint: this.props.endpoint
    };
  componentDidMount() {
    this.onPaginatedSearch();
  }

  onPaginatedSearch =()=>{
    this.setState({ isLoading:true});
    if(this.state.endpoint!=null){
    fetch(this.state.endpoint)
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ placeholder: "Something went wrong" , isLoading:false});
        }
        return response.json();
      })
      .then( data => this.setState({ images: this.state.images.concat(data.results), loaded: true, isLoading:false, endpoint:data.next }));
    }
  }
  render() {
    const { images, loaded, placeholder, isLoading } = this.state;
    return loaded ? this.props.render(images, this.onPaginatedSearch, isLoading) : <p>{placeholder}</p>;
  }
}
export default ImageDataProvider;
