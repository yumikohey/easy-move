import React, { Component } from 'react';
import "./questionnaire.css";

class Questionnaire extends Component {
    render() {
        return (
            <div className="container-fluid">
                <div className="sf-bg-img"> <div className="bg-layer"></div></div>
                <div className="main-content">
                    <div className="questions">
                        <div className="question-text">
                            <p>Have you found a new place to move in yet?</p>

                            <div className="response">
                                <div className="two-option-images">
                                    <div className="option-image">
                                        <img src="./img/apartment.png" alt="" width="100px"/>

                                        <div className="option-image-label">
                                            <p>Yes, I have new address ready.</p>
                                        </div>
                                    </div>
                                    <div className="option-image">
                                        <img src="./img/apartment.png" alt="" width="100px"/>

                                        <div className="option-image-label">
                                            <p>No, give me recommendations.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="question-text">
                            <p>What is your new address?</p>

                            <div className="response">
                                <input type="text" value=""/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Questionnaire;