import React, {useState} from 'react';
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";

const HomePage = (props) =>{
    const [counter, setCounter] = useState(0);

    return (
        <Router>
            <Switch>
                <Route exact path='/'>
                    <p onClick={()=>setCounter(counter+1)}>
                        Home Page {counter}
                    </p>
                </Route>
            </Switch>
        </Router>
    );
}

export default HomePage