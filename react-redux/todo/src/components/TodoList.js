// src/components/TodoList.js
import React, { useState } from 'react';
import { connect } from 'react-redux';
import { addTodo } from './redux/actions';


import TodoItem from './TodoItem';

const TodoList = ({ todos, addTodo }) => {
  const [newTodo, setNewTodo] = useState('');

  const handleAddTodo = () => {
    if (newTodo.trim()) {
      addTodo({
        id: Date.now(),
        text: newTodo
      });
      setNewTodo('');
    }
  };

  return (
    <div>
      <input type="text" value={newTodo} onChange={(e) => setNewTodo(e.target.value)} />
      <button onClick={handleAddTodo}>Add Todo</button>
      <ul>
        {todos.map((todo) => (
          <TodoItem key={todo.id} todo={todo} />
        ))}
      </ul>
    </div>
  );
};

const mapStateToProps = (state) => ({
  todos: state.todos
});

const mapDispatchToProps = {
  addTodo
};

export default connect(mapStateToProps, mapDispatchToProps)(TodoList);
