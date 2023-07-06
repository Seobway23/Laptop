import React from 'react';

export default function Avartar({image, isNew}) {
    return (
        <div className='avartar'>
            <img className="photo" src={image} alt="avatar"
            />
            { isNew && <span className='new'> NEW</span> }
        </div>
    );
}

