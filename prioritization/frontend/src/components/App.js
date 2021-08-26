import React, {Component} from "react";
import {render} from "react-dom";
import Admin from "./Dashboard/src/layouts/Admin";

import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";

import "./Dashboard/src/assets/css/material-dashboard-react.css?v=1.10.0"
import RTL from "./Dashboard/src/layouts/RTL";


const App =(props) => {


        return (
            <BrowserRouter>
                <Switch>
                  <Route path="/admin" component={Admin} />
                  <Route path="/rtl" component={RTL} />
                  <Redirect from="/" to="/admin/dashboard" />
                </Switch>
            </BrowserRouter>
            );

}


const appDiv = document.getElementById("app");
render(<App name="tim" />, appDiv);

export default App