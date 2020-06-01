import React, { Component } from 'react';

class BotInput extends Component{
    constructor(props){
        super(props)
    }

    render(){
        return(
            <div className="chatheader">
                <input className="chat-input border border-light rounded" type="text" />
                <button className="btn btn-sm btn-primary chat-button">Submit</button>
            </div>
        )
    }
}

export default BotInput;