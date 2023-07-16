import React from 'react';
import {FaTrashAlt} from 'react-icons/fa';


export default function Todo({todo, onUpdate, onDelete}) {
    const {text, status} = todo;
    const handleChanged = (e) => {
        const status = e.target.checked ? 'completed' : 'active';
        onUpdate({...todo, status})
    }
    const handleDeleted = () => {
        onDelete(todo)
    };
    
    return (
       <li>
        <input 
            type="checkbox" 
            id='checkbox'
            checked={status === 'completed'}
            onChange={handleChanged}
        />
        <label htmlFor="checkbox">{text}</label>
        <button onClick = {handleDeleted}>
            <FaTrashAlt/>
        </button>
       </li>
    );
    // yarn add react-icons 사용
}

