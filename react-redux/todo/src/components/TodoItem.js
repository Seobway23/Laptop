// src/components/TodoItem.js
import React from 'react';
import { connect } from 'react-redux';
import { removeTodo } from './redux/actions';

const TodoItem = ({ todo, removeTodo }) => {
  const handleRemoveTodo = () => {
    removeTodo(todo.id);
  };

  return (
    <li>
      {todo.text}
      <button onClick={handleRemoveTodo}>Remove</button>
    </li>
  );
};

const mapDispatchToProps = {
  removeTodo
};

export default connect(null, mapDispatchToProps)(TodoItem);
