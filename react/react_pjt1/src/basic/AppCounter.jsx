import React, { useState } from 'react';
import Counter from './components/Counter';
import './App.css';
import AppProduct from './components/AppProduct';

export default function AppCounter() {
    const [showProducts, setShowProducts] = useState(true);
    return (
        <div className='container'>
            <Counter/>
            <Counter/>
            {showProducts && <AppProduct/>}
            <button onClick={()=> setShowProducts((show) => !show)}> Toggle</button>
        </div>
    );
}

