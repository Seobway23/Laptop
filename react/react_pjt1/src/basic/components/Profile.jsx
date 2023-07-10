import React from 'react';
import Avartar from './Avartar';

export default function Profile({image, name, title, isNew}) {
    return (
        <div className = "profile">
            <button onClick={(event)=>{
                console.log(event);
                alert('버튼이 클릭됨');
            }}>버튼</button>
            < Avartar image={image} isNew={isNew} />
            <h1>{name}</h1>
            <p>{title}</p>
        </div>
    );
}

