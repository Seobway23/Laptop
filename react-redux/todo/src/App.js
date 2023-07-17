import { useSelector } from 'react-redux';
import './App.css';
// import TodoList from './components/TodoList/TodoList';
import TodoList from './components/TodoList';

function App() {
  const List = useSelector((state)=> state)
  console.log(List)
  return (
    <div className="App">
      <h1> To do 게시판</h1>
        <TodoList></TodoList>
    </div>
  );
}

export default App;
