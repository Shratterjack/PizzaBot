import React, { Component } from 'react';

class BotBody extends Component {
    constructor(props){
        super(props);
    }

   componentWillMount(){

   }


    render(){
        return(
            <div className="chatbody">
                {/* <BotMessage /> */}
                <ul className="list-unstyled">
                    <li className="media">
                        <div className="media-body">
                            <div className="bot-message-box border border-light rounded">
                                <div className="bot-message-text">
                                    <span>hello world</span>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li className="media">
                        <div className="media-body">
                            <div className="chat-message-box ">
                                <div className="bot-message-text">
                                    <span>hello world</span>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li className="media">
                        <div className="media-body">
                            <div className="bot-message-box border border-light rounded">
                                <div className="bot-message-text">
                                    <span>hello world</span>
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        )
    }
}

export default BotBody;