import React, { Component } from 'react';
import classNames from "classnames";
import "./questionnaire.css";
import {
  Link
} from 'react-router-dom';

class Questionnaire extends Component {
    constructor() {
        super();
        this.state = {
            hasNewAddress: null
        };
    }

    selectImage(hasNewAddress) {
        if (hasNewAddress) {
            this.setState({hasNewAddress: true});
            console.log("yes");
        } else {
            this.setState({hasNewAddress: false});
            console.log("no");
        }
    }

    render() {
        const yesIsSelected = this.state.hasNewAddress ? "option-image option-selected" : "option-image";
        const noIsSelected = (this.state.hasNewAddress === null || this.state.hasNewAddress === true) ? "option-image" : "option-image option-selected";
        return (
            <div className="container-fluid">
                <div className="sf-bg-img"> <div className="bg-layer"></div></div>
                <div className="main-content">
                    <div className="questions">
                        <div className="question-text">
                            <p>Have you found a new place to move in yet?</p>

                            <div className="response">
                                <div className="two-option-images">
                                    <div className={yesIsSelected} onClick={(e) => this.selectImage(true)}>
                                        <img src="./img/apartment.png" alt="" width="100px"/>

                                        <div className="option-image-label">
                                            <p>Yes, I have new address ready.</p>
                                        </div>
                                    </div>
                                    <div className={noIsSelected} onClick={(e) => this.selectImage(false)}>
                                        <img src="./img/apartment.png" alt="" width="100px"/>

                                        <div className="option-image-label">
                                            <p>No, give me recommendations.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="options-footer">
                        <div className="pull-right">
                            <Link to="/move-in-date">
                                <button className="next-btn">
                                    Next
                                </button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Questionnaire;