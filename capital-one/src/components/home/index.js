import React, { Component } from 'react';
import { loginRedirectURL } from "../../secrets";
import "./home.css";

class Home extends Component {
    constructor() {
        super();
    };

    signUpButton (){
        return window.location = `http://api.devexhacks.com/oauth2/authorize?client_id=vgw3sf4f8nq3b98i1gdfr8wpx4gpty0ska52&grant_type=authorization_code&redirect_uri=${loginRedirectURL}&scope=openid%20signup&response_type=code`;
    }

    render() {
        return (
            <div className="container-fluid">
                <div className="bg-img">
                    <div className="login-box">
                        <div className="left">
                            <div className="description">
                                <h1 className="google-font">EASY MOVE</h1>
                                <h3>
                                    Using <b> Capital One </b> sign in,<br/>
                                    moving has never been easier.
                                </h3>
                            </div>
                            <div className="bullet-points">
                                <div>- Friendly</div>
                                <div>- Seemlessly</div>
                                <div>- No more time consuming </div>
                            </div>
                        </div>
                        <div className="right">
                            <img src="./img/capital_one_logo.png" />
                            
                            <div className="login-buttons">
                                <button onClick={e => { this.signUpButton() }}>Sign Up</button>
                                <button onClick={e => {this.signUpButton() }}>Sign In</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Home;