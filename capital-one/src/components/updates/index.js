import React, { Component } from 'react';
import {
  Link
} from 'react-router-dom';

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
                        <p>Lucky day</p>
                        <p>We will do below items for you for FREE!</p>
                    </div>
                    <div className="update-address">
                        <div className="free-item">
                            <div className="item-icon">
                                <img src="./img/001-city-hall.png" alt=""/>
                            </div>
                            <div className="item-text">
                                Update DMV Address
                            </div>
                        </div>
                        <div className="free-item">
                            <div className="item-icon">
                                 <img src="./img/004-credit-card.png" alt=""/>
                            </div>
                            <div className="item-text">
                                Update Billing Address at Banks
                            </div>
                        </div>
                        <div className="free-item">
                            <div className="item-icon">
                                 <img src="./img/003-house.png" alt=""/>
                            </div>
                            <div className="item-text">
                                Update Your Insurance Address 
                            </div>
                        </div>
                        <div className="free-item">
                            <div className="item-icon">
                                 <img src="./img/002-moving-truck.png" alt=""/>
                            </div>
                            <div className="item-text">
                                Free quotes for moving
                            </div>
                        </div>
                    </div>

                    <div className="options-footer">
                        <div className="pull-right">
                            <Link to="/all-service">
                                <button className="sign-up-btn">
                                    Confirm
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