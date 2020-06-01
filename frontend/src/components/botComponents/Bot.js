import React, { Component } from 'react';
import BotHeader from './BotHeader';
import BotBody from './BotBody';
import BotInput from './BotInput';

import '../../css/bot.css'

class Bot extends Component {
    constructor(props){
        super(props)
    }

    render(){
        return (
            <div className="container chat border border-light">
                <div className="justify-content-center align-items-center">
                    <BotHeader />
                    <BotBody />
                    <BotInput/>
                </div>
            </div>
        )
    }    
}

export default Bot;