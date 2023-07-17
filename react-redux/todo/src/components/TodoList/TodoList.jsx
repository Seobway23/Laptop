import React from 'react';
import { useSelector } from 'react-redux';
import AddTodo from '../AddTodo/AddTodo';


export default function TodoList() {
    const List = useSelector((state)=> state)

    return (
        <div>
            <ul>
                <li>{List}</li>
                <AddTodo/>


            </ul>
        </div>
    );
}

