// TodoItemCreator.js
import React, { useState } from 'react';
import { useSetRecoilState } from 'recoil';
import { todoListState } from '../../state/TodoList';

function TodoItemCreator() {
  const [inputValue, setInputValue] = useState('');
  const setTodoList = useSetRecoilState(todoListState);

//   console.log(setTodoList)

  const addItem = () => {
    setTodoList((oldTodoList) => [
      ...oldTodoList,
      {
        id: getId(),
        text: inputValue,
        isComplete: false,
      },
    ]);
    setInputValue('');
  };

  const onChange = ({ target: { value } }) => {
    setInputValue(value);
  };

  const handleKeyUp = (event) => {
    if (event.key === 'Enter') {
      addItem();
    }
  };

  return (
    <div>
      <input
        id="inputField"
        type="text"
        value={inputValue}
        onChange={onChange}
        onKeyUp={handleKeyUp}
      />
      <button onClick={addItem}>Add</button>
    </div>
  );
}

// utility for creating unique Id
let id = 0;
function getId() {
  return id++;
}

export default TodoItemCreator;
