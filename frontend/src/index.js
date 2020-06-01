import React from "react";
import ReactDOM from "react-dom";
import Bot from './components/botComponents/Bot';


const App = () => {
    return (
        <div>
            <Bot/>
        </div>
    );
};

ReactDOM.render(<App />, document.querySelector("#root"));