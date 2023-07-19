import './App.css';
import React from 'react';
import { RecoilRoot } from 'recoil';
import TodoList from './components/Todo/TodoList';


function App() {
  return (
    <RecoilRoot>
      <TodoList />
      <body>
        <p>test</p>
      </body>
      <footer>
        <h3>footer</h3>
        <div>여기는 footer입니다. height: 110px, width: 100%, position: absolute </div>
      </footer>
    </RecoilRoot>
  );
}

export default App;
