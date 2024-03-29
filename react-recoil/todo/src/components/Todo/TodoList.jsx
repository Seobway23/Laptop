// TodoList.js
import React from 'react';
import { useRecoilValue } from 'recoil';
import { todoListState } from '../../state/TodoList';
import TodoItem from './TodoItem';
import TodoItemCreator from './TodoItemCreator';

function TodoList() {
  const todoList = useRecoilValue(todoListState);
  return (
    <>
      {/* <TodoListStats /> */}
      {/* <TodoListFilters /> */}
      <TodoItemCreator />

      {todoList.map((todoItem) => (
        <TodoItem key={todoItem.id} item={todoItem} />
      ))}
    </>
  );
}

export default TodoList;
