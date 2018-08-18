import React, { Component } from "react";
import PropTypes from "prop-types";

class PhotoDataProvider extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired
  };
  state = {
      data: [],
      loaded: false,
      placeholder: "Loading..."
    };

  componentDidMount() {
    fetch(this.props.endpoint,{method: 'get',
        headers: {'Authorization':`Token ${localStorage.getItem('Token')}`},})
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ placeholder: "Something went wrong" });
        }
        return response.json();
      })
      .then( data => this.setState({ data: data.data, loaded: true }));
  }
  render() {
    const { data, loaded, placeholder } = this.state;
    return loaded ? this.props.render(data) : <p>{placeholder}</p>;
  }
}
export default PhotoDataProvider;
