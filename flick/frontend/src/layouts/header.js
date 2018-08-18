import React, {Component} from "react";
import Header from "../components/Header";

export default class HeaderLayout extends Component {
    render() {
        return (
            <div>
                <div>
                    <Header />
                </div>
                <div className="main">{this.props.children}</div>
          </div>
        );
    }
}
