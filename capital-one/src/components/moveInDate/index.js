import React, { Component } from 'react';
import "./move-in-date.css";

class MoveInDate extends Component {
    constructor() {
        super();
        this.state = {
            month: '',
            date: '',
            year: ''
        };

        this.onChange = this.onChange.bind(this);
    }

    onChange (e) {
        const name = e.target.getAttribute("data-name");
        const value = e.target.value;
        this.setState({[name]: value});
        console.log(this.state);
    }

    render() {
        return (
            <div className="container-fluid">
                <div className="sf-bg-img"> <div className="bg-layer"></div></div>
                <div className="main-content">
                    <div className="questions">
                        <div className="question-text">
                            <p>What date will you move in?</p>

                            <div className="response">
                                <div className="move-in-date">
                                    <div className="month-input" >
                                        <input type="text" onChange={this.onChange} data-name="month" value={this.state.month}/>    <span className="slash">/</span>
                                    </div>
                                    <div className="date-input">
                                        <input type="text" onChange={this.onChange} data-name="date" value={this.state.date}/>    <span className="slash">/</span>
                                    </div>
                                    <div className="year-input">
                                        <input type="text" onChange={this.onChange} data-name="year" value={this.state.year}/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="options-footer">
                        <div className="pull-right">
                            <button className="next-btn">
                                Next
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default MoveInDate;