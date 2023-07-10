import React, { useState } from 'react';
import './App.css';

export default function Pointer() {
    const [position, setPosition] = useState({x:0, y:0})
    return (
        <div className='container' 
        onPointerMove={(e)=> {
            console.log('X:', e.clientX, ' Y:', e.clientY )
            // setPosition({x:e.clientX, y: e.clientY})
            setPosition((prev)=> ({...prev, x: e.clientX}))
        }}>
            <dir className='pointer' style={{ transform: `translate(${position.x}px, ${position.y}px)`}}/>
        </div>
    );
}

