import React, { useState } from 'react';
import {v4 as uuidv4} from 'uuid';


export default function AddTodo({onAdd}) {

    const [text, setText] = useState(''); // 처음 시작하는 문자, 숫자

    const handleChange= (e) => setText(e.target.value)

    const handleSubmit = (e) => {
        e.preventDefault();

        if (text.trim().length===0) {
            alert('제대로 작성해')
            return;
        }

        onAdd({id: uuidv4(), text, status: 'active'});
        setText('');

    }
    return (
        <form onSubmit={handleSubmit}>
            <input 
            type="text" 
            placeholder='Add Todo' 
            value={text} 
            onChange={handleChange}
            />
            <button>Add</button>
        </form>
    );
}

