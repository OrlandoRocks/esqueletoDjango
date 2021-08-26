import React, {useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TablePagination from '@material-ui/core/TablePagination';
import TableRow from '@material-ui/core/TableRow';

const PrioritizationStatus = (props) =>{
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