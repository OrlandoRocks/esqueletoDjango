import React, {useState} from 'react';
import Admin from "./Dashboard/src/layouts/Admin";

const DashboardUi = (props) =>{
    const [counter, setCounter] = useState(0);

    return <Admin/>;
}

export default DashboardUi