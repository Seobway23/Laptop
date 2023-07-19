import React from 'react';

export default function Hello() {
    return (
        <div>
            <button
            type="button"
            onClick={() => {
                alert('Hello');
            }}
            
            >Hello </button>
        </div>
    );
}

