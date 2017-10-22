import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter,
  Route
} from 'react-router-dom';
import Home from "./components/home/index";
import Questionnaire from "./components/questionnaire/index";
import MoveInDate from "./components/moveInDate/index";
import AddressInput from "./components/address/index";
import Service from "./components/service/index";
import "./index.css";

ReactDOM.render(
    <BrowserRouter>
        <div>
            <Route exact path="/" component={Home} />
            <Route path="/redirect" component={Questionnaire} />
            <Route path="/move-in-date" component={MoveInDate} />
            <Route path="/place" component={AddressInput} />
            <Route path="/services" component={Service} />
        </div>
    </BrowserRouter>, document.getElementById('root')
);

