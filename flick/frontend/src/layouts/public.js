import React, {Component} from "react";

export default class PublicLayout extends Component {
    render() {
        return (
          <div>
          {this.props.children}
          </div>
        );
    }
}
