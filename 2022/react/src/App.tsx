import logo from './logo.svg';
import './App.css';
import Day from "./common/day";
import React from "react";

const App = () => {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo"/>
                <div className={"AOCTitle"}>aoc 2022</div>
                <div className={"Line"}></div>
                <Day dayNumber={1}></Day>
                <Day dayNumber={2}></Day>
                <Day dayNumber={3}></Day>
            </header>
        </div>
    );
}

export default App;
