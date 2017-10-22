import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter,
  Route
} from 'react-router-dom';
import Home from "./components/home/index";
import Questionnaire from "./components/questionnaire/index";
import "./index.css";

ReactDOM.render(
    <BrowserRouter>
        <div>
            <Route exact path="/" component={Home} />
            <Route path="/redirect" component={Questionnaire}/>
        </div>
    </BrowserRouter>, document.getElementById('root')
);

