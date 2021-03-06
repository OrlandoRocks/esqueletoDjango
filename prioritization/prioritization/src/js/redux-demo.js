const redux = require('redux');

const counterReducer = (state = {counter:0}, action) => {
    if(action.type === 'increment'){
        return {
        counter: state.counter + 1
        };
    }
    if(action.type === 'decrement'){
        return {
        counter: state.counter - 1
        };
    }

};

const store = redux.createStore(counterReducer);

const counterSuscriber = () => {
    //get the last state
    const latesState = store.getState();
    console.log(latesState);
}

store.subscribe(counterSuscriber);


store.dispatch({type:'increment'});
store.dispatch({type:'decrement'});


