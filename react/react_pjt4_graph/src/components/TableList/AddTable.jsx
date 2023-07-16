import React, { useState } from 'react';
import {v4 as uuidv4} from 'uuid';

export default function AddTable({onAdd}) {
    const [list, setList] = useState([]);

    const handleChange = (e) => {
        setList(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault()

        if (list.length===0 ) {
            alert('제대로 작성해 시발아')
            return ;
        }

        onAdd({id: uuidv4(), list})
        setList('')
        
    }

    return (
        <form
            onSubmit={handleSubmit}>

            <input type="text" 
            placeholder='Add List'
            value={list}
            onChange={handleChange}
            />
            <button>Add</button>
        </form>
    );
}

