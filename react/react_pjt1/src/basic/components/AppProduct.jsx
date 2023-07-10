import React, { useState } from 'react';
// import './App.css';
// import Products from './components/Products'

export default function AppProduct() {
    const [showProducts, setShowProducts] = useState(true);
    return (
        <div>
            {/* {showProducts && <Products/>} */}
            <button onClick={()=> setShowProducts((show) => !show)}> Toggle</button>
            
        </div>
    );
}

