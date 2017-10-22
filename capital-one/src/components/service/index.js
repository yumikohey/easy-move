import React, { Component } from 'react';
import {
  Link
} from 'react-router-dom';
import "./services.css";

class Service extends Component {
  constructor(props) {
    super(props)
    this.state = {
        option1: true,
        option2: true,
        option3: true,
        option4: true,
        option5: true,
        option6: true,
        option7: true,
        option8: true,
    }
    this.handleChangeChk = (e) => {
        const name = e.target.getAttribute("data-name");
        const value = e.target.value;
        this.setState({name: !value});
    }
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
                                <ul className="list">
                                    <li className="list__item">
                                        <label className="label--checkbox">
                                        <input type="checkbox" className="checkbox" data-name="option1" defaultChecked={this.state.option1} onChange={this.handleChangeChk} />
                                            <span className="label-text">ComEd</span>
                                        </label>
                                    </li>
                                    <li className="list__item">
                                        <label className="label--checkbox">
                                        <input type="checkbox" className="checkbox" data-name="option2" defaultChecked={this.state.option2} onChange={this.handleChangeChk}/>
                                            <span className="label-text">Water Service</span>
                                        </label>
                                    </li>
                                    <li className="list__item">
                                        <label className="label--checkbox">
                                        <input type="checkbox" className="checkbox" data-name="option3" defaultChecked={this.state.option3} onChange={this.handleChangeChk}/>
                                            <span className="label-text">Comcast</span>
                                        </label>
                                    </li>
                                    <li className="list__item">
                                        <label className="label--checkbox">
                                        <input type="checkbox" className="checkbox" data-name="option4" defaultChecked={this.state.option4} onChange={this.handleChangeChk}/>
                                            <span className="label-text">Street Parking Stickers</span>
                                        </label>
                                    </li>
                                </ul>
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
                            <div className="check-box-section">
                                <ul className="list">
                                    <li className="list__item">
                                        <label className="label--checkbox">
                                        <input type="checkbox" className="checkbox" data-name="option5" defaultChecked={this.state.option5} onChange={this.handleChangeChk}/>
                                            <span className="label-text">ComEd</span>
                                        </label>
                                    </li>
                                    <li className="list__item">
                                        <label className="label--checkbox">
                                        <input type="checkbox" className="checkbox" data-name="option6" defaultChecked={this.state.option6} onChange={this.handleChangeChk}/>
                                            <span className="label-text">Water Service</span>
                                        </label>
                                    </li>
                                    <li className="list__item">
                                        <label className="label--checkbox">
                                        <input type="checkbox" className="checkbox" data-name="option7" defaultChecked={this.state.option7} onChange={this.handleChangeChk}/>
                                            <span className="label-text">Comcast</span>
                                        </label>
                                    </li>
                                    <li className="list__item">
                                        <label className="label--checkbox">
                                        <input type="checkbox" className="checkbox" data-name="option8" defaultChecked={this.state.option8} onChange={this.handleChangeChk}/>
                                            <span className="label-text">Street Parking Stickers</span>
                                        </label>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div className="options-footer">
                        <div className="pull-right">
                            <Link to="/all-service">
                                <button className="sign-up-btn">
                                    Do it for me
                                </button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Service;