import React, { Component } from 'react';
import {
  Link
} from 'react-router-dom';

class AddressInput extends Component {
  constructor(props) {
    super(props)
    this.state = { address: '123 State St., Chicago, IL' }
    this.onChange = (e) => this.setState({ address: [e.target.value] });
  }

    render() {
        return (
            <div className="container-fluid">
                <div className="sf-bg-img"> <div className="bg-layer"></div></div>
                <div className="main-content">
                    <div className="questions">
                        <div className="question-text">
                            <p>Where are you moving to?</p>

                            <div className="response">
                                <input type="text" value={this.state.address} onChange={this.onChange}/>
                            </div>
                        </div>
                    </div>
                    <div className="options-footer">
                        <div className="pull-right">
                            <Link to="/services">
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

export default AddressInput;