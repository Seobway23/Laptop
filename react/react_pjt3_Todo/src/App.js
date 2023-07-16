
import './App.css';
import TodoList from './components/TodoList/TodoList';
import { useSelector } from 'react-redux';
import Header from './components/Header/Header';
import {useState} from 'react';

const filters = ['all', 'active', 'completed']

function App() {
  const [filter, setFilter] = useState(filters[0])

  const 리스트 = useSelector((state)=> state)
  
  return (
    <>
      <Header
      filters={filters}
      filter={filter}
      onFilterChange={setFilter}
      />
      <TodoList filter={filter} />
      
      <h1>{리스트}</h1>

    </>

  );
}

export default App;
