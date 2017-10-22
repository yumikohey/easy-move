import React, { Component } from 'react';
import {
  Link
} from 'react-router-dom';
import "./services.css";

class Service extends Component {
  constructor(props) {
    super(props)
    this.state = { address: '123 California St., San Francisco, CA' }
    this.onChange = (e) => this.setState({ address: [e.target.value] });
  }

    render() {
        return (
            <div className="container-fluid">
                <div className="sf-bg-img"> <div className="bg-layer"></div></div>
                <div className="service-content">
                    <div className="service-text">
                        <p>What you need to do before you move in?</p>
                    </div>
                    <div className="sign-up-and-cancel">
                        <div className="service-box sign-up">
                            <div className="title">
                                <div className="highlighted-text">Sign up services for </div>
                            </div>
                            <div className="color-strip">
                                <div>
                                    123 State St. Chicago, IL 60602
                                </div>
                            </div>
                            <div className="check-box-section">
                                <label className="check">
                                    <input type="checkbox"/>
                                    <div className="box"></div>
                                </label>
                            </div>
                        </div>
                        <div className="service-box cancel">
                            <div className="title">
                                <div className="grey-text">Cancel services for </div>
                            </div>
                            <div className="grey-strip">
                                <div>
                                    15 Kimberly Ln. Morrissonville, NY 12962
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Service;