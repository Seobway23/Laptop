import React from 'react';
import {
    atom,
    // selector,
    // useRecoilState,
    useRecoilValue,
  } from 'recoil';
  
const todoListState = atom({
  key: 'TodoList',
  default: [],
})

export default function State() {
const todoList = useRecoilValue(todoListState)

  return (
    <div>
      {todoList}
    </div>
  );
}

